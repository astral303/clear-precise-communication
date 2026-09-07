---
name: write-commit-messages
description: Write, revise, and review Git commit subjects and bodies as concise engineer-to-engineer explanations of the change and its rationale. Use whenever Codex drafts, amends, squashes, evaluates, or improves a commit message, including messages for bug fixes, refactors, tests, migrations, and configuration changes.
---

# Write Commit Messages

Make the change, motivation, design choice, and relevant test coverage understandable in one scan.
Lead with what changed, then explain why the change and its implementation were necessary.

## Build the message from evidence

1. Inspect the diff, tests, issue context, and repository conventions. Do not infer the change from
   filenames or the existing subject alone.
2. Identify the primary behavior or invariant that changed. Use it as the lede.
3. Identify the defect, constraint, or tradeoff that required the change.
4. Explain only the implementation decisions a future engineer would not recover quickly from the
   diff.
5. Describe durable test coverage added or materially updated by the commit and name the behavior
   it protects. Omit incidental commands, pass counts, unrelated failures, and general CI state;
   keep that execution evidence in the pull request, review notes, or plan.

## Write the subject

- Use an imperative, outcome-oriented subject with no trailing period.
- Name the affected behavior, not merely the files, symbols, or mechanical edits.
- Keep it specific enough to distinguish the commit in a log.
- Follow the repository's subject-length and prefix conventions. Otherwise, prefer 72 characters or
  fewer and omit Conventional Commit prefixes.

## Write the body

- Open with the changed behavior or result. Do not repeat the subject word for word.
- Follow with the concrete failure, constraint, or risk that made the change necessary.
- Use two to five bullets when the implementation, rationale, and added test coverage are parallel
  facts.
- Start each bullet with the action or invariant, then connect it to its reason or consequence.
- Explain non-obvious types, state, ordering, or algorithms by naming the ambiguity or invariant they
  resolve.
- Keep paragraphs short and follow repository wrapping conventions; otherwise, wrap around 72 to 80
  characters.
- Let prose order communicate purpose. Do not add `What:`, `Why:`, or similarly ceremonial labels.

A small commit may need only the subject. A nontrivial change normally needs one short opening
paragraph plus a few bullets. Prefer natural prose over forcing every message into the same shape.

## Use engineer-to-engineer prose

- Write directly and concretely. Prefer "Preserve ordinary lines byte-for-byte" over "This commit
  makes improvements to line handling."
- Describe behavior and causality rather than listing touched files or functions.
- Use domain terms and symbol names when they make the design easier to verify.
- Separate independent facts instead of joining them into a wall of text.
- Avoid sales language, self-congratulation, narration of the coding process, and speculation.
- Do not claim broader compatibility, performance, or safety than the diff and validation support.

## Examples

### Explain a non-obvious representation

```text
Keep cursor ownership when coalescing soft-wrap spaces

Exact-width separator rows now merge into the following text without losing
cursor positions at the wrap boundary.

- Introduce `WrappedLine` because a source range alone cannot represent both
  the bytes rendered on a row and the earliest cursor position owned by that
  row after the separator is removed.
- Route rendering, navigation, and height calculation through the same wrapped
  line model so editing behavior cannot diverge from layout.
- Cover cursor placement, rendered rows, and delete/reinsert behavior at the
  exact-width boundary.
```

### Explain a narrow parser correction

```text
Preserve Markdown hard breaks during stream finalization

Ordinary assistant lines now retain trailing spaces through finalization, so
completed content no longer differs from the streamed source.

- Return no rewritten line when directive stripping changes nothing, keeping
  whitespace cleanup confined to content the parser actually modifies.
- Treat whitespace-only tail lines as empty without trimming visible lines.
- Cover parser preservation and the no-reflow completion path.
```

## Reject these failure modes

- A subject-only message for a change with non-obvious behavior or tradeoffs.
- A body that inventories files, symbols, or edits without explaining impact.
- A long paragraph containing change, cause, design, tests, and caveats at once.
- Explicit `What` and `Why` sections that make natural causal prose feel templated.
- A rationale that appears before the reader knows what changed.
- A validation bullet that inventories commands, pass counts, unrelated failures, or CI state
  instead of test coverage added or updated by the commit.
- Test-coverage claims that are not supported by tests added or updated in the diff.

## Final check

Read only the subject, opening sentence, and bullet starts. They should reveal the outcome, the
reason, and the important design choices without requiring the full diff. Remove any sentence that
merely repeats another one.
