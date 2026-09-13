# Name it from what the user saw

Do not define a thing by who failed to possess it. Define it by what the
user saw.

"A session ID that no agent stores" makes the store the subject of the miss.
The user pasted an ID and saw `not found`. That is the name of the thing.

This is not a search-box rule. Any absence named from the internals
(*stores*, *holds*, *contains*, *emits*, *returns*) is the same point of
view: the thing is defined by **who failed to have it**, not by **what
appeared**.

## Scope

Every durable artifact: changelog entries, PR titles and bodies, commit
messages, user docs, issues, comments, and UI copy. If the screen already
has a word for the miss (`not found`, `ignored`, a missing row), that is
the term. See `one-term-per-concept.md` and `write-from-the-reader.md`.

## Required shape

| Who failed to possess it (cut) | What the user saw (write) |
| --- | --- |
| a session ID that no agent stores | an unknown session ID / an ID that is not in the list |
| when no agent stored it | when it was not found |
| no disk stored the file | file not found |
| a document that stored no match | no match |
| a row no renderer emitted | a missing row |

English already has the lookup-first shape: *file not found*, *page not
found*, *no match*. The store does not get a speaking part.

The tell is a relative clause or *when*-clause whose verb is possession by
an internal actor: *that no X stores/holds/contains/emits/returns*, *when
no X stored it*. Rewrite from the person looking.

## Closed loopholes

- "This was not a lookup, so the rule does not apply." The rule is the
  point of view, not the search box. A missing row named from the renderer
  is the same defect.
- "No agent stores it is the precise condition." It is the code path. The
  user-visible miss is the condition in prose.
- "Agent is the domain word." Not in a sentence about a miss. The list, the
  search box, and `not found` are the domain words.
- "I already said not found in the next line." Then "no agent stores" is a
  second name for the same miss. Cut it.
- "This is a commit, so internals are fine." The commit still names what
  the user saw, then the defect. See `write-commit-messages`.
- "`stores` is a literal verb." Literal for *delete* and *count*. For a
  miss, the verb is *found* / *shows*. See `literal-verbs-not-idioms.md`.

## Final scan

Search for `that no `, `when no `, `stores`, `stored it`, `holds no`,
`contains no`, `did not emit`, `did not return` used to name an absence.
Each hit becomes what the user saw (*not found*, *missing*, *unknown*),
unless the sentence is actually about a store's capacity.
