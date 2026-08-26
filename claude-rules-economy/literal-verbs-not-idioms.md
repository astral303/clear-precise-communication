# Literal verbs, not idioms

Write the operation, not an idiom for it. Durable text is technical, including
comments and test names. The software does not speak.

| Idiom (cut) | Literal (write) |
| --- | --- |
| go with it / goes with the parent | deleted / removed with the parent |
| how many went | how many were deleted / the count `--delete` prints |
| takes / took / goes / went (for delete, remove, count, include) | deleted, removed, counted, included |
| the command / warning / UI *says* or *tells* | *reports*, *prints*, *shows* |
| a list *says* | the list *shows* |
| a term *says* | the term *names* |
| Say how many X were ignored | Report how many X were ignored |
| name how many | report the count / show the count |

Test names: `delete_removes_every_subagent_thread…`, not `delete_takes_…`.
`report_ignored_session_count…`, not `say_how_many_were_ignored…`.

`Takes` and `say` are normal English. They are still banned as stand-ins for
delete/remove/count or for software output. Do not add new occurrences of an
old idiom; fix inherited ones when that paragraph is next edited.
