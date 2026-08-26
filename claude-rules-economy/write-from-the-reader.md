# Write from the reader, not from the diff

Before a sentence goes into a README, doc comment, or inline comment, name
what the reader does differently for having read it. If they would find that
out by doing it, cut the sentence. Comments and drafts are in scope the same
as READMEs.

Document what the software will **not** tell the reader at the right moment.
Do not document what the UI already shows.

## Usefulness test

1. What task is the reader in the middle of?
2. What would they do wrong without this sentence?
3. Does the software already say this at the moment it matters?

Keep the sentence only if (2) is a real failure and (3) is no. Truth is not
usefulness.

## Do not narrate the diff

The reader has a task, not your branch table. Do not enumerate every code path
you added.

| Wrote because you built it | Reader needed |
| --- | --- |
| "An ID that turns up nowhere is reported as not found." | Cut. They will see the message. |
| "Pi/OMP sessions that only open by ID have nothing on the list to click." | Keep. Silence would strand them. |

Prefer the words on screen over identifiers. Cut engineer-only vocabulary from
user text unless the user must type it: `bounded`, `resolved`, `in force`,
`the lookup`, `canonical`. Once you pick a term, reuse it verbatim; see
`one-term-per-concept.md`.

Generic features get generic descriptions: condition, indicator, action — not
today's only instance. Completeness that restates the UI is padding;
completeness that names a limitation is useful.
