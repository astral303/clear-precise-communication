# Changelog entry style

A changelog reader wants to know what class of change this is, what was
broken, and what they can now do.

Area labels and neutral end-state phrasing answer none of those.

## Scope

`CHANGELOG` / `CHANGELOG.md` / release notes / `Unreleased` sections. Parent
bullets in a PR that will be copied into a changelog follow the same shape.

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

## One bullet per behavior

Do not compress two keys or two behaviors into one clause. One bullet per key,
with its full behavior, including fallbacks.

Cut mechanism trivia the user cannot act on (gutter markers, internal metadata
field names) unless the user must know it to use the change. User-visible
symptom only in the parent; mechanism, if needed, as a sub-bullet.

## Verify against what shipped

When editing a changelog, verify each entry against what actually shipped
before rewording it. Do not only reorganize inherited entries. Do not invent
entries for work that did not land. Do not drop user-visible work that did.

US spelling unless the project uses otherwise (`colored`). Capitalize
`Markdown` as a proper name.

## Closed loopholes

- "I grouped by the module I edited." The reader groups by Enhancements /
  Fixes / Internal, not by your files.
- "The end state is more positive." The reader needs the symptom that was
  wrong. Verb + symptom.
- "Two keys do the same kind of thing, so one bullet." Each key gets its own
  bullet if its behavior differs, including fallbacks.

## Final scan

Read only the parent bullets. Each one must stand alone as a summary. Each
fix must start with a verb and a symptom. Confirm grouping is by change class.
See also `changelog-impact-claims.md`.
