# Clear, Precise Communication

Standing writing rules for coding agents. Commit messages are a separate
skill.

They shape ordinary replies and durable writing—documentation, plans, ADRs,
changelogs, release and commit text, pull requests, issues, runbooks, reports,
code comments, and user-facing copy—for readers with ADHD, interrupted
attention, or little time.

> **Prefer conversation-first guidance?** This remix generalizes the original
> approach for durable writing and removes some strict rules designed for
> turn-by-turn replies. For the strongest focus on action-first conversational
> guidance, use Ayoub Ghriss's excellent [i-have-adhd skill](https://github.com/ayghri/i-have-adhd).

## What it does

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

The one-file rule is
[`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).
Claude Code loads extra files under [`claude-rules/`](./claude-rules/) so
comments, drafts, test names, and PR text drafted in chat stay in scope.

## Install

```bash
./install/install.sh
```

```powershell
./install/install.ps1
```

A bare run writes nothing until you approve. In a terminal it shows a checkbox
of detected agents (up/down, Space, Enter), then unified diffs, then
`Apply? [y/N]`. `-h` prints flags. `--dry-run` stops after the diffs.
`--doctor` checks an existing install. `--yes` skips the prompts.

The installer looks for `~/.codex`, `~/.claude`, and `~/.grok`.

Always-on writing is a standing file, not a plugin. Codex would reload a
plugin on every turn; Claude often would not invoke it; many orgs only allow
blessed plugins. This install works in those cases. The commit-message skill
stays a skill: it loads when you are writing a commit, not every turn.

To undo: delete the symlink or copy and the `AGENTS.md` stanza. `--doctor`
reports what is missing.

## What gets installed

| Agent | Always-on | Skill |
| --- | --- | --- |
| Codex, Grok | `AGENTS.d/` plus an `AGENTS.md` pointer | `~/.<agent>/skills/write-commit-messages` |
| Claude Code | `~/.claude/rules/clear-precise-writing` → `claude-rules/` | `~/.claude/skills/write-commit-messages` |

Codex and Grok also get
[`rules/clean-code-principles.md`](./rules/clean-code-principles.md) unless
you pass `--no-clean-code`. Claude's extra files live in
[`claude-rules/`](./claude-rules/). Use `--claude-set economy` for
[`claude-rules-economy/`](./claude-rules-economy/) when the context budget is
tight. Use `--gitlab` for merge-request wording under [`gitlab/`](./gitlab/).

| Artifact | GitHub | GitLab |
| --- | ---: | ---: |
| `claude-rules/` | 25.6k | 25.6k |
| `claude-rules-economy/` | 10.5k | 10.5k |

GitHub is pull-request wording; GitLab is merge-request wording. Counts are
ctok 5.0 (Claude 5).

| Artifact | Claude 5 | Codex |
| --- | ---: | ---: |
| `rules/clear-precise-communication.md` | 2.2k | 1.4k |
| `write-commit-messages` | 2.3k | 1.5k |

Codex counts are tiktoken o200k_base. Do not use them as a Claude estimate.
Rebuild both tables with `uv run python tools/count_claude_tokens.py --table`.

[`claude-rules/clear-precise-communication.md`](./claude-rules/clear-precise-communication.md)
is the one-file body plus a Claude always-on preamble. The economy ten-rule
file is a shortened rewrite, not a copy.

## Commit messages

PR titles still lead with the user-visible bug. Commit subjects follow
[`skills/write-commit-messages/SKILL.md`](./skills/write-commit-messages/SKILL.md):
the changed behavior or invariant first, then the defect, constraint, or
tradeoff that required it.

- Codex: `$write-commit-messages` (also implicit on commit work)
- Claude: `/write-commit-messages`

## Customize

Edit [`rules/clear-precise-communication.md`](./rules/clear-precise-communication.md).
If the install is a symlink, `git pull` is enough. If it is a copy, copy the
body into `claude-rules/clear-precise-communication.md` and keep the
always-on preamble. Start a new session so the revised text enters context.

## Attribution

This repository is a remix of Ayoub Ghriss's excellent
[i-have-adhd skill](https://github.com/ayghri/i-have-adhd), which established
the original ADHD-friendly approach to action-oriented AI responses. The
original copyright notice remains in [LICENSE](./LICENSE).

The upstream project drew from *The Adult ADHD Tool Kit* by J. Russell Ramsay
and Anthony L. Rostain, adapting its ideas for AI-generated communication.

## License

[MIT](./LICENSE)
