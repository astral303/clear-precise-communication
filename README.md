# Clear, Precise Communication

Standing writing rules for coding agents. Not a skill.

They shape ordinary replies and durable writing—documentation, plans, ADRs,
changelogs, release and commit text, pull requests, issues, runbooks, reports,
code comments, and user-facing copy—for readers with ADHD, interrupted
attention, or little time.

> **Prefer conversation-first guidance?** This remix generalizes the original
> approach for durable writing and removes some strict rules designed for
> turn-by-turn replies. For the strongest focus on action-first conversational
> guidance, use Ayoub Ghriss's excellent [i-have-adhd skill](https://github.com/ayghri/i-have-adhd).

## Two install paths

A skill is the wrong delivery mechanism for both agents this repo targets.

- **Codex** obeys skill frontmatter. A description that says to use the skill
  for every conversation loads the full text on every turn. Standing text
  belongs in `~/.codex/AGENTS.md` plus `~/.codex/AGENTS.d/`, not in a skill.
  (`~/.codex/rules` is permission policy, not writing guidance.)
- **Claude Code** often does not invoke skills. Standing text belongs in
  `~/.claude/rules/`, which loads at session start.

Claude also needs more than the one-file rule: it treats comments, drafts, and
test names as exempt, and it skips structure until a later pass.
[`claude-rules/`](./claude-rules/) closes those holes. Codex follows
[`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md);
extra copies would cost tokens every turn.

See [INSTALL.md](./INSTALL.md) for verification, updates, and uninstallation.

### Codex and other agents that obey global instructions

Copy or symlink [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md)
into the agent's global standing-instructions directory, then add a session-start
pointer so the file is read once.

Codex (`~/.codex/AGENTS.d/` plus a stanza in `~/.codex/AGENTS.md`):

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

Add this stanza to `~/.codex/AGENTS.md` if it is not already there:

```markdown
## Mandatory ambient communication and writing guidance

At the beginning of each session, read `~/.codex/AGENTS.d/clear-precise-communication.md` completely and apply it throughout the session.

Do not reread it during the same session, unless immediately after a compaction.
```

Do not install this repo as a Codex plugin or skill.

### Claude Code

Copy or junction [`claude-rules/`](./claude-rules/) into `~/.claude/rules/` so
the files load at session start with no invocation. They have no `paths:`
frontmatter: a PR body drafted in chat still matches.

From the repository root:

```powershell
$repo = (Get-Location).Path
$rules = Join-Path $env:USERPROFILE ".claude\rules"
New-Item -ItemType Directory -Force -Path $rules | Out-Null
$link = Join-Path $rules "clear-precise-writing"
if (Test-Path $link) { Remove-Item $link }
New-Item -ItemType Junction -Path $link -Target (Join-Path $repo "claude-rules")
```

```bash
mkdir -p ~/.claude/rules
ln -sfn /path/to/clear-precise-communication/claude-rules ~/.claude/rules/clear-precise-writing
```

Start a new Claude Code session. In `/context`, the files should appear under
Memory files.

If you already have a short `~/.claude/rules/documentation-tone.md`, remove it.
`claude-rules/documentation-tone.md` replaces it.

## What changes

The rules put the primary value first, expose state and next actions when they
matter, and remove details that slow the reader without helping them act.

### Before

> We made several updates to the authentication flow, including changes to magic-link handling and its related tests. Most of the work is complete, although there are still a few items that need attention before release. The staging checks passed, but production rollout is waiting on an environment variable from the platform team.

### After

> Magic-link authentication now passes in staging. Production rollout is blocked on one environment variable from the platform team.
>
> - Complete: implementation and automated tests
> - Verified: staging login flow
> - Next owner: platform team

## Core rules

1. Lead with the primary value.
2. Design for scanning.
3. Make starting easy and steps bounded.
4. Externalize current state, dependencies, and next actions.
5. Suppress tangents.
6. Give concrete time estimates when time matters.
7. Make progress and outcomes visible.
8. Describe errors matter-of-factly.
9. Keep lists focused and prioritized.
10. Remove preambles, repeated recaps, and generic closers.

Read the complete one-file rule in [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).

[`claude-rules/`](./claude-rules/) adds constraints that file did not enforce:

- Noun-phrase labels, not question headings or `What`/`Where`/`Why` comment openers
- Write from the reader's next action, not as a narration of the diff
- Scannable PR structure: tables for grids, one-fact bullets
- Title and opening name the user-visible effect
- Literal verbs, not idioms (`deleted`, not `go with it`)
- Changelog: change class, verb + symptom, ratios a reader can reuse
- Describe work to a reviewer; do not advocate for it
- Comments only for what code cannot say; structure or a test first

Each Claude file restates that comments, drafts, and test names are in scope.
`final-scan.md` is the post-write search.

## Customize

Edit [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).
Copy the body into `claude-rules/clear-precise-communication.md`, keeping the
always-on preamble on the Claude copy. Re-copy into `~/.codex/AGENTS.d/` if
that file is not a symlink. Start a new session so the revised text enters
fresh context.

## Attribution

This repository is a remix of Ayoub Ghriss's excellent
[i-have-adhd skill](https://github.com/ayghri/i-have-adhd), which established
the original ADHD-friendly approach to action-oriented AI responses. The
original copyright notice remains in [LICENSE](./LICENSE).

The upstream project drew from *The Adult ADHD Tool Kit* by J. Russell Ramsay
and Anthony L. Rostain, adapting its ideas for AI-generated communication.

## License

[MIT](./LICENSE)
