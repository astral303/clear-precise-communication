# Reviewer-facing writing: describe, do not advocate

When writing anything a third party reads to **evaluate** work — PR
descriptions, reviewer guides, self-review line comments, design docs,
code-review replies — describe the code. Do not argue for it.

Advocacy reads as defensiveness. A reviewer told "everything else is
mechanical" starts distrusting the whole guide. Stating an observable fact is
enough; the reader draws the conclusion.

## Scope

PR bodies, reviewer guides, self-review comments, design docs, review replies,
and any comment that explains a choice to a future reader.

This is not "PRs only". A design doc that sells the implementation is in
violation. A line comment that says the deferral is safe is in violation.

## Structure each explanation

Decision (what the code intentionally does) → Reason (what concrete problem
that solves) → Boundary (under what conditions the claim holds).

The Boundary does the real work: it is impossible to write an absolute once
the conditions must be stated.

## Delete these

| Tell | Replace with |
| --- | --- |
| Absolutes: *only, always, never, everything else, no matter what, cannot* | The actual condition. Not "defaults always keep their order no matter what the user adds" but "when both halves of a curated default pair remain, the first pass preserves their declaration order." |
| Verdicts on parts of the diff: *mechanical, can't regress, low risk* | A review **depth** and the code's purpose. Not a verdict. |
| Safety assertions: *deliberately not, the deferral is safe, the failure mode is loud* | Observable behavior — what fails, and with what message. |
| Headings that presuppose a challenge: "Why the crop width is hardcoded" | Topic labels: "Curated pair ordering". See `noun-phrase-labels-not-questions.md`. |

## Division of labor

A reviewer's guide handles navigation: where to look, in what order, how
deeply, and which areas carry risk.

A line comment explains specific code that would otherwise look arbitrary,
surprising, or wrong. See `comments-earn-their-place.md` for whether the
comment earns its place at all.

Overlap with the PR description is acceptable when inline placement materially
reduces review effort. The goal is putting context where the reviewer needs
it, not zero repetition.

## Closed loopholes

- "I was helping the reviewer by flagging low-risk files." Assign a depth
  ("skim", "read the tests") without the verdict "low risk".
- "Always/never was accurate." Then write the condition that makes it true.
  If you cannot name the condition, you cannot support the absolute.
- "The implementation is correct and I don't want a bikeshed." Describing the
  boundary is what prevents the bikeshed. Asserting correctness invites it.

## Final scan

Search for: `only`, `always`, `never`, `everything else`, `no matter what`,
`mechanical`, `low risk`, `can't regress`, `safe`, `deliberately`. Each hit
becomes a condition, a depth, or a deletion. Headings are topic labels.
