# Changelog impact claims

A ratio transfers to the reader's machine. Raw seconds and raw counts do not.
Neither does a statistic the tool never prints. Applies to performance and
size claims in changelogs, MRs, and user docs.

Parent bullet: verb, symptom or effect, ratio, parenthetical scope. Mechanism
is a sub-bullet.

| Do not write | Write |
| --- | --- |
| a warm search over 1,282 rollouts went from 8.5 to 3.3 seconds | about 2.6x faster (on one example corpus) |
| Migration cost in seconds | takes about 4x a normal load, once |

The ratio comes first; the qualifier is in parentheses. A percentage the
reader can compare to their own corpus is fine; a raw count the product does
not print is not. State who gains little next to who gains most.

Do not write that the feature works as expected. For each remaining line: is
it new, can a user reach it, can they act on it? Cut it otherwise. Do not
name a cause you cannot verify from the repo.

"Seven columns" and "at any window width" are this rule: a layout constant or
a completeness claim the UI does not print.
