# Changelog entries

The reader wants the class of change, what was broken, and what they can now
do. Follow the repo's existing format when it has one. Otherwise group by
change class: `### Enhancements`, `### Fixes`, `### Internal: …`. Headings are
optional. The parent bullet is a standalone summary. Mark non-user-facing
groups `Internal:`.

Fixes lead with the verb and the symptom:

| Do not write | Write |
| --- | --- |
| Tool runs in summary mode: | Improve collapsed tool rows in tools summary mode |
| `I` copies the session ID | Fix `I` copying the actual session ID |

One bullet per key or behavior. Mechanism is a sub-bullet only if the reader
must act on it. A sub-bullet must add a fact the parent cannot carry, or it
is cut. Verify each entry against what shipped. US spelling unless the project
uses otherwise. Capitalize `Markdown`.

## Impact claims

A ratio transfers to the reader's machine. Raw seconds, raw counts, and
layout constants the UI does not print (`seven columns`) do not. Parent:
verb, effect, ratio, parenthetical scope. The ratio comes first.

| Do not write | Write |
| --- | --- |
| a warm search over 1,282 items went from 8.5 to 3.3 seconds | about 2.6x faster (on one example corpus) |
| Migration cost in seconds | takes about 4x a normal load, once |

A percentage the reader can compare to their corpus is fine. State who gains
little next to who gains most. Do not write that the feature works as
expected, or that it wraps "at any window width". For each remaining line: is
it new, reachable, and actionable?
