# Second person only in product text

A changelog or a UI string speaks to the person using the software: "a shell
command **you** ran". A title, commit or MR description is a record an engineer
reads about a change, and it describes a third party: "a shell command **the
user** ran".

## Scope

| Person | Artifacts |
| --- | --- |
| Second (`you`, `your`) | Changelogs, release notes, README and user docs, UI copy, error and warning strings |
| Third (`the user`) | MR titles and descriptions, commit subjects and bodies, issues, ADRs, plans, design docs, reviewer guides, `///` and `//` comments, test names |

The same change, in both registers:

| Artifact | Write |
| --- | --- |
| Changelog | Fix a shell command you ran in Pi missing altogether in the default tools summary mode |
| MR title | Attribute a shell command user ran in Pi to the user, not to the model |
| Commit body | Exports render the user's call, as they already render the model's |

## The label is not the register

`You` is a string the product prints. Quoting it in a commit or an MR body
quotes the product; it does not address the reader. "opens a run under `You`"
is correct in a commit, and stays in backticks.

## Closed loopholes

- "The changelog and the MR describe one change, so they should read alike."
  Same facts, different readers. One ran the command; the other is reviewing
  the code that records it.
- "The title should match the changelog entry." It matches its facts, not its
  person.
- "Second person is warmer." A commit is a record. Nobody is being addressed.
- "I wrote the body to match my title." Then the title was wrong, or the body
  is. Fix the one that left its register.

## Final scan

Search the artifact for `you`, `your`. In a title, commit, MR body, issue or
comment, each hit is either a quoted product string — keep it — or the wrong
person, so rewrite it as `the user`. In a changelog or user doc, run it the
other way: `the user` becomes `you`.
