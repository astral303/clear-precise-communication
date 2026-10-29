# Notes on evolving the writing rules (maintainer notes — never loaded)

Not rules. These files exist for the human maintaining `claude-rules/`;
agents follow the rules, they do not update them.

## Early polarity (the family behind `negate-the-verb.md`)

The negative fact must reach the reader before the positive-sounding
verb makes them build its object. Known shapes:

| Shape | Status |
| --- | --- |
| postverb `no <noun>` ("found no other event") | covered by `negate-the-verb.md` |
| "fails to find" / "saves without checking" | no rule yet; write one if it starts failing |
| conditions trailed by `unless` | already ordered by `no-premise-so-consequence.md` |
| `supports only X` vs `only supports X` | scope attachment, not polarity timing — different principle |

## Authoring discipline that has repeatedly mattered

- One rule file per rewrite, named for the rewrite ("negate the verb",
  "literal verbs", "subject first"). Family concepts ("early polarity")
  live as the *why* inside the named rule, never as a vague umbrella
  file — vague directives invite reasoning where a rewrite was wanted.
- Restate a rule in short form + point at the file; pointers alone go
  unheeded when the sibling file isn't loaded.
- No meta-guidance about rule evolution inside loaded rule files.
