# Noun-phrase labels, not questions

Label a section the way an engineer labels a file: a noun phrase. Not a
question, presentation opener, or cleft. Applies to headings **and** comments,
doc comments, and sentences. ASD-STE100: plain declarative labels.

| Write | Do not write |
| --- | --- |
| Rationale for leaving clippy warnings ignored | Why this does not also deny clippy warnings |
| Changes | What changed |
| Validation | How we tested this |
| The agent's share of `message_count` | What the workspace filter narrows the list to |
| True when the handle is missing | Whether the handle is present |
| `None` when no filter is set | Where the filter lives |

Banned openers on headings and comments: `Why …`, `What …`, `Where …`,
`Whether …`, `How …`, `Which …`. A procedure still uses numbered steps; the
heading is `Install`, not `How to install`.

Banned cleft: `X is what keeps/lets/groups Y` → `X keeps/lets/groups Y.`

Field comments use the fact, or `True when …` / `None when …`, not
`What the field …`. The heading for because-clauses is `Rationale for X`.
