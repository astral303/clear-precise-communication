# Always-on writing rules

Economy set: same rules as `claude-rules/`, less repetition. Prefer
`claude-rules/` when the token budget allows.

These files load at session start. They are not skills. Do not wait for
`/clear-precise-communication`. They bind the first draft. A later scan is
not a substitute.

## Artifacts in scope

Every durable artifact, including text drafted in chat:

- pull request titles and bodies
- commit subjects and bodies
- issues and review comments
- changelogs and release notes
- READMEs and other user documentation
- ADRs, plans, specifications, design docs, reviewer guides
- runbooks, reports, status updates
- `///` doc comments, `//` comments, `#` comments, module-level docs
- test names, assertion messages, panic and error strings
- user-facing copy

Comments, drafts, and "internal" text are in scope. "The reader is an
engineer" is not an exemption.

The ten scanning rules live in `clear-precise-communication.md`. They are in
force whether or not anyone invoked a skill.

## Closed excuses

| Excuse | Required behavior |
| --- | --- |
| "I didn't notice while writing." | Run `final-scan.md` on this artifact before sending. |
| "Bullet points didn't occur to me until the paragraph was done." | Parallel facts start as bullets or a table. |
| "That rule didn't apply to docs / comments / test names." | It did. See **Artifacts in scope**. |
| "The skill wasn't invoked." | These are rules, not skills. |
| "This is a heading rule; I was writing a comment." | The construction is banned wherever it appears. |
| "The sentence is true." | Truth is not usefulness. |
| "I'll structure it in a later pass." | Structure the first draft. |
| "Loaded rules do not apply while I draft." | They bind the first draft. |
| "I grepped the banned words." | That is step 3 of `final-scan.md` only. Run every step. |
| "It shipped in the same batch as code." | Scan it anyway. |

## Sibling files

- `clear-precise-communication.md` — ten scanning rules
- `documentation-tone.md` — describe; do not sell or inflate
- `noun-phrase-labels-not-questions.md` — noun-phrase labels
- `write-from-the-reader.md` — reader's next action, not the diff
- `pull-requests.md` — user-visible effect first; scannable; no machine state
- `changelog.md` — change class, verb + symptom, ratios
- `literal-verbs-not-idioms.md` — name the operation
- `one-term-per-concept.md` — one name per concept
- `no-rhetorical-appositives.md` — no theme-then-examples dash lists
- `reviewer-facing-describe-dont-advocate.md` — Decision → Reason → Boundary
- `comments-earn-their-place.md` — structure or a test first
- `final-scan.md` — every step, not only the keyword pass

## Order of work

1. Identify the artifact. Apply the matching sibling file and the shared
   rules.
2. Draft in the required shape: noun-phrase headings, bullets or tables for
   parallel facts, user-visible effect first, one term per concept.
3. Run `final-scan.md` on the text you are about to send.
