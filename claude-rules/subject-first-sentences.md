# Subject-first sentences

Start with the noun the sentence is about, then the verb. Do not open with a
fronted relative clause that elides the noun.

A comment is read cold. The reader should not have to hold an elided noun and
a relative clause before the verb arrives.

## Scope

Every durable artifact: `///` and `//` comments, user docs, changelogs, PR
bodies, commit messages, issues, and chat that states a fact. This is not a
comment-only rule.

## Required shape

| Do not write | Write |
| --- | --- |
| One the format does not recognize contributes nothing. | Unrecognized formats do not contribute any transcripts. |
| one whose directory cannot be read has none either | An unreadable directory is reported and yields none. |
| One that fails to parse is skipped. | A parse failure is skipped. |

Banned openers: `One that…`, `One the…`, `one whose…`, `One whose…`.

See also `noun-phrase-labels-not-questions.md` (no What/Where/Why openers)
and `no-rhetorical-appositives.md` (do not delay the verb behind a catalogue).

## Closed loopholes

- "The antecedent is in the previous sentence." A comment or bullet is often
  read alone. Repeat the noun.
- "It is shorter." Eliding the noun is not shorter for the reader. It is a
  hold.
- "I only grepped What/Where/Why." Those are a different opener. Scan for
  `One that` / `One the` / `one whose` as a separate read.

## Final scan

Search comments and new prose for `One that`, `One the`, `one whose`. Rewrite
each hit as noun, then verb.
