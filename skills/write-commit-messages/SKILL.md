---
name: write-commit-messages
description: Write, revise, and review Git commit subjects and bodies as concise engineer-to-engineer explanations of why the change was necessary, sized to the change and without restating the diff. Use whenever Codex drafts, amends, squashes, evaluates, or improves a commit message, including messages for bug fixes, refactors, tests, migrations, and configuration changes.
---

# Write Commit Messages

The message carries *why* and *what was wrong*. The diff carries *how*. Do not
re-explain what the diff shows.

Length tracks the change, not the effort. A 4-line fix gets about 4 lines. If
the message rivals the size of the feature, cut. A small commit may need only
the subject.

Lead with the behavior or invariant that changed, then the defect, constraint,
or tradeoff that required it. A future engineer reading the log should see
what moved and why. They open the diff for how. The message is not a
stand-alone substitute for the patch.

## Build the message from evidence

1. Inspect the diff, tests, issue context, and repository conventions. Do not
   infer the change from filenames or the existing subject alone.
2. Identify the primary behavior or invariant that changed. Use it as the lede.
3. Identify the defect, constraint, or tradeoff that required the change.
4. Keep only what the diff cannot say: why this representation, which invariant
   forbids the obvious alternative. Mechanics visible in the diff (which type
   became explicit, which token changed, which import moved) carry no
   archaeological value. Delete any clause that describes a diff-visible
   mechanic with no why.
5. Name test coverage this commit added or materially changed, and the
   behavior it protects. Do not record that existing tests still pass, that
   untouched callers still compile, or that unchanged behavior still works.
   Those claims are correctness theater. Keep pass counts, command logs, and
   CI state out of the message; they belong in the pull/merge request, review
   notes, or plan if anywhere.

## Write the subject

- Use an imperative, outcome-oriented subject with no trailing period.
- Name the affected behavior, not merely the files, symbols, or mechanical edits.
- Keep it specific enough to distinguish the commit in a log.
- Follow the repository's subject-length and prefix conventions. Otherwise,
  prefer 72 characters or fewer and omit Conventional Commit prefixes.

## Write the body

- Open with the changed behavior or result. Do not repeat the subject word for
  word.
- Follow with the concrete failure, constraint, or risk that made the change
  necessary.
- State each point once. A consequence you already implied is not a new point.
  "Fixed overshoot in X" already means "X now honors its contract" — do not
  write both.
- Use bullets when implementation, rationale, and added tests are parallel
  facts. That is not a quota. Do not invent bullets to fill two-to-five.
- Start each bullet with the invariant or reason, then the consequence. Do not
  start with a mechanic the diff already shows.
- Keep paragraphs short and follow repository wrapping conventions; otherwise
  wrap around 72 to 80 characters.
- Let prose order communicate purpose. Do not add `What:`, `Why:`, or similarly
  ceremonial labels.

Prefer natural prose over forcing every message into the same shape.

## Use engineer-to-engineer prose

- Write directly and concretely. Prefer "Preserve ordinary lines byte-for-byte"
  over "This commit makes improvements to line handling."
- Describe behavior and causality rather than listing touched files or functions.
- Use the code's own noun. Do not swap in a synonym mid-message (`limit` stays
  `limit`, not `cap` then `capped`).
- Separate independent facts instead of joining them into a wall of text.
- Avoid sales language, self-congratulation, narration of the coding process,
  and speculation.
- Do not claim broader compatibility, performance, or safety than the diff and
  validation support.
- Do not record what is still true of the rest of the tree.

## Examples

### A small change stays small

```text
Share the path join used by load and save

Load and save inlined the same join. Sharing it removes the opportunity for
divergence.
```

### Explain a non-obvious representation

```text
Keep cursor ownership across coalesced soft-wrap spaces

Exact-width separator rows merge into the following text. Cursor positions at
the wrap boundary stay with the row.

- A source range cannot represent both the bytes on a row and the earliest
  cursor that row owns once the separator is gone, so the walk uses
  `WrappedLine`.
- Rendering, navigation, and height share that wrapped-line model with
  editing.
- Tests lock cursor ownership at the exact-width boundary: placement,
  rendered rows, and delete/reinsert.
```

The bullets stay because the diff cannot say why a source range is the wrong
type. They are not a template for a three-line extract.

### Explain a narrow parser correction

```text
Preserve Markdown hard breaks through stream finalization

Ordinary assistant lines keep trailing spaces through finalization, so
completed content matches the streamed source.

- Unchanged directive stripping does not rewrite the line, so whitespace
  cleanup stays on lines the parser modifies.
- Whitespace-only tail lines count as empty. Visible lines keep their spaces.
- Tests lock hard-break preservation through finalization, including the
  no-reflow completion path.
```

## Reject these failure modes

- A subject-only message for a change with non-obvious behavior or tradeoffs.
- A body that restates diff-visible mechanics with no why.
- A message that rivals the size of the change (three paragraphs for a
  three-line extract).
- A body that inventories files, symbols, or edits without explaining impact.
- A long paragraph containing change, cause, design, tests, and caveats at once.
- Explicit `What` and `Why` sections that make natural causal prose feel templated.
- A rationale that appears before the reader knows what changed.
- Still-true claims: tests still pass, unchanged behavior still works, callers
  not touched still compile.
- A validation bullet that inventories commands, pass counts, unrelated
  failures, or CI state instead of test coverage added or updated by the commit.
- Test-coverage claims that are not supported by tests added or updated in the
  diff.

## Final check

Read only the subject, opening sentence, and bullet starts as if they were a
line in `git log`. They should name the outcome and the reason. They should
not summarize the patch.

Delete any sentence that restates a point already made, any clause that
describes a diff-visible mechanic with no why, any still-true claim, and any
paragraph the change did not earn.
