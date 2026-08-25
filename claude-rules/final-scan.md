# Final scan before sending

"I didn't notice while writing the sentence" is a process failure. The scan
is the process. Run it on the artifact you are about to send — PR body,
comment, changelog entry, README sentence, doc comment — not on a later
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
- No paragraph that restates the bullet above it.
- Tests sections name groups, not every case.

## 3. Search the text

Search the artifact (and the diff, for comments and test names) for:

| Pattern | Action |
| --- | --- |
| `What `, `Where `, `Why `, `Whether `, `How `, `Which ` at the start of a heading or comment | Noun phrase or short declarative |
| ` is what ` | Cleft: rewrite as `X verbs Y` |
| `go with`, `goes with`, `went`, `takes`, `took`, `goes` as stand-ins for delete/remove/count/include | Literal verb |
| `elegant`, `robust`, `comprehensive`, `carefully`, `fully`, `powerful`, `seamless`, `load-bearing`, `bulletproof` | Delete or replace with the condition |
| `ensures`, `guarantees`, `importantly`, `worth noting` | Delete or replace with the observable |
| `always`, `never`, `only`, `everything else`, `no matter what`, `mechanical`, `low risk`, `can't regress`, `safe` in reviewer-facing text | Condition, depth, or deletion |
| `now` / `no longer` missing from old-vs-new contrasts | Add the marker |
| raw seconds, unreproducible counts, "it works as expected" | Ratio, percentage, or cut |
| branch names, `worth doing`, `plans/`, `PR A`, timings in a PR body | Cut |

## 4. Usefulness pass

For each sentence in user docs and comments: what does the reader do
differently for having read it? If they would learn it by doing the thing, or
by reading the next line of code, delete it.

## 5. Closed-excuse check

If you are about to send because "it's good enough and I can clean structure
later", stop. Structure it now. If you are about to send because "this is only
a comment / only a changelog / only a test name", stop. Those are in scope.

## Done when

A reader who sees only the title, headings, and first sentences can recover
the point after interruption. A grep of the banned patterns returns nothing
you cannot justify as a literal (for example `always` in `always-on` as a
filename, or `takes` in `takes about 4x` as a ratio).
