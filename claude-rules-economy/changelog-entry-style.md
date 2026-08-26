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

One bullet per key or behavior, including fallbacks. User-visible symptom in
the parent; mechanism as a sub-bullet only if the reader must act on it. A
sub-bullet must add a fact the parent cannot carry, or it is cut.

Verify each entry against what shipped. US spelling unless the project uses
otherwise. Capitalize `Markdown`.
