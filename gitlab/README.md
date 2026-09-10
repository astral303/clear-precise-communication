# GitLab-oriented Claude rules

Generated copies of `claude-rules/` and `claude-rules-economy/` with
merge-request wording. Do not edit files in this directory. Change the
source trees and run:

    uv run python tools/generate_gitlab_rules.py

The script deletes files under `gitlab/` that no longer match a source
file, including leftover `pr-*.md` names after a rename.

Install the same way as the pull-request trees: junction
`gitlab/claude-rules/` or `gitlab/claude-rules-economy/` into
`~/.claude/rules/`.

Lines may run past 80 columns. The generator does not reflow; wrap does
not change what the model reads.
