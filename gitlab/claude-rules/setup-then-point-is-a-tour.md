# Setup then point is a tour

A title or opening that walks setup → symptom → twist is a tour. The reader
scans for what was frozen and what now happens. State that first. The last
sentence must not be the point.

This is not a search-index rule. Any bug described in diagnosis order is
the same shape.

## Scope

MR titles and descriptions, changelog parent bullets,
commit bodies that state a defect, and the first paragraph of "The bug" /
"The change". See `mr-text-leads-with-the-bug.md`.

## Required shape

Title: the frozen thing the user saw, then the change in parentheses or
after a colon. First sentence of the body: the bug as they saw it. Second:
what now happens. Mechanism goes under Cause, or out.

| Tour (cut) | Point first (write) |
| --- | --- |
| Let repeated runs fill the index instead of reporting the same count | Fix search never indexing new sessions (catch up a couple of seconds before the reply) |
| Until now, a corpus that had outgrown the index reported the same warning, with the same missing count, until a manual cache command. The search indexed nothing itself. | Search never updated the index. New sessions stayed missing and the same warning appeared every run. Search now spends a couple of seconds catching up before it answers. |
| A pasted ID was recognized as an ID, so the list emptied and reported not found, although the session was there | An uppercase session ID was reported as not found even though the session exists |

## Banned openings

| Construction | Why it fails |
| --- | --- |
| `Let X …` | Permission to the code, not the user-visible miss |
| `Until now, …` | A story opening. The heading already marks the old world |
| `… instead of Y` as the title's twist | Y is the bug. It belongs first, not in a trailing clause |
| `… although Z` | Z is the bug, parked in a subordinate clause |
| A "The change" paragraph that is only the old world | That paragraph is **The bug**. The change is what happens now |
| Personification (`the corpus outgrew the index`) | New sessions were not in the index |
| A diagnostic count (`the same missing count`) | Same class as seven columns. The user saw the warning again |

## Closed loopholes

- "I described the pipeline accurately." Accuracy in diagnosis order is
  still a tour. State the frozen thing, then the after-state.
- "Let is a normal verb." Not as the title's first word. The user did not
  grant the code permission. They hit a miss.
- "The last sentence summarizes." If deleting everything before it leaves
  the bug, you buried the lede. Promote that sentence.
- "Until now is how changelogs mark the old behavior." The heading **The
  bug** already does that. See `changelog-entry-style.md` for silently
  absent Fixes.

## Final scan

Read only the title and the first two sentences. They must name the
user-visible miss and the after-state. If the point is in `instead of`,
`although`, or the last sentence of a setup chain, rewrite. Search for
`Let `, `Until now`, `instead of`, `although `.
