# Clear, Precise Communication

AI agent skill for clear, scannable, ADHD-friendly technical writing—without burying the point.

This plugin adds the `clear-precise-communication` skill for Codex and Claude Code. It shapes ordinary conversation and durable writing—documentation, plans, ADRs, changelogs, release and commit text, pull requests, issues, runbooks, reports, code comments, and user-facing copy—for readers with ADHD, interrupted attention, or little time.

> **Prefer conversation-first guidance?** This remix generalizes the original approach for durable writing and removes some strict rules designed for turn-by-turn replies. For the strongest focus on action-first conversational guidance, use Ayoub Ghriss's excellent [i-have-adhd skill](https://github.com/ayghri/i-have-adhd).

## Install

### Codex

```bash
codex plugin marketplace add astral303/clear-precise-communication --ref main
codex plugin add clear-precise-communication@clear-precise-communication
```

Use `$clear-precise-communication` to invoke the skill explicitly. Its metadata also allows implicit invocation whenever Codex identifies relevant writing.

### Claude Code

```bash
git clone https://github.com/astral303/clear-precise-communication.git ./clear-precise-communication
claude plugin marketplace add ./clear-precise-communication
claude plugin install clear-precise-communication@clear-precise-communication
```

Use `/clear-precise-communication` to invoke the skill.

See [INSTALL.md](./INSTALL.md) for verification, updates, uninstallation, and troubleshooting.

## What changes

The skill puts the primary value first, exposes state and next actions when they matter, and removes details that slow the reader without helping them act.

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

Read the complete guidance in [SKILL.md](./skills/clear-precise-communication/SKILL.md).

## Customize the skill

Edit `skills/clear-precise-communication/SKILL.md`, then start a new session or re-invoke the skill so the revised instructions enter fresh context.

## Attribution

This repository is a remix of Ayoub Ghriss's excellent [i-have-adhd skill](https://github.com/ayghri/i-have-adhd), which established the original ADHD-friendly approach to action-oriented AI responses. The upstream Codex plugin structure was contributed by Seongho Bae. The original copyright notice remains in [LICENSE](./LICENSE).

The upstream project drew from *The Adult ADHD Tool Kit* by J. Russell Ramsay and Anthony L. Rostain, adapting its ideas for AI-generated communication.

## License

[MIT](./LICENSE)
