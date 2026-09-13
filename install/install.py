"""Install standing writing rules for Codex, Claude Code, and Grok.

A bare run writes nothing until you approve. In a terminal: checkbox of
detected agents (up/down, Space, Enter), unified diffs, then Apply? [y/N].
"""

from __future__ import annotations

import argparse
import difflib
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

AGENT_HOMES = {
    "codex": ".codex",
    "claude": ".claude",
    "grok": ".grok",
}
AGENTS_MD_AGENTS = frozenset({"codex", "grok"})
CLAUDE_LINK_NAME = "clear-precise-writing"
SKILL_NAME = "write-commit-messages"
OLD_SKILL_NAME = "clear-precise-communication"
STANDING_FILES = (
    ("clear-precise-communication.md", Path("rules") / "clear-precise-communication.md"),
    ("clean-code-principles.md", Path("rules") / "clean-code-principles.md"),
)

COMM_STANZA = """\
## Mandatory ambient communication and writing guidance

At the beginning of each session, read `{path}` completely and apply it throughout the session.

Do not reread it during the same session, unless immediately after a compaction.
"""

CODE_STANZA = """\
## Mandatory code writing guidance

Anytime you are writing or reviewing code, read `{path}` completely and apply it.

Do not reread it during the same session, unless writing or reviewing code after a compaction.
"""


@dataclass
class Operation:
    title: str
    diff: str
    dest: Path
    backup_src: Path | None
    apply: Callable[[], None]


def use_symlinks() -> bool:
    return os.name != "nt"


def tilde(path: Path, home: Path) -> str:
    path = path.absolute()
    home = home.absolute()
    try:
        return "~/" + path.relative_to(home).as_posix()
    except ValueError:
        return str(path)


def unified_diff(old: str, new: str, label: str) -> str:
    return "".join(
        difflib.unified_diff(
            old.splitlines(keepends=True),
            new.splitlines(keepends=True),
            fromfile=f"a/{label}",
            tofile=f"b/{label}",
        )
    )


def symlink_diff(label: str, source: Path) -> str:
    return unified_diff("", f"symlink → {source}\n", label)


def detect_agents(home: Path) -> list[str]:
    return [name for name, rel in AGENT_HOMES.items() if (home / rel).is_dir()]


def parse_agents(raw: str | None) -> list[str]:
    if not raw:
        return []
    names = [part.strip() for part in raw.split(",") if part.strip()]
    unknown = [name for name in names if name not in AGENT_HOMES]
    if unknown:
        raise SystemExit(f"Unknown agent(s): {', '.join(unknown)}")
    return names


def claude_tree(repo: Path, economy: bool, gitlab: bool) -> Path:
    name = "claude-rules-economy" if economy else "claude-rules"
    if gitlab:
        return repo / "gitlab" / name
    return repo / name


def all_claude_trees(repo: Path) -> list[Path]:
    return [
        claude_tree(repo, economy, gitlab)
        for gitlab in (False, True)
        for economy in (False, True)
    ]


def _files_match(left: Path, right: Path) -> bool:
    left_files = {path.relative_to(left) for path in left.rglob("*") if path.is_file()}
    right_files = {path.relative_to(right) for path in right.rglob("*") if path.is_file()}
    if left_files != right_files:
        return False
    return all(
        (left / rel).read_bytes() == (right / rel).read_bytes() for rel in left_files
    )


def points_at(dest: Path, source: Path) -> bool:
    if dest.is_symlink():
        try:
            return dest.resolve() == source.resolve()
        except OSError:
            return False
    if not dest.exists():
        return False
    if dest.is_file() and source.is_file():
        return dest.read_bytes() == source.read_bytes()
    if dest.is_dir() and source.is_dir():
        return _files_match(dest, source)
    return False


def find_claude_link(rules_dir: Path, repo: Path) -> Path | None:
    if not rules_dir.is_dir():
        return None
    wanted = {path.resolve() for path in all_claude_trees(repo)}
    for child in sorted(rules_dir.iterdir()):
        try:
            if child.resolve() in wanted:
                return child
        except OSError:
            continue
    return None


def display_path(path: Path, home: Path) -> str:
    return tilde(path, home)


def mkdir_op(dest: Path, home: Path) -> Operation | None:
    if dest.is_dir():
        return None
    label = display_path(dest, home)

    def apply() -> None:
        dest.mkdir(parents=True, exist_ok=True)

    return Operation(
        title=f"create {label}",
        diff=unified_diff("", f"directory\n", label),
        dest=dest,
        backup_src=None,
        apply=apply,
    )


def _remove_dest(dest: Path) -> None:
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)


def _windows_junction(dest: Path, source: Path) -> None:
    completed = subprocess.run(
        ["cmd", "/c", "mklink", "/J", str(dest), str(source)],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        shutil.copytree(source, dest)


def link_or_copy_op(dest: Path, source: Path, home: Path) -> Operation | None:
    if points_at(dest, source) and (dest.is_symlink() or not use_symlinks()):
        return None
    label = display_path(dest, home)
    backup_src = dest if dest.exists() or dest.is_symlink() else None
    if use_symlinks():
        diff = symlink_diff(label, source)
    elif source.is_dir():
        diff = unified_diff("", f"junction or copy → {source}\n", label)
    else:
        old = dest.read_text(encoding="utf-8") if dest.is_file() and not dest.is_symlink() else ""
        diff = unified_diff(old, source.read_text(encoding="utf-8"), label)

    def apply() -> None:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() or dest.is_symlink():
            _remove_dest(dest)
        if use_symlinks():
            dest.symlink_to(source, target_is_directory=source.is_dir())
        elif source.is_dir():
            _windows_junction(dest, source)
        else:
            shutil.copy2(source, dest)

    return Operation(
        title=f"install {label}",
        diff=diff,
        dest=dest,
        backup_src=backup_src,
        apply=apply,
    )


def stanza_for(filename: str, installed: Path, home: Path) -> str:
    path = tilde(installed, home)
    if filename == "clean-code-principles.md":
        return CODE_STANZA.format(path=path)
    return COMM_STANZA.format(path=path)


def append_missing_stanzas(
    existing: str, installed: Sequence[tuple[str, Path]], home: Path
) -> str:
    text = existing
    for filename, dest in installed:
        if filename in text:
            continue
        stanza = stanza_for(filename, dest, home).strip() + "\n"
        if text.strip():
            text = text.rstrip() + "\n\n" + stanza
        else:
            text = stanza
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def patch_agents_md_op(
    agents_md: Path,
    installed: Sequence[tuple[str, Path]],
    home: Path,
) -> Operation | None:
    existing = agents_md.read_text(encoding="utf-8") if agents_md.is_file() else ""
    new = append_missing_stanzas(existing, installed, home)
    if new == existing or not new:
        return None
    label = display_path(agents_md, home)
    backup_src = agents_md if agents_md.is_file() else None

    def apply() -> None:
        agents_md.parent.mkdir(parents=True, exist_ok=True)
        current = agents_md.read_text(encoding="utf-8") if agents_md.is_file() else ""
        agents_md.write_text(
            append_missing_stanzas(current, installed, home),
            encoding="utf-8",
            newline="\n",
        )

    names = ", ".join(filename for filename, _ in installed if filename not in existing)
    return Operation(
        title=f"point {label} at {names}",
        diff=unified_diff(existing, new, label),
        dest=agents_md,
        backup_src=backup_src,
        apply=apply,
    )


def standing_files(include_clean_code: bool) -> tuple[tuple[str, Path], ...]:
    if include_clean_code:
        return STANDING_FILES
    return tuple(item for item in STANDING_FILES if item[0] != "clean-code-principles.md")


def plan_agents_md_agent(
    *,
    name: str,
    home: Path,
    repo: Path,
    include_skill: bool,
    include_clean_code: bool,
    use_agents_d: bool,
) -> list[Operation]:
    agent_home = home / AGENT_HOMES[name]
    dest_dir = agent_home / "AGENTS.d" if use_agents_d else agent_home
    ops: list[Operation] = []
    directories = [agent_home]
    if dest_dir != agent_home:
        directories.append(dest_dir)
    for directory in directories:
        created = mkdir_op(directory, home)
        if created:
            ops.append(created)
    installed: list[tuple[str, Path]] = []
    for filename, rel in standing_files(include_clean_code):
        source = repo / rel
        dest = dest_dir / filename
        op = link_or_copy_op(dest, source, home)
        if op:
            ops.append(op)
        installed.append((filename, dest))
    stanza = patch_agents_md_op(agent_home / "AGENTS.md", installed, home)
    if stanza:
        ops.append(stanza)
    if include_skill:
        ops.extend(plan_skill(agent_home, repo, home))
    return ops


def plan_skill(agent_home: Path, repo: Path, home: Path) -> list[Operation]:
    dest = agent_home / "skills" / SKILL_NAME
    source = repo / "skills" / SKILL_NAME
    ops: list[Operation] = []
    created = mkdir_op(dest.parent, home)
    if created:
        ops.append(created)
    linked = link_or_copy_op(dest, source, home)
    if linked:
        ops.append(linked)
    return ops


def plan_claude(
    *,
    home: Path,
    repo: Path,
    economy: bool,
    gitlab: bool,
    include_skill: bool,
) -> list[Operation]:
    rules_dir = home / ".claude" / "rules"
    source = claude_tree(repo, economy, gitlab)
    existing = find_claude_link(rules_dir, repo)
    dest = existing if existing is not None else rules_dir / CLAUDE_LINK_NAME
    ops: list[Operation] = []
    for directory in (home / ".claude", rules_dir):
        created = mkdir_op(directory, home)
        if created:
            ops.append(created)
    linked = link_or_copy_op(dest, source, home)
    if linked:
        ops.append(linked)
    if include_skill:
        ops.extend(plan_skill(home / ".claude", repo, home))
    return ops


def decide_agents_d(
    *,
    selected: Sequence[str],
    home: Path,
    assume_yes: bool,
    isatty: bool,
    stdin,
    stdout,
) -> dict[str, bool]:
    choices: dict[str, bool] = {}
    for name in selected:
        if name not in AGENTS_MD_AGENTS:
            continue
        agents_d = home / AGENT_HOMES[name] / "AGENTS.d"
        if agents_d.is_dir() or assume_yes or not isatty:
            choices[name] = True
            continue
        prompt = f"Create {tilde(agents_d, home)} for standing files? [Y/n] "
        stdout.write(prompt)
        stdout.flush()
        answer = stdin.readline()
        if not answer:
            choices[name] = True
            continue
        choices[name] = answer.strip().lower() not in {"n", "no"}
    return choices


def plan_all(
    *,
    selected: Sequence[str],
    home: Path,
    repo: Path,
    economy: bool,
    gitlab: bool,
    include_skill: bool,
    include_clean_code: bool,
    agents_d_for: dict[str, bool],
) -> list[Operation]:
    ops: list[Operation] = []
    for name in selected:
        if name in AGENTS_MD_AGENTS:
            ops.extend(
                plan_agents_md_agent(
                    name=name,
                    home=home,
                    repo=repo,
                    include_skill=include_skill,
                    include_clean_code=include_clean_code,
                    use_agents_d=agents_d_for.get(name, True),
                )
            )
        elif name == "claude":
            ops.extend(
                plan_claude(
                    home=home,
                    repo=repo,
                    economy=economy,
                    gitlab=gitlab,
                    include_skill=include_skill,
                )
            )
    return ops


def backup_path(path: Path, backup_root: Path, home: Path) -> Path:
    try:
        rel = path.resolve().relative_to(home.resolve())
    except ValueError:
        rel = Path(path.name)
    target = backup_root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink() or path.is_file():
        shutil.copy2(path, target, follow_symlinks=False)
    else:
        shutil.copytree(path, target, symlinks=True)
    return target


def apply_operations(ops: Sequence[Operation], home: Path, stdout) -> Path | None:
    to_backup = [op.backup_src for op in ops if op.backup_src is not None]
    backup_root = None
    if to_backup:
        backup_root = Path(
            tempfile.mkdtemp(prefix="clear-precise-communication-")
        )
        stdout.write(f"Backup: {backup_root}\n")
        for src in to_backup:
            backup_path(src, backup_root, home)
    for op in ops:
        op.apply()
    return backup_root


def doctor_link(dest: Path, source: Path, home: Path) -> str | None:
    label = display_path(dest, home)
    if dest.is_symlink():
        try:
            if dest.resolve() == source.resolve():
                return None
            return f"FAIL {label} points at {dest.resolve()}, expected {source}"
        except OSError:
            return f"FAIL {label} is a broken symlink"
    if not dest.exists():
        return f"FAIL {label} is missing"
    if points_at(dest, source):
        if use_symlinks():
            return f"WARN {label} is a copy; git pull will not update it"
        return None
    return f"FAIL {label} does not match {source}"


def doctor_agents_md(agents_md: Path, filename: str, home: Path) -> str | None:
    label = display_path(agents_md, home)
    if not agents_md.is_file():
        return f"FAIL {label} is missing"
    if filename not in agents_md.read_text(encoding="utf-8"):
        return f"FAIL {label} does not mention {filename}"
    return None


def warn_old_skill(home: Path, stdout) -> None:
    for rel in (".codex/skills", ".claude/skills"):
        leftover = home / rel / OLD_SKILL_NAME
        if leftover.exists() or leftover.is_symlink():
            stdout.write(
                f"WARN leftover always-on skill at {tilde(leftover, home)}\n"
            )


def warn_documentation_tone(home: Path, repo: Path, stdout) -> None:
    tone = home / ".claude" / "rules" / "documentation-tone.md"
    if not tone.exists() or tone.is_symlink():
        return
    trees = all_claude_trees(repo)
    try:
        resolved = tone.resolve()
    except OSError:
        stdout.write(f"WARN {tilde(tone, home)} exists and is not a symlink\n")
        return
    if any(resolved.is_relative_to(tree.resolve()) for tree in trees):
        return
    stdout.write(
        f"WARN {tilde(tone, home)} competes with claude-rules/documentation-tone.md\n"
    )


def run_doctor(
    *,
    selected: Sequence[str],
    home: Path,
    repo: Path,
    economy: bool,
    gitlab: bool,
    include_skill: bool,
    include_clean_code: bool,
    stdout,
) -> int:
    failures = 0
    for name in selected:
        if name in AGENTS_MD_AGENTS:
            agent_home = home / AGENT_HOMES[name]
            agents_d = agent_home / "AGENTS.d"
            dest_dir = agents_d if agents_d.is_dir() else agent_home
            for filename, rel in standing_files(include_clean_code):
                dest = dest_dir / filename
                issue = doctor_link(dest, repo / rel, home)
                if issue:
                    stdout.write(issue + "\n")
                    if issue.startswith("FAIL"):
                        failures += 1
                issue = doctor_agents_md(agent_home / "AGENTS.md", filename, home)
                if issue:
                    stdout.write(issue + "\n")
                    failures += 1
            if include_skill:
                issue = doctor_link(
                    agent_home / "skills" / SKILL_NAME,
                    repo / "skills" / SKILL_NAME,
                    home,
                )
                if issue:
                    stdout.write(issue + "\n")
                    if issue.startswith("FAIL"):
                        failures += 1
        elif name == "claude":
            rules_dir = home / ".claude" / "rules"
            source = claude_tree(repo, economy, gitlab)
            existing = find_claude_link(rules_dir, repo)
            dest = existing if existing is not None else rules_dir / CLAUDE_LINK_NAME
            if existing is not None and not points_at(existing, source):
                stdout.write(
                    f"FAIL {display_path(existing, home)} points at "
                    f"{existing.resolve()}, expected {source}\n"
                )
                failures += 1
            else:
                issue = doctor_link(dest, source, home)
                if issue:
                    stdout.write(issue + "\n")
                    if issue.startswith("FAIL"):
                        failures += 1
            if include_skill:
                issue = doctor_link(
                    home / ".claude" / "skills" / SKILL_NAME,
                    repo / "skills" / SKILL_NAME,
                    home,
                )
                if issue:
                    stdout.write(issue + "\n")
                    if issue.startswith("FAIL"):
                        failures += 1
            warn_documentation_tone(home, repo, stdout)
    warn_old_skill(home, stdout)
    if failures:
        stdout.write(f"{failures} check(s) failed.\n")
        return 1
    stdout.write("Install looks complete.\n")
    return 0


def _read_key_posix() -> str:
    import termios
    import tty

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            return ch + sys.stdin.read(2)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_key_windows() -> str:
    import msvcrt

    ch = msvcrt.getwch()
    if ch in ("\x00", "\xe0"):
        extra = msvcrt.getwch()
        return {"H": "up", "P": "down"}.get(extra, extra)
    return ch


def read_key() -> str:
    if os.name == "nt":
        return _read_key_windows()
    return _read_key_posix()


def normalize_key(raw: str) -> str:
    if raw in {"\x1b[A", "\x1bOA", "up", "k"}:
        return "up"
    if raw in {"\x1b[B", "\x1bOB", "down", "j"}:
        return "down"
    if raw == " ":
        return "space"
    if raw in {"\r", "\n"}:
        return "enter"
    if raw in {"q", "\x03"}:
        return "quit"
    return raw


def checkbox_tui(agents: Sequence[str], home: Path, stdout) -> list[str]:
    checked = [True] * len(agents)
    index = 0
    stdout.write("\x1b[?25l")
    try:
        while True:
            lines = ["Select agents to configure", ""]
            for i, name in enumerate(agents):
                mark = "x" if checked[i] else " "
                cursor = ">" if i == index else " "
                location = home / AGENT_HOMES[name]
                lines.append(
                    f"{cursor} [{mark}] {name:<7} {tilde(location, home)}"
                )
            lines.append("")
            lines.append("Up/down  Space toggle  Enter continue  q abort")
            view = "\n".join(lines)
            stdout.write(view)
            stdout.flush()
            key = normalize_key(read_key())
            stdout.write(f"\x1b[{len(lines)}A\x1b[J")
            if key == "up":
                index = (index - 1) % len(agents)
            elif key == "down":
                index = (index + 1) % len(agents)
            elif key == "space":
                checked[index] = not checked[index]
            elif key == "enter":
                return [name for name, on in zip(agents, checked, strict=True) if on]
            elif key == "quit":
                raise SystemExit(1)
    finally:
        stdout.write("\x1b[?25h")
        stdout.flush()


def confirm_apply(count: int, stdin, stdout) -> bool:
    stdout.write(f"Apply {count} change(s)? [y/N] ")
    stdout.flush()
    answer = stdin.readline()
    if not answer:
        return False
    return answer.strip().lower() in {"y", "yes"}


def print_ops(ops: Sequence[Operation], stdout) -> None:
    if not ops:
        stdout.write("Already installed.\n")
        return
    stdout.write(f"{len(ops)} change(s):\n\n")
    for op in ops:
        stdout.write(op.title + "\n")
        stdout.write(op.diff)
        if not op.diff.endswith("\n"):
            stdout.write("\n")
        stdout.write("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Install standing writing rules for Codex, Claude Code, and Grok. "
            "A bare run writes nothing until you approve. In a terminal: "
            "up/down and Space select agents, Enter continues, then unified "
            "diffs, then Apply? [y/N]."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print diffs and write nothing",
    )
    parser.add_argument(
        "--doctor",
        "--check",
        action="store_true",
        help="Check an existing install and write nothing",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the TUI and the apply prompt",
    )
    parser.add_argument(
        "--agents",
        help="Comma-separated subset: codex,claude,grok (skips the TUI)",
    )
    parser.add_argument(
        "--claude-set",
        choices=("full", "economy"),
        default="full",
        help="Claude always-on tree (default: full)",
    )
    parser.add_argument(
        "--gitlab",
        action="store_true",
        help="Use GitLab merge-request wording for Claude trees",
    )
    parser.add_argument(
        "--no-skill",
        action="store_true",
        help="Do not install write-commit-messages",
    )
    parser.add_argument(
        "--no-clean-code",
        action="store_true",
        help="Do not install clean-code-principles.md",
    )
    parser.add_argument(
        "--home",
        type=Path,
        help="Override home directory (tests)",
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    stdin=None,
    stdout=None,
    isatty: bool | None = None,
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    args = build_parser().parse_args(argv)
    home = (args.home or Path.home()).expanduser()
    repo = REPO_ROOT
    tty = stdin.isatty() if isatty is None else isatty
    detected = detect_agents(home)
    requested = parse_agents(args.agents)
    economy = args.claude_set == "economy"

    if not detected and not requested:
        stdout.write(
            f"No agent homes under {home} "
            f"(.codex, .claude, .grok).\n"
        )
        return 1

    if args.doctor:
        selected = requested or detected
        return run_doctor(
            selected=selected,
            home=home,
            repo=repo,
            economy=economy,
            gitlab=args.gitlab,
            include_skill=not args.no_skill,
            include_clean_code=not args.no_clean_code,
            stdout=stdout,
        )

    if requested:
        selected = requested
    elif not tty and not args.yes and not args.dry_run:
        stdout.write("Detected:\n")
        for name in detected:
            stdout.write(f"  {name}  {tilde(home / AGENT_HOMES[name], home)}\n")
        stdout.write(
            "Re-run in a terminal to choose agents, or pass --yes / --dry-run.\n"
        )
        return 0
    elif tty and not args.yes:
        selected = checkbox_tui(detected, home, stdout)
        if not selected:
            stdout.write("No agents selected.\n")
            return 0
    else:
        selected = detected

    agents_d_for = decide_agents_d(
        selected=selected,
        home=home,
        assume_yes=args.yes or args.dry_run,
        isatty=tty and not args.yes and not args.dry_run,
        stdin=stdin,
        stdout=stdout,
    )
    ops = plan_all(
        selected=selected,
        home=home,
        repo=repo,
        economy=economy,
        gitlab=args.gitlab,
        include_skill=not args.no_skill,
        include_clean_code=not args.no_clean_code,
        agents_d_for=agents_d_for,
    )
    print_ops(ops, stdout)
    if not ops or args.dry_run:
        return 0
    if not args.yes:
        if not tty:
            stdout.write("Need a terminal or --yes to apply.\n")
            return 0
        if not confirm_apply(len(ops), stdin, stdout):
            stdout.write("No changes applied.\n")
            return 1
    apply_operations(ops, home, stdout)
    stdout.write("Installed.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
