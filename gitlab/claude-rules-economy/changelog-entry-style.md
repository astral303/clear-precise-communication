# Changelog entry style

A changelog reader wants the class of change, what was broken, and what they
can now do. Follow the repo's existing format when it has one. Otherwise group
by change class, not by feature area:

- `### Enhancements`
- `### Fixes`
- `### Internal: …` for non-user-facing work

Headings are optional. The parent bullet is a standalone summary — the
sentence a reader can stop at. Mark non-user-facing groups `Internal:`.

Fixes lead with the verb and the symptom, not the end state:

| Do not write | Write |
| --- | --- |
| Tool runs in summary mode: | Improve collapsed tool rows in tools summary mode |
| `I` copies the session ID to the clipboard | Fix `I` copying the actual session ID |

When components or surfaces share one behavior, one parent line names them
all; own bullets only when a behavior differs. Name a component only when
the change is what it does. When one starts behaving as its neighbors
already do, the entry names the change and skips that shared behavior. Do
not add that the
new behavior matches behavior the product already had ("as the other
routes do").
User-visible symptom in the parent; mechanism as a sub-bullet only if the
reader must act on it. A sub-bullet must add a fact the parent cannot
carry, or it is cut.

A small, one-condition fix is one or two lines stating what the user now
sees. If the user would have expected the thing already, it is a Fix:
`Fix <thing> missing from <surfaces>.` not an Enhancement that ends "until
now they were not read."

Verify each entry against what shipped. US spelling unless the project uses
otherwise. Capitalize `Markdown`.
