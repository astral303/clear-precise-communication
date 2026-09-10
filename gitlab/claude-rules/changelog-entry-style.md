# Changelog entry style

A changelog reader wants to know what class of change this is, what was
broken, and what they can now do.

Area labels and neutral end-state phrasing answer none of those.

## Scope

`CHANGELOG` / `CHANGELOG.md` / release notes / `Unreleased` sections. Parent
bullets in an MR that will be copied into a changelog follow the same shape.

Project conventions take precedence when the repo already has a changelog
format. If grouping is unspecified, use the defaults below.

## Grouping

Group by change class, not by feature area:

- `### Enhancements`
- `### Fixes`
- `### Internal: …` for non-user-facing work (install, releases, refactors
  with no user-visible effect)

Headings are optional. The parent bullet, not the heading, carries the
summary. Single bullets with the rest indented under them are as good as a
subheading.

Mark non-user-facing groups `Internal:`.

## Parent bullet

The parent is a standalone summary — the sentence a reader can stop at.

| Do not write (bare label) | Write (standalone summary) |
| --- | --- |
| Tool runs in summary mode: | Improve collapsed tool rows in tools summary mode and add complete keyboard-only navigation |

## Fixes

Fixes lead with the verb and the symptom, not with the end state.

| Do not write (end state) | Write (verb + symptom) |
| --- | --- |
| `I` copies the session ID to the clipboard | Fix `I` copying the actual session ID |
| Codex runs show one row per call | Fix Codex runs showing one `Called 1 tool` row per call |

A small, one-condition fix is one or two lines stating what the user now
sees. Length signals importance. Do not spell the symptom out across three
lines when the after-state is the fact:

| Do not write | Write |
| --- | --- |
| Fix a tool result, call body or task report one line over its truncation limit hiding that line behind `(1 more lines...)` | Output with one line truncated now shows that line instead of `(1 more lines...)` |

## Silently absent behavior is a Fix

If the user would reasonably have expected the thing already ("why isn't X
there?"), the entry is a Fix: `Fix <thing> missing from <surfaces>.` then
what now shows. It is not an Enhancement, and the symptom is not a trailing
"Until now they were not read."

Decide fix-or-enhancement from the user's expectation, not from the plan's
heading. The MR title and "The bug" section use the same first sentence.

## One bullet per distinct behavior

When keys or surfaces share one behavior, one parent line names them all.
When a key's behavior differs, including fallbacks, it gets its own bullet.

Cut mechanism trivia the user cannot act on (gutter markers, internal metadata
field names) unless the user must know it to use the change. User-visible
symptom only in the parent; mechanism, if needed, as a sub-bullet. A
sub-bullet must add a fact the parent cannot carry, or it is cut.

## Verify against what shipped

When editing a changelog, verify each entry against what actually shipped
before rewording it. Do not only reorganize inherited entries. Do not invent
entries for work that did not land. Do not drop user-visible work that did.

US spelling unless the project uses otherwise (`colored`). Capitalize
`Markdown` as a proper name.

## Closed loopholes

- "I grouped by the module I edited." The reader groups by Enhancements /
  Fixes / Internal, not by your files.
- "The end state is more positive." A real bug still leads with the symptom.
  A one-condition fix may be the after-state, in one or two lines, because
  length signals importance.
- "Two keys do the same kind of thing, so four sub-bullets." If the behavior
  is the same, one line. Own bullets only when the behavior differs.
- "The plan filed it under Enhancements." The user's expectation decides
  the class, not the plan heading.

## Final scan

Read only the parent bullets. Each one must stand alone as a summary. Each
fix must start with a verb and a symptom. Confirm grouping is by change class.
See also `changelog-impact-claims.md`.
