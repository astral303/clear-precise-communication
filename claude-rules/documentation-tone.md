# Documentation tone

Engineering text describes. It does not sell, celebrate, reassure, or
editorialize.

## Scope

Every durable artifact: PR text, commit text, issues, changelogs, user docs,
ADRs, plans, design docs, reviewer guides, `///` and `//` comments, test names,
assertion messages, and user-facing copy. Comments and drafts are in scope.

This is not a README-only rule.

## Register

Name the thing, what it does, under what conditions, and what it does not do.
Use concrete nouns, real symbol names, and measured values.

The reader already has the code, the diff, or the product. They need to
understand it, not be persuaded that it is good.

Length signals importance. Padding makes a small change look like a large one.

## Claims the code must hold up

- Verify a completeness claim before writing it. "Holds every colour in the
  interface" and "covers all cases" are assertions to check by search, not
  framing to add for weight.
- State what a check, guard, or test does **not** cover, in the same place it
  is described.
- Prefer a named limitation over an omission: "written by hand, so it records
  what the stylesheets do today" beats silence about how the table is
  maintained.
- When documentation and implementation disagree, fix the implementation or
  narrow the claim. Do not leave prose that promises more than the code
  delivers.

Confident prose raises trust in code that may not deserve it. A README is a
contract.

## Banned praise and intensifiers

Do not write these, or close synonyms, about code, a change, a test, or a
design:

| Banned | Why it fails | Write instead |
| --- | --- | --- |
| elegant, robust, bulletproof, production-ready | Verdict, not description | The invariant, the failure mode, or the test that holds it |
| load-bearing, critical insight, key part, the important piece | Ranking dressed as description | What the code does, and what breaks if it is wrong |
| comprehensive, fully, carefully, extremely, significantly, seamless | Intensifier with no measurement | The count, the ratio, the named limitation, or delete |
| battle-tested, powerful, solid, well-structured | Sales | Observable behavior |
| it's worth noting, importantly, the key is | Throat-clearing | The fact, in the first sentence |
| this ensures / this guarantees (without a proof or test) | Unchecked safety claim | What happens on the failure path, with the message or test name |

Do not editorialize about the work's difficulty, cleverness, or thoroughness.
Do not congratulate the change. Do not tell the reader the approach is
obvious, natural, or the right one.

## Sentence shapes that are inflation in disguise

| Do not write | Write |
| --- | --- |
| "This is the load-bearing part of the renderer." | "Row height is computed here; a mismatch desyncs hit-testing." |
| "A robust fallback covers all remaining cases." | "Unknown providers return `None`. There is no size-limit path." |
| "The test suite comprehensively covers the feature." | "Tests cover empty input, one match, and a missing file. They do not cover concurrent writers." |
| "We carefully preserve ordering." | "When both halves of a curated pair remain, the first pass keeps declaration order." |

## Closed loopholes

- "I was being precise, not grandiose." If the word is a verdict (`robust`,
  `elegant`, `comprehensive`), it is inflation. Replace it with the condition.
- "The README should sell the tool." User docs still describe. Lead with what
  the reader can do, not with how good the tool is.
- "This comment is just explaining why the code is the way it is." That is
  rationale (keep) plus a verdict (cut). Keep the constraint; cut the praise.

## Final scan

Search the artifact for: `elegant`, `robust`, `comprehensive`, `carefully`,
`fully`, `powerful`, `seamless`, `load-bearing`, `bulletproof`, `ensures`,
`guarantees`, `importantly`, `worth noting`. Delete or replace each hit.
