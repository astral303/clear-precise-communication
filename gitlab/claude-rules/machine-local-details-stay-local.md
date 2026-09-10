# Machine-local details stay local

The test for any detail: can the reader act on it from where they sit?

A session ID, a path on this disk, a wall-clock timing, or a branch that
exists only on this machine is meaningful only to someone with this computer.
That belongs in chat and in a gitignored plans directory. Anything that
**leaves the machine** gets the observable facts instead: "In one example
session, …" plus a table of dates, record types, or other facts a stranger
can use.

This is not an MR-description rule. It is not a session-ID rule. It is the same test
for every durable artifact.

## Scope

Leaves the machine (no local IDs, paths, timings, or working-tree state):

- merge request titles and descriptions
- commit subjects and bodies
- changelogs and release notes
- READMEs and other user documentation
- issues and review comments
- ADRs, design docs, reviewer guides
- any other file that is committed or posted

Stays on this computer (full session IDs and local paths are fine):

- this chat
- a gitignored plans directory

A plan that will be committed is leaving the machine. Treat it as an MR description.

## Required shape

| Do not write (this machine) | Write (the reader can use) |
| --- | --- |
| `bc047371-6b88-4b30-b2a1-cb1cac746094` | In one example session, … (then the table of facts) |
| `C:\Users\…\sessions\…` | the session store / the transcript on disk |
| `cargo test` in 12.4s | which checks pass |
| seven columns measured on a screenshot | the timestamp column (`i`) |
| lane-2 is also editing that file | a structural scope reason |

A UUID is not a fact. It names a file on this disk. The facts are what that
session contained.

## Content that still does not belong in an MR

These are the same test, applied to follow-ups and working-tree chatter:

| Cut | Why |
| --- | --- |
| Which other branches are being edited | The next reader cannot see that machine. |
| Advice ("worth doing as its own branch once…") | An MR is not a coaching note. |
| Plan-internal names: `MR A`, `MR-5.md`, `plans/…` | Gitignored; the reader cannot resolve them. |
| Specifics of a later change | Allowed: "pending a future change" |

A scope reason must be structural: "clearing them edits Rust code, which is
outside the scope of this change." Not situational: "worth doing once the
concurrent work lands."

## Non-default target branch

If the MR does not target the repository's default branch, say so in **chat**,
on its own line: name the target branch, and say whether another MR must merge first or
the commit strands. Do not put a local series plan in the MR description.

## Closed loopholes

- "The chat rule is full session IDs, so maybe the MR too." Full IDs in chat
  are so *you* can open the session in the tool. An MR is not chat. A reader
  of the MR cannot open `bc047371-…`.
- "I did not list documentation / review comments / commits." Anything that
  leaves the machine. The list above is examples, not an exemption table.
- "Plans are durable artifacts." Gitignored plans on this disk are local.
  Committed plans are not.
- "The UUID identifies the example." The table of observable facts identifies
  the example. The UUID identifies a file the reader does not have.
- "The reviewer needs to reproduce the session." They need the facts that
  transfer. They do not have this computer.

## Final scan

For each proper noun, path, UUID, timestamp, and branch name: can a reader
who is not on this machine act on it? No → rewrite as the observable fact, or
move it to chat / the gitignored plan. Search committed text for UUID-shaped
strings and absolute paths; they almost never belong.
