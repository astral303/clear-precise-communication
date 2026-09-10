# Machine-local details stay local

Can the reader act on this from where they sit? A session ID, a path on this
disk, a wall-clock timing, or a local branch is meaningful only on this
computer. That is chat and a gitignored plans directory. Anything that leaves
the machine (MR, commit, changelog, README, issue, review comment, committed
docs) gets "In one example session, …" plus a table of facts a stranger can
use.

A UUID is not a fact. Full IDs in chat are so *you* can open the session.
They do not extend to an MR. Gitignored plans may name IDs; committed plans
may not.

Also cut from MRs: other branches, `cargo test` seconds, `MR A` / `plans/…`,
and advice about when to do a follow-up. Scope reasons must be structural.
A non-default target branch is announced in chat, not in the description.
