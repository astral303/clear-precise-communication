# Reviewer-facing writing: describe, do not advocate

When a third party evaluates work — PR descriptions, reviewer guides,
self-review comments, design docs, review replies — describe the code. Do not
argue for it. A design doc that sells the implementation is in violation.

Structure each explanation: Decision (what the code does) → Reason (what
problem that solves) → Boundary (under what conditions the claim holds). The
boundary makes an absolute impossible.

| Cut | Replace with |
| --- | --- |
| *only, always, never, everything else, no matter what, cannot* | The actual condition |
| *mechanical, can't regress, low risk* | A review **depth** and the code's purpose |
| *the deferral is safe, the failure mode is loud* | What fails, and with what message |
| "Why the crop width is hardcoded" | Topic label: "Curated pair ordering" |

A reviewer's guide is navigation: where to look, in what order, how deeply.
A line comment explains code that would otherwise look arbitrary. Assign a
depth ("skim", "read the tests") without the verdict "low risk". If you cannot
name the condition, you cannot support *always*/*never*.
