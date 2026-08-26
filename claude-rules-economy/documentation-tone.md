# Documentation tone

Engineering text describes. It does not sell, celebrate, reassure, or
editorialize. Comments, drafts, and test names are in scope.

Name the thing, what it does, under what conditions, and what it does not do.
The reader already has the code. Length signals importance; padding misleads.

## Claims the code must hold up

- Verify a completeness claim by search before writing it.
- State what a check, guard, or test does **not** cover, in the same place.
- Prefer a named limitation over an omission.
- When docs and implementation disagree, fix the code or narrow the claim.

A README is a contract.

## Banned praise and intensifiers

Do not write these, or close synonyms, about code, a change, a test, or a
design:

| Banned | Write instead |
| --- | --- |
| elegant, robust, bulletproof, production-ready | The invariant, failure mode, or test |
| load-bearing, critical insight, key part | What it does, and what breaks if it is wrong |
| comprehensive, fully, carefully, extremely, significantly, seamless | The count, the ratio, the named limitation, or delete |
| battle-tested, powerful, solid | Observable behavior |
| it's worth noting, importantly, the key is | The fact, in the first sentence |
| this ensures / this guarantees (without a proof or test) | What happens on the failure path |

Do not editorialize about difficulty, cleverness, or thoroughness.

| Do not write | Write |
| --- | --- |
| "A robust fallback covers all remaining cases." | "Unknown providers return `None`. There is no size-limit path." |
| "The test suite comprehensively covers the feature." | "Tests cover empty input, one match, and a missing file. They do not cover concurrent writers." |

A verdict word (`robust`, `elegant`, `comprehensive`) is inflation even when
you meant to be precise. User docs still describe; they do not sell.
