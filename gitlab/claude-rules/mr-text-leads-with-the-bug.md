# MR text leads with the user-visible change

An MR title names what the user sees fixed or changed, never the mechanism. The description opens with the problem in the reader's terms, then the after-state, then
cause and fix.

Commit subjects do **not** follow this order. They follow the
`write-commit-messages` skill: the subject and opening sentence name the
changed behavior or invariant, then the defect, constraint, or tradeoff that
required it. An MR title can name the bug while the commit names the
behavior that moved (`Read sub-agent transcripts through their parent
session`), not `Refactor the provider lookup`.

## Scope

Merge request titles and descriptions, issue titles that report a defect, and
changelog parent bullets for fixes. Comments that explain a bugfix follow the
same order: symptom first, mechanism second.

This is not a "bug tickets only" rule. A feature MR still leads with the
user-visible effect, not the refactor that enabled it.

## Title

| Do not write (mechanism) | Write (user-visible effect) |
| --- | --- |
| Keep a tool run folded across entries that render nothing | Fix summary mode showing one `Called 1 tool` row per tool call |
| Refactor session lookup into a three-pass resolver | Report a missing session ID as not found |
| Share fold state through the scratch buffer | Keep a folded tool run folded when the next entry is empty |

If a reader who never opened the diff cannot tell what improved, the title is
wrong. A title that walks setup → `instead of` the bug is a tour. See
`setup-then-point-is-a-tour.md`. Do not open a description with `Until now` or
`Let `. Do not park the bug in `although` or in the last sentence.

Name a control or setting the change touches (a key, a mode, a config
flag, or a route) only when the change is what that thing does, and name
every such thing, not only the one that headlines. A thing that did
nothing before is `Add support for …`; a thing whose behavior changed
is `ensure …`. Do not list or re-explain machinery the change leaves
unchanged: when one thing starts behaving as its neighbors already do, name
the change, not the behavior they already share. When one route starts
retrying, do not list the retry settings every route already shares. Use the changelog's noun for the thing. Two changes in one MR
are joined with a semicolon, each with its own verb.

## Description order

Follow the repository's merge request template when it has one. Keep its
headings and its section order. Do not rename them.

The description still carries these facts, in this order, in whichever
section the template uses for each:

1. The user-visible problem or effect, in the reader's terms. For a feature,
   the effect, not the refactor that enabled it.
2. What the user sees after the change.
3. Cause, then fix.
4. What was tested: two to four lines naming coverage groups. No test names,
   no per-case lines. See `mr-text-scannable-structure.md`.

When the repository has no template, use noun-phrase headings for those
facts.

Do not open with a symbol name, a file, or a function. If a named mode,
control, or setting is required to understand the bug, name what it is
on first use, not the keystroke, flag, or command that reaches it: name
the setting (`dry-run` mode, `verbose` logging), not how to turn it on. The
MR describes the change, not how to operate the program.

## Old vs new

Every sentence that contrasts old and new behavior uses `now` or `no longer`
so the tense carries the meaning.

| Ambiguous | Clear |
| --- | --- |
| "A Codex run of consecutive tool calls shows as one `Called N tools` row instead of one `Called 1 tool` row per call." | "Summary mode showed one `Called 1 tool` row per Codex tool call. It now shows one `Called N tools` row for the run." |

A reader must not have to guess whether the sentence describes the bug or the
fix.

## Closed loopholes

- "The mechanism *is* the interesting part." It can come after the effect.
  It is not the title and not the first sentence.
- "It didn't behave this way before, so list how it works."
  Its neighbors already work that way. Name the change, not the shared behavior.
- "The audience is other engineers, so symbols are fine." Engineers still need
  the symptom first. Symbols come after, defined on first use.
- "This is a refactor with no user-visible change." The MR title still names
  the user-visible effect or the failure the change makes impossible. The
  commit subject names the behavior or invariant that moved, not a file list.
- "The commit should match the MR title." Same facts, different lede. MR: the
  bug. Commit: the changed behavior, then why it was necessary.

## Final scan

Read only the title and the first two headings. They must name the
user-visible problem and the after-state. If they name a function, rewrite.
Search contrast sentences for `now` / `no longer`. If a contrast relies on
tense alone, add the marker.
