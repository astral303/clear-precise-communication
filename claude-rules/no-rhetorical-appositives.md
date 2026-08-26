# No rhetorical appositives

A sentence like `Wrapped text — a reply, a result, a shell command — now
reflows…` is a rhetorical appositive: it announces a category, pauses,
illustrates, then delivers the verb. The `a …, a …, a …` is a tricolon
(pulpit rhythm). Neither belongs in a changelog bullet, an MR description, a
commit
message, or a doc sentence.

This does not ban the em-dash. It bans using the dash as stage directions:
pause, enumerate, resume.

## Scope

Every durable artifact: changelog entries, MR titles and descriptions, commit
messages, issues, user docs, `///` and `//` comments, and any sentence that
states a change.

## Why it fails a changelog

A changelog bullet is a record. The first clause names what broke or what
the user can do now. A rhetorical appositive is a talk: theme, then examples,
then the news. The reader is already scanning bullets and does not need a
spoken list inside the sentence. Working memory goes to "what does 'wrapped
text' include?" instead of the fix. The verb is delayed on purpose.

## Test

Delete the dashed phrase. If the subject turns vague, those words were the
subject, not an aside. Put them before the verb:

| Cut | Write |
| --- | --- |
| Wrapped text — a reply, a result, a shell command — now reflows… | Wrapped replies, results, and shell commands no longer … |

If the parent bullet already carries that fact, cut the sentence. A
sub-bullet must add a fact the parent cannot carry, or it goes.

An em-dash is fine when it defines or contrasts **one** thing, and the
sentence still leads with the change:

> Wrapped lines no longer run under the timestamp — wrap width now excludes
> that column.

## Closed loopholes

- "I was listing the kinds of wrapped text." Then they are the subject, or
  they are a bullet list. They are not a dash chorus after a category noun.
- "The parent named the bug; this sentence explains." Explanation is one
  added fact (for example: wrap still used the full width). Restating the
  parent as mechanism is not an added fact.
- "I only grepped banned words, and em-dash is not banned." This construction
  is caught by a read, not a search. See `final-scan.md`.

## Final scan

For each dashed phrase: delete it. If the sentence loses its subject, rewrite
with the examples before the verb, or delete the sentence. For each
sub-bullet: name the fact the parent cannot carry. None → delete.
