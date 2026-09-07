# Clean Code Principles

Apply these rules whenever creating or changing code, not only during review or refactoring. They concisely paraphrase Robert C. Martin's *Clean Code*. Correctness, security, explicit requirements, public contracts, and established project conventions take precedence.

## Priorities

- Make code correct, then improve its structure while tests protect behavior.
- Prefer the smallest coherent change that solves the problem.
- Leave touched code clearer without expanding into unrelated cleanup.
- Optimize for the next reader, not for cleverness or rigid rule-following.

## Names

- Choose names that reveal purpose, domain meaning, units, state, and important constraints.
- Prefer precise, searchable, pronounceable names over abbreviations, encodings, single letters, or vague words such as `data`, `info`, `thing`, and `manager`.
- Never shorten a name merely to save typing. Autocomplete removes typing cost; ambiguity taxes every reader.
- Use one term consistently for one concept, and do not reuse it for unrelated concepts.
- Name functions with verbs, types with nouns, and booleans as predicates such as `is_valid` or `can_retry`.
- Replace unexplained literals with meaningful constants. Rename identifiers that need comments merely to explain them.

## Functions and control flow

- Make each function perform one coherent operation at one level of abstraction.
- Keep control flow small and obvious. Extract helpers when their names reveal intent, remove genuine duplication, or separate abstraction levels—not merely to make functions shorter.
- Arrange code from high-level policy to lower-level details.
- Minimize parameters; treat long lists, output parameters, and boolean mode flags as design warnings.
- Make mutation, I/O, caching, and other side effects explicit in names and contracts.
- Separate commands that change state from queries that return information when practical.

## Comments

- First express the idea through names, structure, types, and tests. Do not use comments to compensate for confusing code.
- Comment what code cannot express: rationale, consequential warnings, external constraints, public contracts, or a concise actionable `TODO`.
- Explain *why*, not line-by-line *what* the code does.
- Keep comments accurate and local; update or remove them when behavior changes.
- Delete redundant, misleading, stale, ceremonial, journal-style, attribution, and commented-out code. Version control preserves history.
- Document public APIs only when the documentation adds contract information rather than restating the signature.

## Structure and design

- Give each class or module one clear responsibility and one primary reason to change.
- Keep state narrowly owned, variables near their use, scopes small, and related declarations together.
- Follow repository formatting consistently; use its automated formatter.
- Do not mix high-level policy with low-level parsing, storage, formatting, or protocol mechanics.
- Encapsulate implementation details behind small, meaningful interfaces. Avoid reaching through chains of collaborators.
- Prefer objects when behavior and invariants belong with data; prefer plain data structures when callers legitimately transform exposed data.
- Keep each rule or algorithm in one authoritative place. Consolidate code only when it represents the same concept and should change for the same reason.
- Add abstractions only when they reduce duplication or cognitive load; avoid speculative frameworks and needless layers.

## Errors and boundaries

- Use idiomatic error mechanisms rather than magic return values. Add useful context without losing the original cause.
- Keep recovery and translation logic from obscuring the normal path. Never silently swallow unexpected failures.
- Avoid `null` when an empty collection, optional/result type, or explicit domain value communicates the contract better.
- Validate untrusted input at boundaries and maintain clear internal invariants.
- Contain third-party details when a boundary clarifies usage, translates errors, or limits future change.

## Tests

- Treat tests as production-quality code: clear, focused, and maintainable.
- Prefer tests that are fast, independent, repeatable, self-validating, and written with the behavior they protect.
- Make setup, action, and expected result obvious. Test boundaries, failures, and regressions as well as happy paths.

## Simplicity

In priority order, a clean design works correctly and passes its tests, reveals intent, avoids unnecessary duplication, and uses no more structural elements than needed. Remove dead code and speculative generality. Apply patterns only to present problems. Simple means easy to understand and change, not merely short.
