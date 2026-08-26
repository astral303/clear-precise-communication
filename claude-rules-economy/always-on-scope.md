# Always-on writing rules

These files are Claude Code user rules. They load at session start. They are not
skills. Do not wait for `/clear-precise-communication` or any other invocation.

They bind the first draft. There is no cleanup pass the user asked for. If a
later scan finds a violation, fix it before the artifact leaves your hands.

Companion file, also always-on: `clear-precise-communication.md` in this
directory (the one-file rule, with an always-on preamble). These files do not
replace it. They close the loopholes it left. If that file is not loaded, the
ten rules below are still in force. They apply to every durable artifact in
the list that follows. They are not a skill. Do not wait to be asked.

## Artifacts in scope

Every durable artifact, including text you draft in chat and later paste:

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

Comments are in scope. Drafts are in scope. "Internal" text is in scope. "The
reader is an engineer" is not an exemption. "This sentence is only in a
comment" is not an exemption.

`clear-precise-communication.md` already says it applies to every durable
artifact. Treat that sentence as literal.

## Ten scanning rules (always in force)

1. **Lead with the primary value.** First sentence is the conclusion, decision,
   change, request, outcome, or risk. Not background.
2. **Design for scanning.** Descriptive headings. First sentence of each
   paragraph is the point. A series of points is bullets, from the first
   draft, not after a paragraph exists. Grids are tables. Title, headings,
   and opening sentences are a useful map on their own.
3. **Make starting easy and steps bounded.** One bounded action per step.
   Commands, paths, and expected results sit next to the step that needs them.
4. **Externalize state.** Current status, remaining work, blockers, when the
   artifact tracks progress. No manufactured next action on a completed record
   or a descriptive changelog.
5. **Suppress tangents.** One thread per section. Optional material is labeled
   optional or cut.
6. **Give concrete time estimates** when time matters. Units, ranges,
   assumptions. Do not invent an estimate.
7. **Make progress and outcomes visible.** What changed, what now works — not
   which files were touched.
8. **Describe errors matter-of-factly.** Symptom, cause if known, impact,
   remedy. No alarmist filler.
9. **Control list size.** Prefer ≤5 siblings when prioritization is possible.
   Do not split a canonical list just to meet a count.
10. **Remove preambles, repeated recaps, and generic closers.** No "This
    document will." No recap of the recap. No "happy to help."

Full text: `clear-precise-communication.md` in this directory.

## Closed excuses

These have been offered and are rejected:

| Excuse | Required behavior |
| --- | --- |
| "I didn't notice while writing the sentence." | After drafting, search the artifact for the banned patterns in these files. Fix before sending. |
| "Bullet points didn't occur to me until the paragraph was done." | If the content is a series of parallel facts, start as bullets or a table. Do not write a paragraph and convert later. |
| "I didn't think that instruction applied to docs / comments / test names." | It did. See **Artifacts in scope**. |
| "The skill wasn't invoked." | These are rules, not skills. |
| "This is a heading rule, and I was writing a comment." | The banned construction is banned wherever it appears. |
| "The sentence is true." | Truth is not usefulness. Cut a true sentence that does not change what the reader does. |
| "I'll structure it in a later pass." | Structure the first draft. |
| "Loaded rules do not apply themselves while I draft." | They bind the first draft. A later scan is not a substitute. |
| "I grepped the banned words / ran a keyword pass." | That is step 3 of `final-scan.md` only. The other steps are reads. Run every step. |
| "The artifact shipped in the same batch as code edits." | Scan it anyway. A code batch is not a reason to skip the writing check. |
| "This is just a draft / plan / reviewer note." | Durable text uses the same register as shipped docs. |

## Sibling rules in this directory

- `clear-precise-communication.md` — the ten scanning rules in full.
- `documentation-tone.md` — describe; do not sell, celebrate, or inflate.
- `noun-phrase-labels-not-questions.md` — labels are noun phrases, not questions or What/Where/Why openers.
- `write-from-the-reader.md` — write for the reader's next action, not as a narration of the diff.
- `pr-text-leads-with-the-bug.md` — title and opening name the user-visible problem or effect.
- `pr-text-scannable-structure.md` — tables for grids, one-fact bullets, no prose restating bullets.
- `pr-bodies-are-permanent-records.md` — facts about the change only; no machine state, no advice.
- `changelog-entry-style.md` — change class, standalone parent summary, verb + symptom.
- `changelog-impact-claims.md` — ratios a reader can reuse; no correctness theater.
- `literal-verbs-not-idioms.md` — name the operation; do not analogize it.
- `one-term-per-concept.md` — one name for one concept; no synonyms for variety.
- `no-rhetorical-appositives.md` — no theme-then-examples dash lists; the things are the subject.
- `reviewer-facing-describe-dont-advocate.md` — Decision → Reason → Boundary; no verdicts.
- `comments-earn-their-place.md` — structure or a test first; comments only for what code cannot say.
- `final-scan.md` — every step of the post-write scan, not only the keyword pass.

## Order of work

1. Identify the artifact type. Use the matching sibling rule and the shared
   rules (tone, labels, reader, verbs, scan).
2. Draft in the required shape: noun-phrase headings, bullets or tables for
   parallel facts, user-visible effect first. Pick one term per concept and
   reuse it verbatim.
3. Run `final-scan.md` on the text you are about to send. Not on a later
   revision. On this one.
