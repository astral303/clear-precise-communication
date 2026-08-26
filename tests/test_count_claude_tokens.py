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

    def test_cli_counts_default_rules_dir(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with patch("sys.stdout", stdout), patch("sys.stderr", stderr):
            code = cct.main([])
        self.assertEqual(code, 0)
        self.assertIn("total", stdout.getvalue())
        self.assertIn("ctok family 5.0", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
