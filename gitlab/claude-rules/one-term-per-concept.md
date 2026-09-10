# One term per concept, no synonyms

Use one term for one concept across a change's title, body, commit message,
changelog entry, README sentence, and doc comments. Do not swap in a synonym
for variety or to fit a line.

Every extra term makes the reader check whether it is the same thing. An
inexact synonym also narrows or shifts the meaning, and can collide with a
word the product already uses.

## Scope

Every durable artifact for the change, together: MR title and description, commit
subject and body, issue text, changelog, user docs, `///` and `//` comments,
test names, assertion messages, and user-facing copy.

This is not an "MR description only" rule. If the title, the changelog, and a doc
comment each use a different name, the rule was already ignored.

User-facing text uses the words on screen. Identifiers and comments that
name the same concept use that same word. See also
`write-from-the-reader.md` and `literal-verbs-not-idioms.md`.

## Required shape

Pick the term once. Define it once at first use if the reader would not
already know it. Reuse it verbatim.

| Same concept, three names (cut) | One term (write) |
| --- | --- |
| calls issued together / interleaved calls / alternate | interleaved calls, defined at first use |
| parallel batch (as another name for that group) | batch — the group noun, including in identifiers |
| interleave rewritten as alternate in one sentence | interleaved, verbatim |
| not read / unread / ignored | the word the UI already uses |

A group noun is a second concept, not a synonym. "Interleaved calls" names the
calls; "batch" names the group. "A batch of interleaved calls" is two terms
for two concepts. "Parallel batch" and "issued together" still rename the
calls, so they are out.

"Alternate" for interleaved calls is the inexact-synonym failure: it implies a
binary pattern, and it collides with "alternate screen" if the product already
has that term. Closeness is not sameness.

## Closed loopholes

- "I varied it to avoid repetition." Repeat the term. Variety is the defect.
- "The synonym is close enough." If it narrows, shifts, or collides with an
  existing product word, it is a different concept. Do not use it.
- "The title needed a shorter phrase." Shorten without renaming the concept.
- "The comment is explaining in different words." The comment uses the same
  term as the MR and the changelog.
- "Code already uses the other word." Then the durable prose either adopts
  that word everywhere, or the code is renamed. Do not keep both in the
  artifacts the reader sees.
- "Batch appeared, so I grepped it out as a synonym." Only replace names of
  the same concept. Do not flatten a group noun, an identifier, or another
  distinct term.

## Final scan

Name the chosen term. Search the artifact and the touched comments for every
other phrasing you used while drafting. Replace those hits with the chosen
term. If two terms both appear and you cannot say they are different
concepts, you have not picked yet — pick, then scan again.
