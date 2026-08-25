# Install Clear, Precise Communication

This repo is standing writing rules, not a plugin and not a skill.

- **Codex and other agents that obey global instructions:** one file,
  [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).
- **Claude Code:** the [`claude-rules/`](./claude-rules/) directory in
  `~/.claude/rules/`.

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

Copy or symlink the one-file rule into the agent's global standing-instructions
directory, then add a session-start pointer.

From the repository root, for Codex:

```powershell
$repo = (Get-Location).Path
$dest = Join-Path $env:USERPROFILE ".codex\AGENTS.d"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item (Join-Path $repo "rules\clear-precise-communication.md") (Join-Path $dest "clear-precise-communication.md") -Force
```

```bash
mkdir -p ~/.codex/AGENTS.d
cp rules/clear-precise-communication.md ~/.codex/AGENTS.d/clear-precise-communication.md
```

Add this stanza to `~/.codex/AGENTS.md` if it is not already there. Codex
`~/.codex/rules` is permission policy and will not load this file.

```markdown
## Mandatory ambient communication and writing guidance

At the beginning of each session, read `~/.codex/AGENTS.d/clear-precise-communication.md` completely and apply it throughout the session.

Do not reread it during the same session, unless immediately after a compaction.
```

For another agent, drop the same file into its global instructions directory
and add an equivalent session-start pointer.

### Verify

The file `~/.codex/AGENTS.d/clear-precise-communication.md` exists, and
`~/.codex/AGENTS.md` names it. Start a new Codex thread. The writing guidance
should apply without `$clear-precise-communication` or any other invocation.

### Update

```bash
git pull
```

Re-copy `rules/clear-precise-communication.md` into `AGENTS.d` if that file is
not a symlink. Start a new thread.

### Uninstall

Delete `~/.codex/AGENTS.d/clear-precise-communication.md` and remove the stanza
from `~/.codex/AGENTS.md`.

## Claude Code

Claude Code loads every `*.md` file under `~/.claude/rules/` recursively at
session start, unless the file has `paths:` frontmatter. These files have none,
so they apply to chat-drafted PR bodies, comments, and changelogs, not only to
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
this file) and use `AGENTS.d` plus the `AGENTS.md` stanza instead.

### Claude still writes inflated PR or comment text

Confirm the rules loaded with `/context`. Do not add `paths:` frontmatter: a
PR body that exists only in chat would not match a path glob. Start a new
session; a session started before the install will not have the files.

### Updated always-on rules do not appear

Start a new thread or session. Existing context can retain the previous
instructions. For Claude, the junction or symlink must point at `claude-rules/`
in this checkout.

### The writing still feels too dense

Edit `rules/clear-precise-communication.md`, copy the body into
`claude-rules/clear-precise-communication.md` (keep the always-on preamble),
re-copy to `AGENTS.d` if needed, and start a new session.
