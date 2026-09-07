# Name the type, not a nickname

When a sentence rests on a code concept, the first mention is the identifier
plus one clause of meaning. Reuse that identifier verbatim afterwards. Do not
shorten it to a nickname, and do not invent a category word for an existing
mechanism.

## Scope

Chat, plans, PR bodies, design docs, reviewer notes, and comments. Applies
the moment a type, module, or function is the thing being discussed.

## Required shape

| Do not write | Write |
| --- | --- |
| the stub | `` `SessionStub`, what discovery returns per session before parsing `` |
| spliced entry stream | `` `splice.rs` inserts a sub-agent's messages into the parent's list `` |
| merging scalars | the two counts, named |

First mention = identifier + one clause of what it does in the reader's
terms. Later mentions reuse the identifier. See
`one-term-per-concept.md`.

A design that has not been seen yet is judged against what exists now:
prefer moving an existing function over introducing a new mechanism.

## Closed loopholes

- "The nickname is obvious in context." Context is the previous sentence in
  your head. The reader is entering cold.
- "Scalars is just a word for two numbers." If it reads as a new feature, it
  is a nickname. Name the two numbers.
- "The module name is too long to repeat." Repeat it. Variety is the defect.

## Final scan

For each new noun in the artifact: is it an identifier the code uses, or a
word you coined? Coined words become the identifier plus one clause, or they
are deleted.
