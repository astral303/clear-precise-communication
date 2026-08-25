# Literal verbs, not idioms

Write the operation, not an idiom for it. Durable text is in a technical
register, never the conversational one.

The reader should not have to translate "go with it" into "deleted and counted",
or "says how many" into "reports the count".

## Scope

Changelogs, user docs, `///` and `//` comments, test names, assertion
messages, panic and error strings, PR bodies, commit messages, and any other
durable text.

This is not a changelog-only rule. If the idiom reached a comment or a test
name, the rule was already ignored.

## Required shape

Name the operation with the verb the software uses or the verb that is the
operation:

| Idiom (cut) | Literal (write) |
| --- | --- |
| go with it / goes with the parent | deleted with the parent / removed with the parent |
| how many went | how many were deleted / the count `--delete` prints |
| takes the subagent threads | deletes the subagent threads / removes the subagent threads |
| went / took / goes / takes (as a stand-in for delete, remove, count, include) | deleted, removed, counted, included |
| they now go with it, and `--delete` says how many went | They are now also deleted and included in the count `--delete` prints |
| the command / warning / UI *says* or *tells* | *reports*, *prints*, *shows* |
| a list *says* | the list *shows* |
| a term *says* / *tells you what* | the term *names* |
| Say how many X were ignored | Report how many X were ignored |
| name how many | report the count / show the count |

The software does not speak. A list shows, a warning or command reports, a
term names. Never *says*, *tells*, or *name how many*.

In test names: `delete_removes_every_subagent_thread…`, not `delete_takes_…`.
`report_ignored_session_count…`, not `say_how_many_were_ignored…`.

## Failure mode

"Go with", "went", "takes" describe the effect by analogy. "Says" and "tells"
personify output. The reader has to map the analogy onto the actual operations
(delete, count, include, print, report, show, name). The replacement uses
those verbs.

## Closed loopholes

- "It's a comment, conversational tone is fine." Durable text is technical.
  Comments use the same verbs as the changelog.
- "Takes is a normal English word." Not as a substitute for delete, remove, or
  count. If the code `delete`s, write `delete`.
- "Say is a normal English word." Not as a substitute for show, report, print,
  or name when the subject is the software. A PR title, changelog, or doc
  comment that "says how many" is in violation.
- "The README already says 'go with' in an old paragraph." Do not spread it.
  Fix it when that paragraph is next edited. Do not add new occurrences.

## Final scan

Before sending user-facing or durable text, search the new text for:

`go with`, `goes with`, `went`, `takes`, `took`, `goes`

used as a stand-in for delete, remove, count, or include, and

`say`, `says`, `said`, `tell`, `tells`, `name how many`

used for software output — identifiers, titles, and doc comments included.
Replace each hit with the literal verb.
