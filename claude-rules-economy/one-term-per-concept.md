# One term per concept, no synonyms

Use one term for one concept across title, body, commit, changelog, README,
and comments. Do not swap a synonym for variety or to fit a line. Every extra
term makes the reader check whether it is the same thing.

Pick the term once. Define it at first use if needed. Reuse it verbatim.

| Same concept (cut) | One term |
| --- | --- |
| calls issued together / interleaved calls / alternate | interleaved calls |
| parallel batch (as another name for that group) | batch — the group noun |
| not read / unread / ignored | the word the UI already uses |

A group noun is a second concept, not a synonym. "A batch of interleaved
calls" is two terms for two concepts. "Parallel batch" still renames the
calls.

An inexact synonym narrows or collides (`alternate` vs alternate screen).
Closeness is not sameness. Repeat the term; variety is the defect. Shorten a
title without renaming the concept. Do not grep away a group noun or
identifier as if it were a synonym.
