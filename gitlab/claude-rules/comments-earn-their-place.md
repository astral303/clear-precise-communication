# Comments earn their place

First express the idea through names, structure, types, and tests. A comment
is not a substitute for those, and a comment is not an acceptable fix for a
review finding of the form "the next reader could break X without noticing."

## Scope

`///` doc comments, `//` comments, `#` comments, module-level docs, review
suggestions that propose adding a comment, and self-review line comments
destined for GitLab.

This file is the comments half of clean-code "necessary comments only" plus
the reviewer-facing rule that a comment must not advocate. It applies while
writing code, not only during review.

## Order of answers

When a constraint is not obvious:

1. What shape of code makes the mistake impossible or obvious? (constructor
   that establishes the invariant, a type, a function boundary, a name that
   states the predicate)
2. Which test fails if the mistake is made?
3. Only if neither exists: a comment, and then say why structure could not
   carry it.

A self-describing name beats a documented constant:
`Deleted::just_the_session()` replaces `Deleted::ONE_COPY` plus its doc.

## Allowed comment content

Keep only what the code cannot say:

- why this branch and not the obvious one
- a consequence someone would break by "simplifying"
- a limit the reader would otherwise assume away
- a public-contract detail the signature does not carry

Explain *why*, not line-by-line *what*.

Each comment should identify the non-obvious decision, give the behavior or
invariant it preserves, state any condition limiting the claim, stay local to
the anchored code in 2–3 sentences, and stop short of arguing the
implementation is unquestionably correct.

## Banned comment content

| Cut | Why |
| --- | --- |
| Restatement of the signature | The signature already says it |
| Restatement of the next line (`// increment i` above `i += 1`) | The code already says it |
| Restatement of the test's name | The test name already says it |
| `What X does / Where X lives / Whether X` | Banned construction; see `noun-phrase-labels-not-questions.md` |
| Idioms (`goes with the parent`) | Literal verbs; see `literal-verbs-not-idioms.md` |
| Verdicts (`this is safe`, `mechanical`, `can't regress`) | Describe; see `reviewer-facing-describe-dont-advocate.md` |
| Narration of the diff you just wrote | The reader has the code, not your session |

Keep internal checklist notes visibly separate from text destined for GitLab.

## Closed loopholes

- "A comment is the smallest change." Smallest is not best. A constructor, a
  name, or a test that fails is the change. Propose the comment only after
  saying why those cannot carry it.
- "The function is clear, I'm just being thorough." Thorough restatement is
  noise. Delete it.
- "I'll add the comment now and we can refactor later." The comment becomes
  the record of a structural problem you chose not to fix. Fix the structure.

## Final scan

For each new or edited comment: if deleting it would not change what a cold
reader understands, delete it. If a name or a test would make it unnecessary,
do that instead. Remaining comments are 2–3 sentences, local, no advocacy, no
What/Where/Why openers.
