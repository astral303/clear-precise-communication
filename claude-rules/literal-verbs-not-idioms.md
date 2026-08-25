# Literal verbs, not idioms

Write the operation, not an idiom for it. Durable text is in a technical
register, never the conversational one.

The reader should not have to translate "go with it" into "deleted and counted".

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

In test names: `delete_removes_every_subagent_thread…`, not `delete_takes_…`.

## Failure mode

"Go with", "went", "takes" describe the effect by analogy. The reader has to
map the analogy onto the actual operations (delete, count, include). The
replacement names those operations in the words the software uses.

## Closed loopholes

- "It's a comment, conversational tone is fine." Durable text is technical.
  Comments use the same verbs as the changelog.
- "Takes is a normal English word." Not as a substitute for delete, remove, or
  count. If the code `delete`s, write `delete`.
- "The README already says 'go with' in an old paragraph." Do not spread it.
  Fix it when that paragraph is next edited. Do not add new occurrences.

## Final scan

Before sending user-facing or durable text, search the new text for:

`go with`, `goes with`, `went`, `takes`, `took`, `goes`

used as a stand-in for delete, remove, count, or include — identifiers
included. Replace each hit with the literal verb.
