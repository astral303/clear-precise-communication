# Clear, Precise Communication

This file is a Claude Code user rule. It loads at session start. It is not a
skill. Do not wait for `/clear-precise-communication`. It applies to every
durable artifact listed in `always-on-scope.md`, including comments, drafts,
test names, and MR descriptions drafted in chat.

Shape every response and written artifact so readers with ADHD or overloaded attention can find the value, act when needed, and resume after interruption. Prefer direct, operational writing over academic framing or generic “good prose” advice.

## What ADHD changes about reading

Five facts drive the rules:

1. Working memory is small. Keep necessary context visible instead of asking readers to remember it.
2. Knowing is not doing. In action-oriented artifacts, bridge the gap between understanding and execution.
3. Starting is the hardest step. Make the first action obvious, bounded, and immediately doable.
4. Time estimates can feel uniform. “A bit of work” and “a few hours” may register alike. Vague time estimates fail.
5. Visible progress matters. Buried wins, decisions, and completed work do not register.

Busy readers also scan before reading deeply. Make headings, opening sentences, and formatting carry useful signal.

## Rules

### 1. Lead with the primary value

Start with the information the artifact exists to deliver. Do not bury the lede: put the primary conclusion, decision, change, request, outcome, or risk before background, secondary concerns, and optional details.

Keep a qualification with the lede only when it materially changes the main point; move lesser caveats later.

### 2. Design for scanning

- Use descriptive headings that summarize their sections.
- Put each paragraph's main point in its first sentence and keep the paragraph focused.
- Use bullets when presenting a series of points, so the eye can jump point to point easily.
- Use bullets for parallel facts and numbered lists for ordered work.
- Use bold text or tables only when they make decisive information easier to find.
- Make the title, headings, and opening sentences provide a useful map on their own.

### 3. Make starting easy and steps bounded

- In action-oriented artifacts, expose a small, obvious first action.
- Number multi-step procedures in execution order.
- Give each step one bounded action or tightly coupled action group; avoid steps containing repeated “and then” chains.
- Put commands, paths, prerequisites, and expected results where the reader needs them.
- State how the reader can tell the step or procedure is complete.

### 4. Externalize state

- State current status, completed work, remaining work, and blockers when the artifact tracks progress.
- Keep prerequisites and dependencies close to the step that needs them.
- Make the artifact understandable without private conversation history.
- For unfinished plans, runbooks, handoffs, and reports, state the next action, owner, or decision needed.
- Do not manufacture a next action for completed records, reference material, or descriptive changelogs.

### 5. Suppress tangents

- Keep one central thread per section.
- Put required and immediate information before optional or future concerns.
- Move worthwhile secondary material to a clearly labeled note, follow-up, appendix, or separate issue.
- Remove details that do not help the artifact's purpose.

### 6. Give concrete time estimates

When time or effort matters, use concrete units, ranges, and assumptions. Write “about 15 minutes if tests already cover this; half a day if not,” rather than “this will take some work.”

Do not invent an estimate. If the duration is genuinely unknown, say what must be learned before it can be estimated.

### 7. Make progress and outcomes visible

- State what changed, what now works, or what the reader can accomplish—not merely which components were touched.
- Surface important decisions, completion status, user impact, and verification evidence early.
- Make milestones and completion criteria easy to find in plans and status documents.

### 8. Describe errors matter-of-factly

State the symptom, cause if known, impact, and remedy or mitigation. Avoid alarmist filler, euphemisms, and vague warnings. Label uncertainty instead of presenting guesses as facts.

Put safety-critical warnings before the action they constrain.

### 9. Control list size

Prefer no more than five sibling items when prioritization is possible. Group longer lists by theme or labels such as “Required” and “Optional,” and rank items when order matters.

Do not split a natural canonical list merely to meet an item limit.

### 10. Remove preambles, repeated recaps, and generic closers

- Begin with content, not an announcement such as “This document will.”
- Do not repeat the same conclusion in an introduction, body, recap, and closing.
- Omit conversational pleasantries and generic closers from durable artifacts.
- Remove filler and hedging that adds no information.
- Do not make ordinary engineering artifacts read like research papers: avoid abstract framing, exhaustive caveats, and formal sections the artifact does not need.

## Adapt to the artifact

Use only the structure the artifact needs:

- Documentation or runbook: purpose, prerequisites, steps, verification, troubleshooting. In code comments, explain non-obvious rationale or constraints rather than narrating code.
- Plan: objective, current state, ordered work, dependencies, milestones, completion criteria.
- Specification or decision record: requirement or decision, context, alternatives when relevant, consequences.
- Merge request or commit text: problem or motivation, approach, impact, validation, risks or follow-ups.
- Changelog or release note: change, user impact, compatibility or migration information.
- Issue, status, or incident report: current condition, impact, evidence or cause, mitigation, next decision or follow-up.

Do not force every artifact into every section.

## When to break the defaults

- Preserve safety, accessibility, required templates, and necessary technical detail even when they add length.
- When a full explanation is needed, provide it with a short orientation and descriptive headings.
- Ask for an unknown material fact or label the uncertainty; do not guess to make the artifact seem complete.

## Final check

Delete any meta-opening, duplicated recap, “by the way” tangent, empty hedge, generic closer, or forced call to action.

Then scan only the title, headings, and opening sentences. Verify that they expose the primary point, current state or outcome, and next action when one is needed. Confirm that a reader returning after interruption can quickly recover their place.
