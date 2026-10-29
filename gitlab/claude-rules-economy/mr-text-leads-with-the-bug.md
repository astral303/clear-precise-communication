# MR text leads with the user-visible change

An MR title names what the user sees fixed or changed, never the mechanism. The description opens with the problem in the reader's terms, then the after-state, then
cause and fix. A feature MR still leads with the user-visible effect.

Commit subjects do not follow this order. They follow the
`write-commit-messages` skill: changed behavior or invariant first, then the
defect that required it. An MR title can name the bug while the commit names
the behavior that moved, not `Refactor the lookup`.

Name a control or setting (a key, a mode, a route) only when the change
is what that thing does, and name every such thing. A thing that did
nothing before is `Add support for …`; a changed thing is `ensure …`.
Do not re-explain machinery the change leaves unchanged: when one thing
starts behaving as its neighbors already do, name the change, not
the behavior they already share. When one route starts retrying, do not
list the retry settings every route already shares. Use the changelog's noun. Two
changes join with a semicolon, each with its own verb.

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |

If a reader who never opened the diff cannot tell what improved, the title is
wrong. Setup → `instead of` the bug is a tour; see
`setup-then-point-is-a-tour.md`. No `Until now` or `Let ` as the opening.

Follow the repository's merge request template when it has one. Keep its
headings. Do not rename them. The description still carries, in order: the
user-visible problem or effect, what the user sees now, the cause and the
fix, and what was tested (two to four lines of coverage groups, no test
names). When there is no template, use noun-phrase headings for those facts.

Do not open with a symbol, file, or function. Name a required mode or
setting on first use (`dry-run`, `verbose`), not the keystroke or flag
that reaches it. Every old-vs-new contrast uses `now` or
`no longer`.

A refactor with no user-visible change still titles the invariant that moved,
not a file list. Mechanism comes after the effect; it is not the title.
