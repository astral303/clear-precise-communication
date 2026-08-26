# PR bodies are permanent records

A PR description is read by people with no access to the author's machine.
Keep facts about the change. Keep out working-tree state, other branches,
wall-clock timings, and advice about when to do a follow-up.

A scope reason must be structural ("clearing them edits Rust code, which is
outside this change"), never situational ("worth doing once the concurrent
work lands").

| Cut | Why |
| --- | --- |
| Other branches being edited | No archaeological value |
| Timings on the author's hardware | A later reader cannot reproduce them |
| Advice ("worth doing as its own branch once…") | A PR is not a coaching note |
| Plan-internal names (`PR A`, `plans/…`) | Often gitignored; the reader cannot resolve them |
| Specifics of a later change | Allowed: "pending a future change" |
| Validation as seconds | Name which checks pass, not how long |

If the PR is not against the default branch, say so in **chat**, on its own
line: name the base, and that it must merge first or the commit strands. Do
not put the stacking plan in the PR body.
