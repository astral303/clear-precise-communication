# Comments earn their place

First express the idea through names, structure, types, and tests. A comment
is not an acceptable fix for "the next reader could break X without noticing."

When a constraint is not obvious:

1. What shape of code makes the mistake impossible or obvious?
2. Which test fails if the mistake is made?
3. Only if neither exists: a comment, and why structure could not carry it.

A self-describing name beats a documented constant
(`Deleted::just_the_session()` instead of `Deleted::ONE_COPY` plus its doc).

Keep only what the code cannot say: why this branch and not the obvious one, a
consequence of "simplifying", a limit the reader would assume away. Explain
*why*, not line-by-line *what*. Two or three sentences, local, no advocacy.

Cut: restatement of the signature, of the next line, of the test's name;
`What X does` / `Where X lives`; idioms; verdicts (`this is safe`); narration
of the diff. Thorough restatement is noise. Do not leave a comment as a record
of a structural problem you chose not to fix.
