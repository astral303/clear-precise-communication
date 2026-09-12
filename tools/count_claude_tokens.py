"""Estimate Claude token counts for files.

Uses ctok family 5.0 (Opus 5 and Claude 5). That reconstruction is unofficial
and is not Anthropic's tokenizer. It targets counts, not token boundaries.

On 2026-08-26, ctok 5.0 matched Claude Code /memory integers on every
claude-rules file whose UI value was not rounded to 0.1k:

- no-rhetorical-appositives.md = 862
- pr-bodies-are-permanent-records.md = 920
- pr-text-leads-with-the-bug.md = 998
- noun-phrase-labels-not-questions.md = 1100

Rounded UI values (1.1k, 2.2k) matched after the same 0.1k rounding.
tiktoken cl100k_base and o200k_base undercounted this prose by about 30%.
Do not use tiktoken as the Claude estimate.

Usage, from the repository root:

    uv run python tools/count_claude_tokens.py
    uv run python tools/count_claude_tokens.py claude-rules/final-scan.md
    uv run python tools/count_claude_tokens.py --table
    uv run python tools/count_claude_tokens.py --compare-tiktoken
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from ctok import token_count

CTOK_VERSION = "5.0"
CLAUDE5_VERSION = "5.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = REPO_ROOT / "claude-rules"

CLAUDE_RULE_SETS: tuple[tuple[str, str, str], ...] = (
    ("claude-rules/", "claude-rules", "gitlab/claude-rules"),
    ("claude-rules-economy/", "claude-rules-economy", "gitlab/claude-rules-economy"),
)
SHARED_ARTIFACTS: tuple[tuple[str, str], ...] = (
    (
        "rules/clear-precise-communication.md",
        "rules/clear-precise-communication.md",
    ),
    (
        "write-commit-messages",
        "skills/write-commit-messages/SKILL.md",
    ),
)


def read_on_disk(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def count_tokens(text: str, version: str = CTOK_VERSION) -> int:
    return token_count(text, version)


def count_opus5(text: str) -> int:
    return count_tokens(text, CTOK_VERSION)


def count_claude5(text: str) -> int:
    return count_tokens(text, CLAUDE5_VERSION)


def format_memory_display(tokens: int) -> str:
    """Match Claude Code /memory rounding: exact below 1000, else 0.1k."""
    if tokens < 1000:
        return str(tokens)
    tenths = round(tokens / 1000, 1)
    if tenths == int(tenths):
        return f"{int(tenths)}k"
    return f"{tenths}k"


def markdown_files(path: Path) -> list[Path]:
    if path.is_dir():
        files = sorted(path.glob("*.md"))
        if not files:
            raise SystemExit(f"No markdown files in {path}")
        return files
    if path.is_file():
        return [path]
    raise SystemExit(f"Not a file or directory: {path}")


def count_path(path: Path, version: str = CTOK_VERSION) -> int:
    return sum(count_tokens(read_on_disk(file), version) for file in markdown_files(path))


def collect_paths(requested: Sequence[str]) -> list[Path]:
    if not requested:
        return markdown_files(DEFAULT_DIR)

    collected: list[Path] = []
    for raw in requested:
        collected.extend(markdown_files(Path(raw)))
    if not collected:
        raise SystemExit("No files to count")
    return collected


def tiktoken_counts(text: str) -> tuple[int, int]:
    import tiktoken

    cl100k = tiktoken.get_encoding("cl100k_base")
    o200k = tiktoken.get_encoding("o200k_base")
    return len(cl100k.encode(text)), len(o200k.encode(text))


def count_codex_path(path: Path) -> int:
    return sum(tiktoken_counts(read_on_disk(file))[1] for file in markdown_files(path))


def claude_table_rows(repo_root: Path) -> list[tuple[str, int, int]]:
    rows: list[tuple[str, int, int]] = []
    for label, github_rel, gitlab_rel in CLAUDE_RULE_SETS:
        github = count_path(repo_root / github_rel, CTOK_VERSION)
        gitlab = count_path(repo_root / gitlab_rel, CTOK_VERSION)
        rows.append((label, github, gitlab))
    return rows


def shared_table_rows(repo_root: Path) -> list[tuple[str, int, int]]:
    rows: list[tuple[str, int, int]] = []
    for label, rel in SHARED_ARTIFACTS:
        path = repo_root / rel
        rows.append((label, count_path(path, CLAUDE5_VERSION), count_codex_path(path)))
    return rows


def render_claude_table(rows: Sequence[tuple[str, int, int]]) -> str:
    lines = [
        "| Artifact | GitHub | GitLab |",
        "| --- | ---: | ---: |",
    ]
    for label, github, gitlab in rows:
        lines.append(
            f"| `{label}` | {format_memory_display(github)} | "
            f"{format_memory_display(gitlab)} |"
        )
    return "\n".join(lines)


def render_shared_table(rows: Sequence[tuple[str, int, int]]) -> str:
    lines = [
        "| Artifact | Claude 5 | Codex |",
        "| --- | ---: | ---: |",
    ]
    for label, claude5, codex in rows:
        lines.append(
            f"| `{label}` | {format_memory_display(claude5)} | "
            f"{format_memory_display(codex)} |"
        )
    return "\n".join(lines)


def render_install_tables(repo_root: Path) -> str:
    return "\n\n".join(
        [
            render_claude_table(claude_table_rows(repo_root)),
            render_shared_table(shared_table_rows(repo_root)),
        ]
    )


def print_file_table(paths: Sequence[Path], compare_tiktoken: bool) -> None:
    rows: list[tuple[str, int, int, int]] = []
    for path in paths:
        text = read_on_disk(path)
        claude = count_opus5(text)
        cl100k = o200k = 0
        if compare_tiktoken:
            cl100k, o200k = tiktoken_counts(text)
        rows.append((path.name, claude, cl100k, o200k))

    name_width = max(len(name) for name, *_ in rows)
    name_width = max(name_width, 4)
    if compare_tiktoken:
        header = (
            f"{'file':<{name_width}}  {'opus5':>6}  {'display':>7}  "
            f"{'cl100k':>6}  {'o200k':>6}"
        )
    else:
        header = f"{'file':<{name_width}}  {'opus5':>6}  {'display':>7}"
    print(header)
    print("-" * len(header))

    total = 0
    for name, claude, cl100k, o200k in rows:
        total += claude
        display = format_memory_display(claude)
        if compare_tiktoken:
            print(
                f"{name:<{name_width}}  {claude:6d}  {display:>7}  "
                f"{cl100k:6d}  {o200k:6d}"
            )
        else:
            print(f"{name:<{name_width}}  {claude:6d}  {display:>7}")

    print("-" * len(header))
    print(
        f"{'total':<{name_width}}  {total:6d}  {format_memory_display(total):>7}"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Estimate Claude tokens for markdown files (ctok 5.0)."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories (default: claude-rules/*.md)",
    )
    parser.add_argument(
        "--table",
        action="store_true",
        help="Print the Claude GitHub/GitLab table and the shared-agent table",
    )
    parser.add_argument(
        "--compare-tiktoken",
        action="store_true",
        help="Also print cl100k_base and o200k_base counts",
    )
    args = parser.parse_args(argv)

    if args.table:
        print(render_install_tables(REPO_ROOT))
    else:
        print_file_table(collect_paths(args.paths), args.compare_tiktoken)

    print(
        f"ctok family {CTOK_VERSION} (Opus 5 / Claude 5). Unofficial reconstruction.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
