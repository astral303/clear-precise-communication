# Relay findings in reader terms

A finding you pass on — a review subagent's list, a relayed bug, a quoted
diagnostic — is your artifact. Rewrite each item before sending. Do not
forward the reviewer's compressed, symbol-first shorthand.

## Scope

Chat that relays a review, a PR comment that quotes a finding, a summary of
someone else's notes. The original reviewer's notes can stay dense; the text
the user reads cannot.

## Required shape

Open with the user-visible effect and the condition that triggers it, then
the mechanism, then the fix. Symbol names come after the effect, at most one
per sentence.

| Do not forward | Write |
| --- | --- |
| `` `stored_session_in` now runs `session_rows`, which sums `LENGTH(data)` on a keystroke `` | While typing an id that is not in the list, each keystroke scans the whole database. |

Where a finding says "before X, now Y", say which one is the bug and whether
it predates the branch. Verify a claim in the code first when the item
decides scope.

See `pr-text-leads-with-the-bug.md` and `name-the-type-not-a-nickname.md`.

## Closed loopholes

- "I am only forwarding." The relay is a new artifact. It follows these
  rules.
- "The reviewer was precise." Precision that opens with a function name is
  not readable. Rewrite.
- "There are twenty items, so compression is required." Twenty unread items
  are not shorter. Each item still leads with what the user sees.

## Final scan

Read each item as someone who did not open the diff. If the first clause is a
function name, rewrite.
