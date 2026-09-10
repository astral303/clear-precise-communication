import re
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import generate_gitlab_rules as ggr  # noqa: E402


class GitlabFilenameTests(unittest.TestCase):
    def test_renames_pr_prefix(self) -> None:
        self.assertEqual(
            ggr.gitlab_filename("pr-text-leads-with-the-bug.md"),
            "mr-text-leads-with-the-bug.md",
        )

    def test_leaves_other_names(self) -> None:
        self.assertEqual(
            ggr.gitlab_filename("machine-local-details-stay-local.md"),
            "machine-local-details-stay-local.md",
        )


class RewriteProseTests(unittest.TestCase):
    def test_pull_request_titles_and_bodies(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("- pull request titles and bodies"),
            "- merge request titles and descriptions",
        )
        self.assertEqual(
            ggr.rewrite_prose("Pull request titles and bodies, issue titles"),
            "Merge request titles and descriptions, issue titles",
        )

    def test_commit_bodies_stay_bodies(self) -> None:
        text = "- commit subjects and bodies"
        self.assertEqual(ggr.rewrite_prose(text), text)

    def test_issue_bodies_stay_bodies(self) -> None:
        source = (
            "Pull request bodies, issues, design docs, reviewer guides, "
            "plans, ADRs, and\nany engineering note that lists facts, "
            "mappings, or behavior. Commit bodies\nwhen they contain more "
            "than one fact."
        )
        expected = (
            "Merge request descriptions, issues, design docs, reviewer "
            "guides, plans, ADRs, and\nany engineering note that lists facts, "
            "mappings, or behavior. Commit bodies\nwhen they contain more "
            "than one fact."
        )
        self.assertEqual(ggr.rewrite_prose(source), expected)

    def test_pr_body_becomes_mr_description_with_article(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("a PR body drafted in chat"),
            "an MR description drafted in chat",
        )
        self.assertEqual(
            ggr.rewrite_prose('This is not a "PR body only" rule.'),
            'This is not an "MR description only" rule.',
        )
        self.assertEqual(
            ggr.rewrite_prose("This is not a PR-body rule."),
            "This is not an MR-description rule.",
        )

    def test_existing_mr_body_becomes_description(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("in a title, commit, MR body, or comment"),
            "in a title, commit, MR description, or comment",
        )
        self.assertEqual(
            ggr.rewrite_prose("`the user` in titles, commits, MR bodies and comments."),
            "`the user` in titles, commits, MR descriptions and comments.",
        )

    def test_generic_artifact_body_is_unchanged(self) -> None:
        source = 'Search title, body, commit, changelog, README, and'
        self.assertEqual(ggr.rewrite_prose(source), source)
        source = '"I wrote the body to match my title." Then the title was wrong, or the body'
        self.assertEqual(ggr.rewrite_prose(source), source)
        source = "changelog's noun for the thing (`truncated messages`, not `bodies`)."
        self.assertEqual(ggr.rewrite_prose(source), source)

    def test_body_order_and_opens(self) -> None:
        self.assertEqual(ggr.rewrite_prose("## Body order"), "## Description order")
        self.assertEqual(ggr.rewrite_prose("Body order:"), "Description order:")
        self.assertEqual(
            ggr.rewrite_prose("The body opens with the problem"),
            "The description opens with the problem",
        )

    def test_phrases_match_across_a_wrap(self) -> None:
        wrapped_open = (
            "never the mechanism. The\n"
            "body opens with the problem"
        )
        self.assertEqual(
            ggr.rewrite_prose(wrapped_open),
            "never the mechanism. The description opens with the problem",
        )
        wrapped_body = (
            "If the chat text is the PR body, it is the PR\n"
            "  body."
        )
        self.assertEqual(
            ggr.rewrite_prose(wrapped_body),
            "If the chat text is the MR description, it is the MR description.",
        )
        wrapped_list = "changelogs, PR\nbodies, commit messages"
        self.assertEqual(
            ggr.rewrite_prose(wrapped_list),
            "changelogs, MR descriptions, commit messages",
        )

    def test_github_word_not_github_url(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("destined for GitHub."),
            "destined for GitLab.",
        )
        url = "https://github.com/ayghri/i-have-adhd"
        self.assertEqual(ggr.rewrite_prose(url), url)

    def test_filename_mentions(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("See `pr-text-leads-with-the-bug.md`."),
            "See `mr-text-leads-with-the-bug.md`.",
        )

    def test_plan_internal_names(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose("`PR A`, `PR-5.md`, `plans/…`"),
            "`MR A`, `MR-5.md`, `plans/…`",
        )

    def test_stacking_vocabulary(self) -> None:
        source = (
            "If the PR is not against the repository's default branch, "
            "say so in **chat**,\non its own line: name the base, and say "
            "that it must merge before this PR or\nthe commit strands. Do "
            "not put the stacking plan in the PR body."
        )
        expected = (
            "If the MR does not target the repository's default branch, "
            "say so in **chat**,\non its own line: name the target branch, "
            "and say whether another MR must merge first or\nthe commit "
            "strands. Do not put a local series plan in the MR description."
        )
        self.assertEqual(ggr.rewrite_prose(source), expected)
        self.assertEqual(
            ggr.rewrite_prose(
                "A non-default PR base is announced in chat, not in the body."
            ),
            "A non-default target branch is announced in chat, not in the description.",
        )
        self.assertEqual(
            ggr.rewrite_prose(
                '"Naming the follow-up PR makes the series navigable." '
                "GitHub already links stacked PRs."
            ),
            '"Naming the follow-up MR makes the series navigable." '
            "GitLab already links related merge requests.",
        )

    def test_rewrite_is_idempotent_on_source_rules(self) -> None:
        for dir_name in ggr.SOURCE_DIR_NAMES:
            for path in sorted((REPO_ROOT / dir_name).glob("*.md")):
                once = ggr.rewrite_prose(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    ggr.rewrite_prose(once),
                    once,
                    path.relative_to(REPO_ROOT).as_posix(),
                )

    def test_feature_pr_and_prs_only(self) -> None:
        self.assertEqual(
            ggr.rewrite_prose('A feature PR still leads with the user-visible effect.'),
            "A feature MR still leads with the user-visible effect.",
        )
        self.assertEqual(
            ggr.rewrite_prose('This is not "PRs only".'),
            'This is not "MRs only".',
        )
        self.assertEqual(
            ggr.rewrite_prose("Two changes in one PR are joined"),
            "Two changes in one MR are joined",
        )


class GenerateTreeTests(unittest.TestCase):
    def test_rebuilds_and_deletes_stale_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            repo = Path(raw)
            (repo / "claude-rules").mkdir()
            (repo / "claude-rules-economy").mkdir()
            (repo / "claude-rules" / "always-on-scope.md").write_text(
                "- pull request titles and bodies\n", encoding="utf-8"
            )
            (repo / "claude-rules" / "pr-text-leads-with-the-bug.md").write_text(
                "# PR text leads with the user-visible change\n", encoding="utf-8"
            )
            (repo / "claude-rules-economy" / "always-on-scope.md").write_text(
                "See `pr-text-leads-with-the-bug.md`.\n", encoding="utf-8"
            )
            stale_dir = repo / "gitlab" / "claude-rules"
            stale_dir.mkdir(parents=True)
            (stale_dir / "stale.md").write_text("leftover\n", encoding="utf-8")
            (stale_dir / "pr-text-leads-with-the-bug.md").write_text(
                "old name\n", encoding="utf-8"
            )

            written = ggr.generate_gitlab_tree(repo)
            gitlab = repo / "gitlab"

            self.assertFalse((stale_dir / "stale.md").exists())
            self.assertFalse((stale_dir / "pr-text-leads-with-the-bug.md").exists())
            leads = gitlab / "claude-rules" / "mr-text-leads-with-the-bug.md"
            self.assertTrue(leads.exists())
            self.assertEqual(
                leads.read_text(encoding="utf-8"),
                "# MR text leads with the user-visible change\n",
            )
            self.assertEqual(
                (gitlab / "claude-rules" / "always-on-scope.md").read_text(
                    encoding="utf-8"
                ),
                "- merge request titles and descriptions\n",
            )
            self.assertEqual(
                (gitlab / "claude-rules-economy" / "always-on-scope.md").read_text(
                    encoding="utf-8"
                ),
                "See `mr-text-leads-with-the-bug.md`.\n",
            )
            self.assertEqual(
                (gitlab / "README.md").read_text(encoding="utf-8"),
                ggr.GITLAB_README,
            )
            self.assertEqual(len(written), 4)

    def test_source_trees_are_not_modified(self) -> None:
        original = (
            REPO_ROOT / "claude-rules" / "always-on-scope.md"
        ).read_bytes()
        with tempfile.TemporaryDirectory() as raw:
            repo = Path(raw)
            for name in ggr.SOURCE_DIR_NAMES:
                dest = repo / name
                dest.mkdir()
                (dest / "always-on-scope.md").write_bytes(
                    (REPO_ROOT / name / "always-on-scope.md").read_bytes()
                )
            ggr.generate_gitlab_tree(repo)
            self.assertEqual(
                (repo / "claude-rules" / "always-on-scope.md").read_bytes(),
                original,
            )
        self.assertEqual(
            (REPO_ROOT / "claude-rules" / "always-on-scope.md").read_bytes(),
            original,
        )


class CommittedTreeTests(unittest.TestCase):
    def test_gitlab_tree_matches_generator(self) -> None:
        planned = ggr.planned_outputs(REPO_ROOT)
        gitlab = REPO_ROOT / ggr.OUTPUT_DIRNAME
        on_disk = {path.resolve() for path in gitlab.rglob("*") if path.is_file()}
        planned_resolved = {path.resolve(): content for path, content in planned.items()}
        self.assertEqual(
            on_disk,
            set(planned_resolved),
            "gitlab/ has extra or missing files; rerun "
            "tools/generate_gitlab_rules.py",
        )
        for path, content in planned.items():
            self.assertEqual(
                path.read_text(encoding="utf-8"),
                content,
                f"{path.relative_to(REPO_ROOT)} is stale; rerun "
                "tools/generate_gitlab_rules.py",
            )

    def test_generated_rules_drop_pr_and_github_host(self) -> None:
        leftover = re_compile_leftovers()
        gitlab_rules = (REPO_ROOT / ggr.OUTPUT_DIRNAME).glob("claude-rules*/**/*.md")
        hits = []
        for path in gitlab_rules:
            text = path.read_text(encoding="utf-8")
            if leftover.search(text):
                hits.append(path.relative_to(REPO_ROOT).as_posix())
        self.assertEqual(hits, [])


def re_compile_leftovers():
    return re.compile(r"\bpull request\b|\bPRs?\b|\bGitHub\b|\bstacked PRs\b", re.I)


if __name__ == "__main__":
    unittest.main()
