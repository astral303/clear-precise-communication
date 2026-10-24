# Second person only when addressing the operator

`you` addresses the person operating the product. A record of a change
describes that person as `the user`. Changelogs and release notes are
records.

## Where each person goes

| Person | Artifacts |
| --- | --- |
| Second (`you`, `your`) | README and other user docs, UI copy, error and warning strings |
| Third (`the user`) | Changelogs, release notes, MR titles and descriptions, commit subjects and bodies, issues, ADRs, plans, design docs, reviewer guides, `///` and `//` comments, test names |

The same change:

| Artifact | Write |
| --- | --- |
| Changelog | Fix a shell command the user ran in Pi missing from the default tools summary |
| README | The installer asks you to confirm before it writes |
| MR title | Attribute a shell command the user ran in Pi to the user, not to the model |

## The label is not the register

`You` is a string the product prints. Quoting it in a commit, a changelog,
or an MR body quotes the product; it does not address the reader. "opens a
run under `You`" stays in backticks.

## Closed loopholes

- "The changelog speaks to the person who upgrades." They are reading a
  record. Write `the user`.
- "The title should match the changelog's wording." It matches the facts.
  Both use `the user`. A README step that addresses the operator uses `you`.
- "Second person is warmer." A commit, a pull request, and a changelog are
  records. Nobody is being addressed.
- "I wrote the body to match my title." Then the title was wrong, or the body
  is. Fix the one that left its register.

## Final scan

Search for `you` and `your`. In a changelog, release note, title, commit,
MR body, issue, or comment, each hit is either a quoted product string or
the wrong person. Rewrite the wrong person as `the user`. In a README or
other user doc, a sentence that addresses the reader uses `you`.
