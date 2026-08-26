# Noun-phrase labels, not questions

Label a section the way an engineer labels a file: a noun phrase that names
the topic. Not a question. Not a presentation opener. Not a cleft.

Reference point: ASD-STE100 (Simplified Technical English) — plain declarative
labels, short sentences, no rhetorical questions, no talk-stage framing.

## Scope

Every durable artifact: MR headings, issue headings, changelog headings, README
headings, ADR headings, plan headings, design-doc headings, reviewer-guide
headings, commit-body headings, `///` doc comments, `//` comments, and any
other label that introduces a block of text.

**This is not a headings-only rule.** The banned construction is banned in
comments, doc comments, and sentences. Reading it as "MR headings only" is how
it was ignored on the second offence.

## Required shape

Use a noun phrase, or a short declarative sentence that states the fact:

| Write | Do not write |
| --- | --- |
| Rationale for leaving clippy warnings ignored | Why this does not also deny clippy warnings |
| Changes | What changed |
| Validation | How we tested this |
| Limitations | What this does not do |
| Curated pair ordering | Why the crop width is hardcoded |
| The agent's share of `message_count` | What the workspace filter narrows the list to |
| True when the handle is missing | Whether the handle is present |
| `None` when no filter is set | Where the filter lives |

## Banned openers

Do not start a heading, comment, or doc comment with:

- `Why …` (rhetorical or explanatory heading)
- `What …` (`What X does`, `What X holds`, `What X narrows to`, `What changed`)
- `Where …` (`Where X lives`, `Where X is stored`)
- `Whether …`
- `How …` as a heading (`How X works`, `How we …`)
- `Which …`

A procedure can still use numbered steps. The heading above those steps is
still a noun phrase: `Install`, `Verification`, not `How to install`.

## Banned cleft

Do not write `X is what keeps/lets/groups/does Y`. Write `X keeps/lets/groups Y.`

| Do not write | Write |
| --- | --- |
| The workspace filter is what narrows the list. | The workspace filter narrows the list. |
| This buffer is what keeps the fold state. | This buffer keeps the fold state. |

## Closed loopholes

- "The heading is friendlier as a question." User-facing docs still use noun
  phrases. Questions belong in an FAQ body, not as the label.
- "I was writing a field comment, not a heading." Field comments use the same
  shape: the fact, or `True when …` / `None when …`. Not `What the field …`.
- "What changed is standard in release notes." The heading is `Changes`. The
  bullets state the changes.
- "Why is the natural word for rationale." The heading is `Rationale` or
  `Rationale for X`. The body may contain because-clauses.

## Final scan

Search headings and comments for a leading `What `, `Where `, `Why `,
`Whether `, `How `, `Which `. Search sentences for ` is what `. Rewrite each
hit as a noun phrase or a short declarative.
