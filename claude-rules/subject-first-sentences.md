# Subject-first sentences

Do not park a fact in a relative clause. Start with the noun the sentence is
about, then the verb.

Delete the relative. If a fact leaves with it, the relative was the sentence:
write it as noun, then verb.

A comment is read cold. The reader should not have to hold a noun and a
relative before the verb arrives, or hold one noun while a different noun
inside the relative verbs.

## Scope

Every durable artifact: `///` and `//` comments, user docs, changelogs, PR
bodies, commit messages, issues, and chat that states a fact. This is not a
comment-only rule.

## Required shape

The noun the fact is about is the subject of the verb.

| Do not write | Write |
| --- | --- |
| One the format does not recognize contributes nothing. | Unrecognized formats do not contribute any transcripts. |
| one whose directory cannot be read has none either | An unreadable directory is reported and yields none. |
| One that fails to parse is skipped. | A parse failure is skipped. |
| directories, for which the listing does not include stat info | A directory listing does not include stat info. |
| Add FLAG, which only requests stat with each directory listing | Add FLAG to request stat with each directory listing. |

`One that…`, `One the…`, `one whose…` are dummy-head openers. `, for which `
parks the fact mid-sentence and often gives the relative a different subject.
`, which` plus the payload (`which only requests…`) is the same hold with the
same noun. `for which` is also legal register; drop it.

See also `noun-phrase-labels-not-questions.md` (no What/Where/Why openers)
and `no-rhetorical-appositives.md` (do not delay the verb behind a catalogue).

## Closed loopholes

- "The antecedent is in the previous sentence." A comment or bullet is often
  read alone. Repeat the noun.
- "It is shorter." Eliding the noun is not shorter for the reader. It is a
  hold. Parking the fact in `, for which` is the same hold.
- "I only grepped What/Where/Why." Those are a different opener. Scan for
  `One that` / `One the` / `one whose` as a separate read.
- "I grepped `One that` / `one whose`." Those are one spelling. Search
  `, for which ` as a separate read. The delete-the-relative test catches
  payload `, which` that grep will miss.
- "Every `that` / `which` is this rule." Delete the relative. If the sentence
  still states the fact, the relative was a modifier. If a fact left, rewrite
  that fact as noun then verb. Do not grep `that will`.

## Final scan

Search comments and new prose for `One that`, `One the`, `one whose`,
`, for which `. Rewrite each hit as noun, then verb. For any other relative:
delete it; if a fact leaves, rewrite that fact as its own declaration.
