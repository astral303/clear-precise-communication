# PR text leads with the user-visible change

A PR title names what the user sees fixed or changed, never the mechanism. The
body opens with the problem in the reader's terms, then the after-state, then
cause and fix. A feature PR still leads with the user-visible effect.

Commit subjects do not follow this order. They follow the
`write-commit-messages` skill: changed behavior or invariant first, then the
defect that required it. A PR title can name the bug while the commit names
the behavior that moved, not `Refactor the lookup`.

Name a key when the change is what that key does, and name every such key.
A key that did nothing before is `Add support for …`; a changed key is
`ensure …`. A row that starts using an expand those keys already perform
gets no key list. Use the changelog's noun. Two changes join with a
semicolon, each with its own verb.

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |

If a reader who never opened the diff cannot tell what improved, the title is
wrong. Setup → `instead of` the bug is a tour; see
`setup-then-point-is-a-tour.md`. No `Until now` or `Let ` as the opening.

Body order:

1. **The bug** (or **The change**): user-visible problem or effect.
2. **After this change**: what they see now.
3. Cause, then fix, under noun-phrase headings.
4. Validation: two to four lines of coverage groups. No test names.

Do not open with a symbol, file, or function. Name a status-bar mode on
first use (`summary mode (tools·sum in the status bar)`). Do not add the
keystroke that reaches it. Every old-vs-new contrast uses `now` or
`no longer`.

A refactor with no user-visible change still titles the invariant that moved,
not a file list. Mechanism can be interesting in section 3; it is not the
title.
