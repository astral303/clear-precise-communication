# Install Clear, Precise Communication

This repo is standing writing rules, not a plugin and not a skill.

- **Codex and other agents that obey global instructions:** one file,
  [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).
- **Claude Code:** [`claude-rules/`](./claude-rules/) in `~/.claude/rules/`
  (19.9k Opus 5 tokens), or [`claude-rules-economy/`](./claude-rules-economy/)
  (8.9k) when the context budget is tight.

Do not add this repo as a Codex or Claude plugin. Skill frontmatter that says
to use the guidance on every conversation makes Codex reload the full text on
every turn. Claude often does not invoke the skill at all.

If you previously installed the plugin, remove it, then use the paths below.

```bash
codex plugin remove clear-precise-communication
codex plugin marketplace remove clear-precise-communication
claude plugin uninstall clear-precise-communication
claude plugin marketplace remove clear-precise-communication
```

## Codex and other obedient agents

### Install

Codex's standing-instructions file is `~/.codex/AGENTS.md`. It does not scan a
rules directory for writing guidance: `~/.codex/rules` is permission policy.

Symlink or copy the one-file rule next to `AGENTS.md`, then add a session-start
pointer. From the repository root:

```powershell
$repo = (Get-Location).Path
$link = Join-Path $env:USERPROFILE ".codex\clear-precise-communication.md"
if (Test-Path $link) { Remove-Item $link }
New-Item -ItemType SymbolicLink -Path $link -Target (Join-Path $repo "rules\clear-precise-communication.md")
```

```bash
ln -sfn "$(pwd)/rules/clear-precise-communication.md" ~/.codex/clear-precise-communication.md
```

If the host cannot create a file symlink, copy the file instead.

Add this stanza to `~/.codex/AGENTS.md` if it is not already there:

```markdown
## Mandatory ambient communication and writing guidance

At the beginning of each session, read `~/.codex/clear-precise-communication.md` completely and apply it throughout the session.

Do not reread it during the same session, unless immediately after a compaction.
```

There is no `~/.codex/AGENTS.d` in Codex. If you already keep several standing
files in a directory of your own and point `AGENTS.md` at them, put this file
there instead and use that path in the stanza.

For another agent, drop the same file into its global instructions directory
and add an equivalent session-start pointer.

### Verify

`~/.codex/clear-precise-communication.md` exists (symlink or copy), and
`~/.codex/AGENTS.md` names it. Start a new Codex thread. The writing guidance
should apply without `$clear-precise-communication` or any other invocation.

### Update

```bash
git pull
```

A symlink already tracks this checkout. Re-copy the file if you installed it
as a copy. Start a new thread.

### Uninstall

Delete `~/.codex/clear-precise-communication.md` and remove the stanza from
`~/.codex/AGENTS.md`.

## Claude Code

Claude Code loads every `*.md` file under `~/.claude/rules/` recursively at
session start, unless the file has `paths:` frontmatter. These files have none,
so they apply to chat-drafted MR descriptions, comments, and changelogs, not only to
matching paths.

Do not put a README in the linked directory: Claude would load it as a rule.

### Install

**Windows (junction; no admin required):**

From the repository root:

```powershell
$repo = (Get-Location).Path
$rules = Join-Path $env:USERPROFILE ".claude\rules"
New-Item -ItemType Directory -Force -Path $rules | Out-Null
$link = Join-Path $rules "clear-precise-writing"
if (Test-Path $link) { Remove-Item $link }
New-Item -ItemType Junction -Path $link -Target (Join-Path $repo "claude-rules")
```

**Unix (symlink):**

```bash
mkdir -p ~/.claude/rules
ln -sfn /path/to/clear-precise-communication/claude-rules ~/.claude/rules/clear-precise-writing
```

A junction or symlink tracks `git pull`. Copying the files also works; then
re-copy after updates.

If `~/.claude/rules/documentation-tone.md` already exists as a short file,
remove it so it does not compete with `claude-rules/documentation-tone.md`.

To install the shorter set instead, point the junction or symlink at
`claude-rules-economy/` (8.9k Opus 5 tokens instead of 19.9k). Same
constraints, less repetition. Use `claude-rules/` when the budget allows.

Count either directory with:

```bash
uv run python tools/count_claude_tokens.py claude-rules
uv run python tools/count_claude_tokens.py claude-rules-economy
```

Start a new Claude Code session after installing. Existing sessions keep the
previous instruction set.

### Verify

Run `/context` in a new session and check Memory files for
`clear-precise-writing/` (or the filenames under `claude-rules/`).

### Update

```bash
git pull
```

Start a new Claude Code session. A junction or symlink already points at
`claude-rules/` in this checkout.

### Uninstall

This does not delete the repository:

```powershell
Remove-Item (Join-Path $env:USERPROFILE ".claude\rules\clear-precise-writing")
```

```bash
rm ~/.claude/rules/clear-precise-writing
```

## Troubleshooting

### Codex reloads the writing rules on every turn

The repo is installed as a skill or plugin. Remove it (commands at the top of
this file) and use a sibling file plus an `AGENTS.md` stanza instead.

### Claude still writes inflated MR or comment text

Confirm the rules loaded with `/context`. Do not add `paths:` frontmatter: a
MR description that exists only in chat would not match a path glob. Start a new
session; a session started before the install will not have the files.

### Updated always-on rules do not appear

Start a new thread or session. Existing context can retain the previous
instructions. For Claude, the junction or symlink must point at `claude-rules/`
in this checkout.

### The writing still feels too dense

Edit `rules/clear-precise-communication.md`, copy the body into
`claude-rules/clear-precise-communication.md` (keep the always-on preamble),
re-copy to `~/.codex/` if that file is not a symlink, and start a new session.
