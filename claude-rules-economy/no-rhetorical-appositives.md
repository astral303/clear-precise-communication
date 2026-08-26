# No rhetorical appositives

`Wrapped text — a reply, a result, a shell command — now reflows…` announces
a category, pauses, illustrates, then delivers the verb. The `a …, a …, a …`
is pulpit rhythm. Neither belongs in a changelog, MR, commit, or doc sentence.

This does not ban the em-dash. It bans using the dash as stage directions:
pause, enumerate, resume.

Test: delete the dashed phrase. If the subject turns vague, those words were
the subject. Put them before the verb: "Wrapped replies, results, and shell
commands no longer …"

An em-dash is fine when it defines or contrasts **one** thing:

> Wrapped lines no longer run under the timestamp — wrap width now excludes
> that column.

A sub-bullet must add a fact the parent cannot carry, or it is cut. Restating
the parent as mechanism is not an added fact. This construction is caught by a
read, not a grep for `—`.
