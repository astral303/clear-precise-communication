# MR text leads with the user-visible change

An MR title names what the user sees fixed or changed, never the mechanism.
The description opens with the problem in the reader's terms, then the
after-state, then cause and fix.

The same order applies to the commit subject.

## Scope

Merge request titles and descriptions, commit subjects and bodies, issue
titles that report a defect, and changelog parent bullets for fixes. Comments
that explain a bugfix follow the same order: symptom first, mechanism second.

This is not a "bug tickets only" rule. A feature MR still leads with the
user-visible effect, not the refactor that enabled it.

## Title

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |
| Share fold state through the scratch buffer | Keep a folded tool run folded when the next entry is empty |

If a reader who never opened the diff cannot tell what improved, the title is
wrong.

## Description order

1. **The bug** (or **The change**, for a feature): the user-visible problem or
   effect, in the reader's terms.
2. **After this change**: what they see now.
3. Cause, then fix, under their own noun-phrase headings.
4. Validation: named test groups, not a tour of every case.

Do not open with a symbol name, a file, or a function. If the status bar, a
key, or a mode flag is required to understand the bug, explain it on first
use: `summary mode (press t until the status bar reads tools·sum)`.

## Old vs new

Every sentence that contrasts old and new behavior uses `now` or `no longer`
so the tense carries the meaning.

| Ambiguous | Clear |
| --- | --- |
| "A Codex run of consecutive tool calls shows as one `Called N tools` row instead of one `Called 1 tool` row per call." | "Summary mode showed one `Called 1 tool` row per Codex tool call. It now shows one `Called N tools` row for the run." |

A reader must not have to guess whether the sentence describes the bug or the
fix.

## Closed loopholes

- "The mechanism *is* the interesting part." It can be interesting in section
  3. It is not the title and not the first sentence.
- "The audience is other engineers, so symbols are fine." Engineers still need
  the symptom first. Symbols come after, defined on first use.
- "This is a refactor with no user-visible change." Then the title names the
  invariant that moved or the failure the refactor makes impossible — still an
  effect, not a file list.

## Final scan

Read only the title and the first two headings. They must name the
user-visible problem and the after-state. If they name a function, rewrite.
Search contrast sentences for `now` / `no longer`. If a contrast relies on
tense alone, add the marker.
