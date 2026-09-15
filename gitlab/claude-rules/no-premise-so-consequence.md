# No premise-so-consequence

A comment (or a changelog/PR sentence that states behavior) is an
**instruction**: when to act, in the imperative, in execution order. It is
not a proof. Do not open with a general truth about the system and *so*
the behavior.

The prestige prior is mathematical English: lemma → corollary. `needs no
write` is `admits no nontrivial solution`. `read anew` is the monograph
adverb. `A shard holds its sessions' text, so only…` is `Since a shard
holds…, it follows that only…`. The mirrored second sentence is the
`Conversely,` that closes a biconditional. That register loses. The
instruction wins.

Theorem prose exists so the reader can check each inference. A comment's
reader is not verifying a proof. They trust the code and need to act.
A lemma-and-corollary assigns them a job they did not come to do. That
is the mental gymnastics — not mere parse cost.

## Scope

`///` and `//` comments first. The same shape is banned in changelog
parent bullets, PR "The bug" / MR description sentences, and commit bodies
that explain a branch. Reasons, if they must appear, go after the rule as
a subordinate clause — not as the premise.

## Required shape

Lead with the rule. Execution order. Imperative or a plain when-clause.

| Derived (cut) | Stated (write) |
| --- | --- |
| A shard holds its sessions' text, so only a shard holding a session read anew, newly recorded as empty, or removed from disk is rewritten. | Rewrite a shard only if one of its sessions was reread, recorded empty, or deleted. |
| A restored entry equals the one on disk, so its shard needs no write. | If the restored session matches disk, skip the write. |

If you catch yourself deriving the behavior from how the system *is*,
delete the premise and state the behavior.

## Banned constructions

These are the prestige-register tells, not a poetry ban:

| Construction | Why it fails | Write |
| --- | --- | --- |
| `X, so Y` where X is a general truth about the system | `Since X, it follows that Y.` | Y. Optionally `Y, because X` after. |
| `needs no ___` | `admits no nontrivial solution` | `do not ___` / `skip the ___` |
| `anew` | Monograph adverb | `again` / `reread` |
| `alone suffices` | Maxim | the action that is enough |
| Two sentences that mirror each other (`A, so B` / `C, so not-B`) | `Conversely,` on a biconditional | One rule, then the exception if needed |

`so` after a real consequence is fine: "retry so the error is visible."
`so` after ontology is not: "a shard holds text, so…"

## Closed loopholes

- "It sounded precise / complete / good." That is the prestige prior
  dressing itself as taste. State the rule.
- "The so-clause lets the reader check why." They did not come to verify
  an inference. They came to act.
- "The first sentence is the reason the second is true." Then the second
  sentence *is* the comment. Keep it. Delete the first, or demote it to
  `because` after the rule.
- "Comments should explain why." Why is a subordinate clause on the rule,
  not a premise that earns the rule. See `comments-earn-their-place.md`.
- "I was avoiding repetition of *write*." Repeat the verb. Variety produced
  `needs no write`.

## Final scan

Read each comment as an instruction. If the first clause is how the world
is, and `so` delivers what the code does, delete the premise. Search for
`anew`, `needs no`, `suffices`, and a `so` that follows a general truth.
