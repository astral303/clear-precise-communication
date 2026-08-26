# Pull requests, commits, and issues

A title names what the user sees fixed or changed, never the mechanism. The
body opens with the problem in the reader's terms, then the after-state, then
cause and fix. Same order for the commit subject. A feature PR still leads
with the user-visible effect.

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |

If a reader who never opened the diff cannot tell what improved, the title is
wrong. A refactor titles the invariant that moved, not a file list.

Body order: **The bug** (or **The change**) → **After this change** → cause
and fix under noun-phrase headings → validation as named test groups. Do not
open with a symbol, file, or function. Explain status-bar jargon on first use.
Every old-vs-new contrast uses `now` or `no longer`.

## Scannable shape

If the content is parallel facts, the first draft is bullets. If it is a grid,
the first draft is a table. A bullet is one fact. A child bullet must add a
fact the parent cannot carry. Tests sections name groups, not every case.
Three rows of key × behavior is still a table. If the chat text is the PR
body, it is the PR body.

Delete on sight: "the way X does", "happy to…", "One-line fix", "as before"
per bullet, "this change makes it so that", "in order to" when a verb would
do, a summary sentence above a list the list already states.

## Permanent record

Keep facts about the change. Keep out working-tree state, other branches,
author-machine timings, and advice about when to do a follow-up. A scope
reason must be structural, never situational.

Cut: other branches; timings; "worth doing once…"; plan-internal names (`PR
A`, `plans/…`); specifics of a later change (allowed: "pending a future
change"); validation as seconds.

If the PR is not against the default branch, say so in **chat**, on its own
line. Do not put the stacking plan in the PR body.
