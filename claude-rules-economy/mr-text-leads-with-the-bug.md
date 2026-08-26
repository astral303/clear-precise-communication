# MR text leads with the user-visible change

An MR title names what the user sees fixed or changed, never the mechanism.
The description opens with the problem in the reader's terms, then the
after-state, then cause and fix. Same order for the commit subject. A feature
MR still leads with the user-visible effect.

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |

If a reader who never opened the diff cannot tell what improved, the title is
wrong.

Description order:

1. **The bug** (or **The change**): user-visible problem or effect.
2. **After this change**: what they see now.
3. Cause, then fix, under noun-phrase headings.
4. Validation: named test groups, not every case.

Do not open with a symbol, file, or function. Explain status-bar jargon on
first use. Every old-vs-new contrast uses `now` or `no longer`.

A refactor with no user-visible change still titles the invariant that moved,
not a file list. Mechanism can be interesting in section 3; it is not the
title.
