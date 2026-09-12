import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import count_claude_tokens as cct  # noqa: E402


class FormatMemoryDisplayTests(unittest.TestCase):
    def test_exact_below_one_thousand(self) -> None:
        self.assertEqual(cct.format_memory_display(862), "862")
        self.assertEqual(cct.format_memory_display(920), "920")
        self.assertEqual(cct.format_memory_display(998), "998")

    def test_tenths_of_k(self) -> None:
        self.assertEqual(cct.format_memory_display(1000), "1k")
        self.assertEqual(cct.format_memory_display(1048), "1k")
        self.assertEqual(cct.format_memory_display(1070), "1.1k")
        self.assertEqual(cct.format_memory_display(1100), "1.1k")
        self.assertEqual(cct.format_memory_display(1213), "1.2k")
        self.assertEqual(cct.format_memory_display(1373), "1.4k")
        self.assertEqual(cct.format_memory_display(1559), "1.6k")
        self.assertEqual(cct.format_memory_display(2153), "2.2k")
        self.assertEqual(cct.format_memory_display(2241), "2.2k")


class CtokOpus5Tests(unittest.TestCase):
    def test_published_hello_world(self) -> None:
        self.assertEqual(cct.count_opus5("hello, world"), 10)
        self.assertEqual(cct.count_claude5("hello, world"), 10)

    def test_cli_counts_default_rules_dir(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with patch("sys.stdout", stdout), patch("sys.stderr", stderr):
            code = cct.main([])
        self.assertEqual(code, 0)
        self.assertIn("total", stdout.getvalue())
        self.assertIn("ctok family 5.0", stderr.getvalue())

    def test_install_tables_split_claude_rules_from_shared_artifacts(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with patch("sys.stdout", stdout), patch("sys.stderr", stderr):
            code = cct.main(["--table"])
        self.assertEqual(code, 0)
        table = stdout.getvalue()
        self.assertIn("| Artifact | GitHub | GitLab |", table)
        self.assertIn("| Artifact | Claude 5 | Codex |", table)
        self.assertNotIn("| Artifact | GitHub | GitLab | Claude 5 |", table)
        self.assertIn("`claude-rules/`", table)
        self.assertIn("`claude-rules-economy/`", table)
        self.assertIn("`rules/clear-precise-communication.md`", table)
        self.assertIn("`write-commit-messages`", table)

        claude_rows = cct.claude_table_rows(cct.REPO_ROOT)
        self.assertEqual(
            [label for label, *_ in claude_rows],
            ["claude-rules/", "claude-rules-economy/"],
        )
        self.assertGreater(claude_rows[0][1], 0)
        self.assertGreater(claude_rows[0][2], 0)

        shared_rows = cct.shared_table_rows(cct.REPO_ROOT)
        self.assertEqual(
            [label for label, *_ in shared_rows],
            [
                "rules/clear-precise-communication.md",
                "write-commit-messages",
            ],
        )
        for _label, claude5, codex in shared_rows:
            self.assertGreater(claude5, 0)
            self.assertGreater(codex, 0)
            self.assertLess(codex, claude5)


if __name__ == "__main__":
    unittest.main()
