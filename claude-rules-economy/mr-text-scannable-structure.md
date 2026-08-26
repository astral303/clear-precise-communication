# Scannable engineering docs

MR descriptions, issues, and similar notes are built so the structure is
visible without reading the prose. If the content is a series of parallel
facts, the first draft is bullets. If it is a grid, the first draft is a
table.

| Content | Shape |
| --- | --- |
| Grid (key × state, name → tool → input) | Table |
| Parallel facts | Bullets, one fact each |
| Ordered work | Numbered steps |
| One idea with a because-clause | One short paragraph |

A bullet is one fact. Not a fact plus "so that…". Not two behaviors joined
with "and". Do not follow a bullet with a paragraph that restates it. Tests
sections name groups covered, not every case. Three rows of key × behavior is
still a table.

Delete on sight: "the way X does", "happy to…", "One-line fix", "as before"
repeated per bullet, "this change makes it so that", "in order to" when a verb
would do, a summary sentence above a list the list already states.

If the chat text is the MR description, it is the MR description.
