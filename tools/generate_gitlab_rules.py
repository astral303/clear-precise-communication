"""Generate GitLab-oriented copies of the Claude rule sets.

Rewrites pull-request wording to merge-request wording and GitHub host
names to GitLab. Source trees are not modified. Output under gitlab/ is
always rebuilt; files that do not match a source file are deleted.

Usage, from the repository root:

    uv run python tools/generate_gitlab_rules.py
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR_NAMES = ("claude-rules", "claude-rules-economy")
OUTPUT_DIRNAME = "gitlab"

# Longer phrases first. Workflow rewrites must run before generic PR → MR.
PHRASE_REPLACEMENTS: tuple[tuple[str, str], ...] = (
    (
        "GitHub already links stacked PRs",
        "GitLab already links related merge requests",
    ),
    (
        "If the PR is not against the repository's default branch",
        "If the MR does not target the repository's default branch",
    ),
    (
        "If the PR is not against the default branch",
        "If the MR does not target the default branch",
    ),
    (
        "name the base, and say that it must merge before this PR or",
        "name the target branch, and say whether another MR must merge first or",
    ),
    (
        "name the base, and that it must merge first",
        "name the target, and that another MR must merge first",
    ),
    ("Do not bury the base", "Do not bury the target"),
    ("the stacking plan", "a local series plan"),
    ("stacked PRs", "related merge requests"),
    ("Non-default PR base", "Non-default target branch"),
    ("non-default PR base", "non-default target branch"),
    (
        "announced in chat, not in the body",
        "announced in chat, not in the description",
    ),
    (
        "pull request titles and bodies",
        "merge request titles and descriptions",
    ),
    (
        "Pull request titles and bodies",
        "Merge request titles and descriptions",
    ),
    ("pull request bodies", "merge request descriptions"),
    ("Pull request bodies", "Merge request descriptions"),
    ("PR titles and bodies", "MR titles and descriptions"),
    ("PR title and body", "MR title and description"),
    ("PR-body", "MR-description"),
    ("PR bodies", "MR descriptions"),
    ("PR body", "MR description"),
    ("PR descriptions", "MR descriptions"),
    ("PR description", "MR description"),
    ("pull requests", "merge requests"),
    ("Pull request", "Merge request"),
    ("pull request", "merge request"),
    ("## Body order", "## Description order"),
    ("Body order:", "Description order:"),
    ("The body opens", "The description opens"),
    ("the body opens", "the description opens"),
)

# Allow a glossary phrase to break across a wrap, but not a paragraph.
_WHITESPACE_GAP = r"(?:[ \t]+|[ \t]*\n[ \t]*)"


def _phrase_pattern(old: str) -> re.Pattern[str]:
    parts = old.split()
    if not parts:
        raise ValueError(f"empty phrase: {old!r}")
    return re.compile(_WHITESPACE_GAP.join(re.escape(part) for part in parts))


COMPILED_PHRASES = tuple(
    (_phrase_pattern(old), new) for old, new in PHRASE_REPLACEMENTS
)
PR_MARKDOWN_FILE = re.compile(r"\bpr-(?P<rest>[\w.-]+\.md)")
GITHUB_WORD = re.compile(r"\bGitHub\b")
PRS_WORD = re.compile(r"\bPRs\b")
PR_WORD = re.compile(r"\bPR\b")
MR_BODY_HYPHEN = re.compile(r"\bMR-body\b")
MR_BODIES = re.compile(r"\bMR" + _WHITESPACE_GAP + r"bodies\b")
MR_BODY = re.compile(r"\bMR" + _WHITESPACE_GAP + r"body\b")
ARTICLE_BEFORE_MR = (
    (re.compile(r"\ba MR\b"), "an MR"),
    (re.compile(r"\bA MR\b"), "An MR"),
    (re.compile(r'\ba "MR\b'), 'an "MR'),
    (re.compile(r'\bA "MR\b'), 'An "MR'),
)

GITLAB_README = """\
# GitLab-oriented Claude rules

Generated copies of `claude-rules/` and `claude-rules-economy/` with
merge-request wording. Do not edit files in this directory. Change the
source trees and run:

    uv run python tools/generate_gitlab_rules.py

The script deletes files under `gitlab/` that no longer match a source
file, including leftover `pr-*.md` names after a rename.

Install with `./install/install.sh --gitlab` from the repository root.

Lines may run past 80 columns. The generator does not reflow; wrap does
not change what the model reads.
"""


def gitlab_filename(source_name: str) -> str:
    if source_name.startswith("pr-"):
        return "mr-" + source_name.removeprefix("pr-")
    return source_name


def rewrite_prose(text: str) -> str:
    for pattern, new in COMPILED_PHRASES:
        text = pattern.sub(new, text)
    text = PR_MARKDOWN_FILE.sub(lambda match: f"mr-{match.group('rest')}", text)
    text = GITHUB_WORD.sub("GitLab", text)
    text = PRS_WORD.sub("MRs", text)
    text = PR_WORD.sub("MR", text)
    text = MR_BODY_HYPHEN.sub("MR-description", text)
    text = MR_BODIES.sub("MR descriptions", text)
    text = MR_BODY.sub("MR description", text)
    for pattern, replacement in ARTICLE_BEFORE_MR:
        text = pattern.sub(replacement, text)
    return text


def planned_outputs(repo_root: Path) -> dict[Path, str]:
    output_root = repo_root / OUTPUT_DIRNAME
    planned = {output_root / "README.md": GITLAB_README}
    for dir_name in SOURCE_DIR_NAMES:
        source_dir = repo_root / dir_name
        if not source_dir.is_dir():
            raise SystemExit(f"Missing source directory: {source_dir}")
        sources = sorted(source_dir.glob("*.md"))
        if not sources:
            raise SystemExit(f"No markdown files in {source_dir}")
        dest_dir = output_root / dir_name
        for source_path in sources:
            dest_path = dest_dir / gitlab_filename(source_path.name)
            planned[dest_path] = rewrite_prose(
                source_path.read_text(encoding="utf-8")
            )
    return planned


def remove_unplanned_files(output_root: Path, planned: set[Path]) -> None:
    if not output_root.exists():
        return
    planned_resolved = {path.resolve() for path in planned}
    for path in sorted(output_root.rglob("*"), reverse=True):
        if path.is_file() and path.resolve() not in planned_resolved:
            path.unlink()
        elif (
            path.is_dir()
            and path.resolve() != output_root.resolve()
            and not any(path.iterdir())
        ):
            path.rmdir()


def generate_gitlab_tree(repo_root: Path) -> list[Path]:
    planned = planned_outputs(repo_root)
    for dest_path, content in planned.items():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(content, encoding="utf-8", newline="\n")
    output_root = repo_root / OUTPUT_DIRNAME
    remove_unplanned_files(output_root, set(planned))
    return sorted(planned)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate GitLab-oriented copies of the Claude rule sets."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root (default: the repo that contains this script)",
    )
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    written = generate_gitlab_tree(repo_root)
    print(f"Wrote {len(written)} files under {repo_root / OUTPUT_DIRNAME}")
    for path in written:
        print(path.relative_to(repo_root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
