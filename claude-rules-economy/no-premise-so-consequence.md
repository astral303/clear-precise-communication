# No premise-so-consequence

A comment is an instruction: when to act, imperative, execution order. It
is not a proof from a general truth. Theorem prose asks the reader to
check each inference. A comment's reader trusts the code and needs to
act. Do not assign them the proof.

| Derived (cut) | Stated (write) |
| --- | --- |
| A shard holds its sessions' text, so only a shard holding a session read anew … is rewritten. | Rewrite a shard only if one of its sessions was reread, recorded empty, or deleted. |
| A restored entry equals the one on disk, so its shard needs no write. | If the restored session matches disk, skip the write. |

If you derive the behavior from how the system *is*, delete the premise
and state the behavior. Reasons go after, as `because`, if at all.

Banned: `X, so Y` where X is ontology; `needs no ___`; `anew`; `alone
suffices`; two sentences that mirror each other. `so` after a real
consequence is fine ("retry so the error is visible").
