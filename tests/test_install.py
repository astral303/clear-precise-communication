import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "install"))

import install as inst  # noqa: E402


def run(args: list[str], home: Path) -> tuple[int, str]:
    stdout = io.StringIO()
    code = inst.main([*args, "--home", str(home)], stdin=io.StringIO(), stdout=stdout, isatty=False)
    return code, stdout.getvalue()


class CheckboxViewTests(unittest.TestCase):
    def test_redraw_moves_up_exactly_the_printed_lines(self) -> None:
        home = Path("/tmp/fake-home")
        view, line_count = inst.checkbox_view(
            ["codex", "claude", "grok"],
            home,
            [True, True, False],
            1,
        )
        self.assertTrue(view.endswith("\n"))
        self.assertEqual(view.count("\n"), line_count)
        self.assertEqual(inst.checkbox_clear(line_count), f"\r\x1b[{line_count}A\x1b[J")
        self.assertIn("> [x] claude", view)
        self.assertIn("  [ ] grok", view)


class DiffColorTests(unittest.TestCase):
    def test_tty_diffs_request_color(self) -> None:
        plain = inst.unified_diff("old line\n", "new line\n", "sample.md", color=False)
        colored = inst.unified_diff("old line\n", "new line\n", "sample.md", color=True)
        self.assertIn("--- a/sample.md", plain)
        self.assertIn("+++ b/sample.md", plain)
        self.assertNotIn("\x1b[", plain)
        self.assertIn("\x1b[", colored)


class HelpTests(unittest.TestCase):
    def test_help_says_bare_run_writes_nothing(self) -> None:
        stdout = io.StringIO()
        with patch("sys.stdout", stdout):
            with self.assertRaises(SystemExit) as ctx:
                inst.main(["-h"])
        self.assertEqual(ctx.exception.code, 0)
        text = stdout.getvalue()
        self.assertIn("writes nothing", text)
        self.assertIn("up/down", text)
        self.assertIn("Space", text)


class SafetyTests(unittest.TestCase):
    def test_no_tty_without_flags_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            (home / ".codex").mkdir()
            code, out = run([], home)
            self.assertEqual(code, 0)
            self.assertIn("Detected:", out)
            self.assertFalse((home / ".codex" / "AGENTS.d").exists())
            self.assertFalse((home / ".codex" / "AGENTS.md").exists())

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            (home / ".codex").mkdir()
            code, out = run(["--dry-run", "--agents", "codex"], home)
            self.assertEqual(code, 0)
            self.assertIn("change(s)", out)
            self.assertFalse((home / ".codex" / "AGENTS.d").exists())
            self.assertFalse((home / ".codex" / "AGENTS.md").exists())


class InstallTests(unittest.TestCase):
    def test_yes_installs_codex_claude_and_grok(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            code, out = run(
                ["--yes", "--agents", "codex,claude,grok"],
                home,
            )
            self.assertEqual(code, 0, out)
            self.assertIn("Installed.", out)
            for agent in ("codex", "grok"):
                agents_d = home / f".{agent}" / "AGENTS.d"
                comm = agents_d / "clear-precise-communication.md"
                code_file = agents_d / "clean-code-principles.md"
                self.assertTrue(comm.is_symlink(), comm)
                self.assertEqual(
                    comm.resolve(),
                    (REPO / "rules" / "clear-precise-communication.md").resolve(),
                )
                self.assertTrue(code_file.is_symlink())
                self.assertEqual(
                    code_file.resolve(),
                    (REPO / "rules" / "clean-code-principles.md").resolve(),
                )
                agents_md = (home / f".{agent}" / "AGENTS.md").read_text(encoding="utf-8")
                self.assertIn("clear-precise-communication.md", agents_md)
                self.assertIn("clean-code-principles.md", agents_md)
                skill = home / f".{agent}" / "skills" / "write-commit-messages"
                self.assertTrue(skill.is_symlink())
                self.assertEqual(
                    skill.resolve(),
                    (REPO / "skills" / "write-commit-messages").resolve(),
                )
            writing = home / ".claude" / "rules" / "clear-precise-writing"
            self.assertTrue(writing.is_symlink())
            self.assertEqual(writing.resolve(), (REPO / "claude-rules").resolve())
            claude_skill = home / ".claude" / "skills" / "write-commit-messages"
            self.assertTrue(claude_skill.is_symlink())

    def test_second_install_is_noop(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            run(["--yes", "--agents", "codex"], home)
            agents_md = home / ".codex" / "AGENTS.md"
            before = agents_md.read_text(encoding="utf-8")
            code, out = run(["--yes", "--agents", "codex"], home)
            self.assertEqual(code, 0, out)
            self.assertIn("Already installed.", out)
            self.assertNotIn("Backed up ", out)
            self.assertEqual(agents_md.read_text(encoding="utf-8"), before)

    def test_doctor_ok_then_fails_if_stanza_removed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            run(["--yes", "--agents", "codex"], home)
            code, out = run(["--doctor", "--agents", "codex"], home)
            self.assertEqual(code, 0, out)
            self.assertIn("Install looks complete.", out)
            agents_md = home / ".codex" / "AGENTS.md"
            agents_md.write_text("# empty\n", encoding="utf-8")
            code, out = run(["--doctor", "--agents", "codex"], home)
            self.assertEqual(code, 1, out)
            self.assertIn("does not mention", out)

    def test_replacing_drifted_copy_writes_backup(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            run(["--yes", "--agents", "codex"], home)
            dest = home / ".codex" / "AGENTS.d" / "clear-precise-communication.md"
            dest.unlink()
            dest.write_text("stale copy\n", encoding="utf-8")
            code, out = run(["--yes", "--agents", "codex"], home)
            self.assertEqual(code, 0, out)
            self.assertIn("Backed up ~/.codex/AGENTS.d/clear-precise-communication.md to ", out)
            self.assertTrue(dest.is_symlink())
            self.assertEqual(
                dest.resolve(),
                (REPO / "rules" / "clear-precise-communication.md").resolve(),
            )
            backup_line = next(
                line for line in out.splitlines() if line.startswith("Backed up ")
            )
            saved = Path(backup_line.rsplit(" to ", 1)[1])
            self.assertTrue(saved.name.endswith("clear-precise-communication.md"))
            self.assertEqual(saved.read_text(encoding="utf-8"), "stale copy\n")

    def test_gitlab_economy_points_at_generated_tree(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            code, out = run(
                [
                    "--yes",
                    "--agents",
                    "claude",
                    "--gitlab",
                    "--claude-set",
                    "economy",
                ],
                home,
            )
            self.assertEqual(code, 0, out)
            writing = home / ".claude" / "rules" / "clear-precise-writing"
            self.assertEqual(
                writing.resolve(),
                (REPO / "gitlab" / "claude-rules-economy").resolve(),
            )

    def test_old_skill_warns_but_doctor_still_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            run(["--yes", "--agents", "codex"], home)
            leftover = home / ".codex" / "skills" / "clear-precise-communication"
            leftover.mkdir()
            code, out = run(["--doctor", "--agents", "codex"], home)
            self.assertEqual(code, 0, out)
            self.assertIn("leftover always-on skill", out)


if __name__ == "__main__":
    unittest.main()
