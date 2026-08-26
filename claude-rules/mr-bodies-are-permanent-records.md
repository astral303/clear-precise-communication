# MR descriptions are permanent records

A merge request description is a permanent record read by people with no
access to the author's machine, the author's other branches, or the author's
plan files.

Keep out working-tree state, other agents' branches, wall-clock timings, and
any sentence that tells the reader when or how to do a follow-up.

## Scope

Merge request descriptions, issue bodies that describe a change, and commit
bodies. Chat announcements may mention a non-default target branch (see
below). The MR description still does not.

## Content that belongs

Facts about the change: user-visible effect, cause, fix, structural reason for
scope limits, named validation.

A scope reason must be structural: "clearing them edits Rust code, which is
outside the scope of this change." Not situational: "worth doing once the
concurrent work lands."

## Content that does not belong

| Cut | Why |
| --- | --- |
| Which other branches are being edited | No archaeological value. The next reader cannot see that machine. |
| Timings measured on the author's hardware | A later reader cannot reproduce the wall clock. Ratios belong in the changelog; see `changelog-impact-claims.md`. |
| Advice to the reader ("worth doing as its own branch once…") | An MR is not a coaching note. |
| Plan-internal names: `MR A`, `MR-5.md`, `plans/…`, dates of the plan | Plan directories are often gitignored. The reader cannot resolve them. |
| Specifics of a later change ("until the Kimi provider maps its names") | The only allowed pointer to later work is generic: "pending a future change", "until a future change maps them". |
| Validation as seconds (`cargo test` in 12.4s) | Validation states which checks pass, not how long they took. |

## Non-default target branch

If the MR does not target the repository's default branch, say so in **chat**,
on its own line: name the target branch, and say whether another MR must merge
first or the commit strands.

Do not bury the target in a subordinate clause of the announcement. Do not put
a local series plan in the MR description.

## Closed loopholes

- "The reviewer needs to know about the other branch." They need a structural
  scope reason. They do not need the name of a local lane.
- "I'm being helpful about what to do next." Helpful advice in an MR
  description is still advice. Put scheduling in the plan, not in git history.
- "Naming the follow-up MR makes the series navigable." GitLab already links
  related merge requests. Letters and plan filenames do not.

## Final scan

Search the description for: branch names that are not the MR's own, `worth
doing`, `once X lands`, `MR A`, `MR B`, `plans/`, and any time in seconds.
Delete them. Confirm every scope sentence is structural.
