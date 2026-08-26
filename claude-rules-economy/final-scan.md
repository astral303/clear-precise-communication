# Final scan before sending

Run this on the artifact you are about to send. Not on a later revision. A
keyword pass is not the scan. Shipping the artifact in a batch of code edits
is not a reason to skip it.

## 1. Skeleton

Title, headings, and the first sentence of each section name the user-visible
problem or effect, the after-state, and the next action when one is needed.
Headings are noun phrases (`Changes`, `Rationale for X`), not questions or
What/Where/Why/Whether/How/Which openers.

## 2. Data shape

- Parallel facts → bullets, one fact each.
- Grid → table. A sentence with two em-dashes is not a table.
- A child bullet must add a fact the parent cannot carry, or it is cut.
- No rhetorical appositive: `X — a …, a …, a … — verb`. See
  `no-rhetorical-appositives.md`.
- Tests sections name groups, not every case.

## 3. Search

Search the artifact (and the diff, for comments and test names):

| Pattern | Action |
| --- | --- |
| `What `, `Where `, `Why `, `Whether `, `How `, `Which ` at the start of a heading or comment | Noun phrase or short declarative |
| ` is what ` | `X verbs Y` |
| `go with`, `goes with`, `went`, `takes`, `took`, `goes` for delete/remove/count/include | Literal verb |
| `say`, `says`, `said`, `tell`, `tells`, `name how many` for software output | *shows* / *reports* / *prints* / *names* |
| `elegant`, `robust`, `comprehensive`, `carefully`, `fully`, `powerful`, `seamless`, `load-bearing`, `bulletproof` | Condition or delete |
| `ensures`, `guarantees`, `importantly`, `worth noting` | Observable or delete |
| `always`, `never`, `only`, `everything else`, `no matter what`, `mechanical`, `low risk`, `can't regress`, `safe` in reviewer-facing text | Condition, depth, or delete |
| `now` / `no longer` missing from old-vs-new contrasts | Add the marker |
| raw seconds, unreproducible counts, "it works as expected" | Ratio, percentage, or cut |
| branch names, `worth doing`, `plans/`, `MR A`, timings in an MR description | Cut |

A grep cannot catch a count the product does not print, or a completeness
claim (`at any window width`, `every row`) that is not on this list. Read for
those.

## 4. One term per concept

Name the chosen term. Search title, body, commit, changelog, README, and
touched comments for every other phrasing. Replace those hits.

## 5. Usefulness

For each sentence in docs and comments: what does the reader do differently
for having read it? If they would learn it by doing the thing, or by reading
the next line of code, delete it.

## 6. Closed-excuse check

If you are about to send because it is "only a comment / changelog / test
name", stop. Those are in scope. If you only ran step 3, you have not scanned.

## Done when

Steps 1–6 have all been run. A clean grep is not sufficient.
