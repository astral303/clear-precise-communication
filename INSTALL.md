# Install Clear, Precise Communication

Install the plugin for Codex or Claude Code, then verify that `clear-precise-communication` appears in the relevant plugin list.

## Codex

### Install

```bash
codex plugin marketplace add astral303/clear-precise-communication --ref main
codex plugin add clear-precise-communication@clear-precise-communication
```

Invoke the skill explicitly with `$clear-precise-communication`. The skill can also activate implicitly for relevant writing tasks.

### Verify

```bash
codex plugin list
```

The list should include `clear-precise-communication` from the `clear-precise-communication` marketplace.

### Update

```bash
codex plugin marketplace upgrade clear-precise-communication
codex plugin remove clear-precise-communication
codex plugin add clear-precise-communication@clear-precise-communication
```

Start a new thread after reinstalling so Codex loads the updated skill.

### Uninstall

```bash
codex plugin remove clear-precise-communication
codex plugin marketplace remove clear-precise-communication
```

## Claude Code

### Install

```bash
git clone https://github.com/astral303/clear-precise-communication.git ./clear-precise-communication
claude plugin marketplace add ./clear-precise-communication
claude plugin install clear-precise-communication@clear-precise-communication
```

Invoke the skill with `/clear-precise-communication`.

### Verify

```bash
claude plugin list
```

The list should show `clear-precise-communication` as enabled.

### Update

```bash
cd ./clear-precise-communication
git pull
```

The marketplace reads the local checkout. Start a new Claude Code session after updating.

### Uninstall

```bash
claude plugin uninstall clear-precise-communication
claude plugin marketplace remove clear-precise-communication
```

## Troubleshooting

### The skill is missing from autocomplete

Restart Codex or Claude Code. Plugin and skill indexes are loaded at startup.

### Claude Code cannot add the marketplace

Point the command at the repository root containing `.claude-plugin/marketplace.json`, not at `.claude-plugin/` itself.

### Updated rules do not appear

Start a new thread or session. Existing context can retain the previous skill instructions.

### The writing still feels too dense

Edit `skills/clear-precise-communication/SKILL.md`, tighten the relevant rule, and invoke the skill again in fresh context.
