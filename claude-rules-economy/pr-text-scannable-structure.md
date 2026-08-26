# Scannable engineering docs

PR bodies, issue drafts, and similar engineering docs are built so the
structure is visible without reading the prose.

A reviewer should not have to dig the structure out of a paragraph.

## Scope

Pull request bodies, issues, design docs, reviewer guides, plans, ADRs, and
any engineering note that lists facts, mappings, or behavior. Commit bodies
when they contain more than one fact.

This is not "when I remember to make it pretty." If the content is a series of
parallel facts, the first draft is bullets. If the content is a grid, the
first draft is a table. Do not write a paragraph and convert later.

`clear-precise-communication` already requires bullets for a series of points
and tables when they make decisive information easier to find. This file makes
that mechanical.

## Shape the content to the data

Ask of each section:

| Content | Shape |
| --- | --- |
| A grid (key × focus state, name → canonical tool → input change) | A table |
| Parallel facts | Bullets, one fact each |
| Ordered work | Numbered steps |
| One idea with a because-clause | One short paragraph |

Group bullets under short labels: `Summary sentences:`, `Headers:`,
`Unchanged:`.

Do not follow a bullet with a paragraph that restates it.

## One fact per bullet

A bullet is one fact. Not a fact plus a trailing "so that…" justification. Not
two behaviors joined with "and".

| Do not write | Write |
| --- | --- |
| `→`/`←` and `J`/`K` move between calls | One bullet per key, with its full behavior |
| "Copies the session ID so that the user can paste it" | "Fix `I` copying the actual session ID" |
| A sentence that summarises the sentence before it | Delete the second sentence |

Tests sections name the **groups** covered, not every case.

## Delete on sight

These are AI-shaped filler. Remove them when they appear:

- "the way X does"
- "hides nothing, whichever…"
- "happy to…"
- "One-line fix" as a heading or opener
- "as before" repeated per bullet
- parenthetical asides that duplicate the sentence
- "this change makes it so that"
- "in order to" when a verb would do
- a summary sentence above a list that the list already states

## Closed loopholes

- "I didn't notice it needed to be bullets until the sentence was written."
  Look at the content type before writing. Parallel facts → bullets. Grid →
  table. That choice is made first, not after a paragraph exists.
- "A short paragraph is more readable." Not for a list of keys, mappings, or
  behaviors. Those are tables or bullets.
- "The table felt too heavy for three rows." Three rows of key × behavior is
  still a table. A sentence with two em-dashes is not a table.
- "This is chat, not the PR." If the chat text is the PR body, it is the PR
  body.

## Final scan

For each section: if you can put it in a two-column table, do. If you can put
it in bullets, do. Delete any paragraph whose first sentence restates the
heading or the bullet above it. Delete the filler phrases in "Delete on sight".
