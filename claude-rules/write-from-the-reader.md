# Write from the reader, not from the diff

Before a sentence goes into a README, a doc comment, or an inline comment, name
what the reader does differently for having read it. If the answer is "nothing —
they would find that out by doing it", cut the sentence.

Document what the software will **not** tell the reader at the right moment:
limitations, constraints, options nobody would guess. Do not document what the
UI already says on screen.

## Scope

Every durable artifact, and **code comments and doc comments exactly as much as
READMEs**. Reading this as "user-facing docs only" is the mistake that let it
be ignored three times.

Applies to: READMEs, user docs, changelogs, PR bodies, `///` comments, `//`
comments, module docs, error-string comments, and any prose that explains
behavior.

## Usefulness test

For each sentence, answer:

1. What task is the reader in the middle of?
2. What would they do wrong, or fail to do, without this sentence?
3. Does the software already say this at the moment it matters?

Keep the sentence only if (2) is a real failure and (3) is no.

A sentence can be true and still fail this test. Truth is not the bar.
Usefulness is.

## Do not narrate the diff

You implemented three branches. The reader has a task, not your branch table.

| Wrote because you built it | What the reader needed |
| --- | --- |
| "An ID that turns up nowhere is reported as not found." | Nothing. They will see the message. Cut. |
| "Lookup checks the list, then the disk, then reports not found." | Nothing. Narration of control flow. Cut. |
| "Pi/OMP sessions that only open by ID have nothing on the list to click." | Keep. Silence would strand them. |
| "which for Codex, Kimi and Pi is not what the file is called" | Cut unless the reader must type that filename. Name the condition, not today's instances. |

Do not enumerate every code path you added. Do not name three of four providers
when the rule is generic.

## Prefer the words on screen

Use the label the user sees, not the identifier in the code.

Cut engineer-only vocabulary from user text unless the user must type it:
`bounded`, `resolved`, `in force`, `the lookup`, `canonical`, `materialize`,
`hydrate`.

Generic features get generic descriptions: the condition, the indicator, and
the action — not today's only instance of it.

## Comments

In a comment, keep only what the code cannot say:

- why this branch and not the obvious one
- a consequence someone would break by "simplifying"
- a limit the reader would otherwise assume away

Cut restatements of the signature, of the method call on the next line, and of
a test's own name. See `comments-earn-their-place.md`.

## Closed loopholes

- "I documented it so the README would be complete." Completeness that restates
  the UI is padding. Completeness that names a limitation is useful.
- "It's a comment, so the reader is a programmer." Programmers still do not
  need the next line of code repeated in English.
- "The changelog should mention the mechanism." The parent bullet is the
  user-visible change. Mechanism is a sub-bullet only if the reader must act
  on it.
- "I listed the providers so it would be precise." If the behavior is generic,
  describe the condition. Today's provider list goes stale.

## Final scan

For each sentence in docs and comments: if the reader learns it by clicking,
running, or reading the next line of code, delete it. If the vocabulary is
from the type name and not from the screen, replace it.
