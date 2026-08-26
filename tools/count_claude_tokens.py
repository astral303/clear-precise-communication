"""Estimate Claude Opus 5 token counts for files.

Uses ctok's v5 family (Opus 5 and Sonnet 5). That reconstruction is unofficial
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
    uv run python tools/count_claude_tokens.py --compare-tiktoken
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from ctok import token_count

CTOK_VERSION = "5.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = REPO_ROOT / "claude-rules"


def read_on_disk(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def count_opus5(text: str) -> int:
    return token_count(text, CTOK_VERSION)


def format_memory_display(tokens: int) -> str:
    """Match Claude Code /memory rounding: exact below 1000, else 0.1k."""
    if tokens < 1000:
        return str(tokens)
    tenths = round(tokens / 1000, 1)
    if tenths == int(tenths):
        return f"{int(tenths)}k"
    return f"{tenths}k"


def collect_paths(requested: Sequence[str]) -> list[Path]:
    if not requested:
        paths = sorted(DEFAULT_DIR.glob("*.md"))
        if not paths:
            raise SystemExit(f"No markdown files in {DEFAULT_DIR}")
        return paths

    collected: list[Path] = []
    for raw in requested:
        path = Path(raw)
        if path.is_dir():
            collected.extend(sorted(path.glob("*.md")))
        elif path.is_file():
            collected.append(path)
        else:
            raise SystemExit(f"Not a file or directory: {path}")
    if not collected:
        raise SystemExit("No files to count")
    return collected


def tiktoken_counts(text: str) -> tuple[int, int]:
    import tiktoken

    cl100k = tiktoken.get_encoding("cl100k_base")
    o200k = tiktoken.get_encoding("o200k_base")
    return len(cl100k.encode(text)), len(o200k.encode(text))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Estimate Claude Opus 5 tokens for markdown files (ctok v5)."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories (default: claude-rules/*.md)",
    )
    parser.add_argument(
        "--compare-tiktoken",
        action="store_true",
        help="Also print cl100k_base and o200k_base counts",
    )
    args = parser.parse_args(argv)

    paths = collect_paths(args.paths)
    rows: list[tuple[str, int, int, int]] = []
    for path in paths:
        text = read_on_disk(path)
        claude = count_opus5(text)
        cl100k = o200k = 0
        if args.compare_tiktoken:
            cl100k, o200k = tiktoken_counts(text)
        rows.append((path.name, claude, cl100k, o200k))

    name_width = max(len(name) for name, *_ in rows)
    name_width = max(name_width, 4)
    if args.compare_tiktoken:
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
        if args.compare_tiktoken:
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
    print(
        f"ctok family {CTOK_VERSION} (Opus 5 / Sonnet 5). Unofficial reconstruction.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
