# Changelog impact claims

A changelog reader wants to know whether this change helps **them**, and what
it costs them once. A ratio transfers to their machine. Raw seconds and raw
counts do not. Neither does a statistic the tool never prints.

Every line spent asserting that the feature works correctly, or describing a
branch nobody reaches, pushes the facts that matter further down.

## Scope

Performance entries, migration-cost entries, and any changelog or MR sentence
that claims impact, speed, size, or correctness. User docs that cite
benchmarks follow the same rules.

## Parent bullet

Write the parent as: verb, symptom or effect, ratio, parenthetical scope —
nothing else. Mechanism is a sub-bullet. The parent carries impact only.

| Do not write | Write |
| --- | --- |
| a warm agent search over 1,282 rollouts went from 8.5 to 3.3 seconds | about 2.6x faster (on one example corpus) |
| Migration cost in seconds | takes about 4x a normal load, once |

Do not bury the ratio behind the mechanism or behind a long corpus qualifier.
The number (the ratio) comes first; the qualifier is in parentheses.

## Counts the reader cannot reproduce

Do not publish a raw count the product does not surface. A **percentage** they
can compare against their own corpus is fine; "991 of 1,282 were such threads"
is not, if nothing in the tool prints that count.

State who gains little in the same place you state who gains most:

> Codex writes one transcript per sub-agent thread, so a workflow that spawns
> many agents gains the most. The example corpus was 77% such threads; one
> without them gains little.

## Correctness theater

Do not write that the feature works as expected. If it did not, the software
would be broken; that is not changelog material.

| Cut | Why |
| --- | --- |
| "The record lasts as long as the transcript's size and modification time do, so a session that gains content is read again" | Restating that the cache is not stale forever. Expected behavior. |
| "A transcript that could not be read is retried on the next load" | Only notable if it is new. Failed reads that already retried stay out. |
| "one skipped for exceeding a provider's size limit" | If no provider exposes that limit, the path is unreachable. Do not document it. |

For each remaining line ask: is it new, can a user reach it, and can they act
on it? Cut it otherwise.

Do not name a specific cause you cannot verify from the repo. Give the
mechanism you can verify.

## Closed loopholes

- "The raw timing makes it concrete." It makes it about your machine. A ratio
  plus parenthetical scope is what transfers.
- "I should mention the cache still invalidates, so people aren't scared."
  That is reassurance, not information. Cut. See `documentation-tone.md`.
- "The unreachable branch is documented so future us doesn't reintroduce it."
  That belongs in a test or a comment on the `None` return, not in the
  changelog.

## Final scan

Parent bullet: verb, effect, ratio, scope in parentheses. No raw seconds. No
counts the tool cannot print. No sentence whose claim is "it works". No path
the user cannot reach. Who gains little sits next to who gains most.
