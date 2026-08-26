# Final scan before sending

"I didn't notice while writing the sentence" is a process failure. The scan
is the process. Run it on the artifact you are about to send — MR
description, comment, changelog entry, README sentence, doc comment — not on a
later
revision.

This is not optional and not a skill invocation.

## 1. Read only the skeleton

Title, headings, and the first sentence of each section.

- They name the user-visible problem or effect, the after-state, and the next
  action when one is needed.
- Headings are noun phrases: `Changes`, `Rationale for X`, `Validation`.
- Not questions. Not `What` / `Where` / `Why` / `Whether` / `How` / `Which`
  openers.

If the skeleton is a function name, a file list, or a recap, rewrite before
reading the rest.

## 2. Check the data shape

- Parallel facts → bullets, one fact each. If you wrote a paragraph, convert
  it now.
- Grid (key × behavior, name → tool → input) → table. If you wrote a sentence
  with two em-dashes, convert it now.
- No paragraph or sub-bullet that restates the bullet above it. A child
  bullet must add a fact the parent cannot carry, or it is cut.
- No rhetorical appositive: `X — a …, a …, a … — verb`. The examples are
  the subject; put them before the verb. See
  `no-rhetorical-appositives.md`.
- Tests sections name groups, not every case.

## 3. Search the text

Search the artifact (and the diff, for comments and test names) for:

| Pattern | Action |
| --- | --- |
| `What `, `Where `, `Why `, `Whether `, `How `, `Which ` at the start of a heading or comment | Noun phrase or short declarative |
| ` is what ` | Cleft: rewrite as `X verbs Y` |
| `go with`, `goes with`, `went`, `takes`, `took`, `goes` as stand-ins for delete/remove/count/include | Literal verb |
| `say`, `says`, `said`, `tell`, `tells`, `name how many` for software output | *shows* / *reports* / *prints* / *names* |
| `elegant`, `robust`, `comprehensive`, `carefully`, `fully`, `powerful`, `seamless`, `load-bearing`, `bulletproof` | Delete or replace with the condition |
| `ensures`, `guarantees`, `importantly`, `worth noting` | Delete or replace with the observable |
| `always`, `never`, `only`, `everything else`, `no matter what`, `mechanical`, `low risk`, `can't regress`, `safe` in reviewer-facing text | Condition, depth, or deletion |
| `now` / `no longer` missing from old-vs-new contrasts | Add the marker |
| raw seconds, unreproducible counts, "it works as expected" | Ratio, percentage, or cut |
| branch names, `worth doing`, `plans/`, `MR A`, timings in an MR description | Cut |

## 4. One term per concept

Name the term you picked for each concept in this change. Search the title,
body, commit text, changelog, README, and touched comments for every other
phrasing. Replace those hits. Two names for one thing is a defect even when
both are accurate.

## 5. Usefulness pass

For each sentence in user docs and comments: what does the reader do
differently for having read it? If they would learn it by doing the thing, or
by reading the next line of code, delete it.

## 6. Closed-excuse check

If you are about to send because "it's good enough and I can clean structure
later", stop. Structure it now. If you are about to send because "this is only
a comment / only a changelog / only a test name", stop. Those are in scope.

If you searched for the step 3 patterns and are about to send, you have not
scanned. Steps 1, 2, 4 and 5 are reads, not searches: a keyword pass skips the
skeleton, the sub-bullet that restates its parent, the second term for one
concept, and the usefulness test. It also cannot catch a count the product
does not print, or a completeness claim (`at any window width`, `every row`)
that is not on the banned-word list. Sending the artifact in the same batch
as code edits is not a reason to skip them.

## Done when

A reader who sees only the title, headings, and first sentences can recover
the point after interruption. Steps 1–6 have all been run. A grep of the
step 3 patterns returning clean is not sufficient (for example `always` in
`always-on` as a filename, or `takes` in `takes about 4x` as a ratio, can
stay; a grepless restating child bullet cannot).
