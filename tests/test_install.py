import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "install"))

import install as inst  # noqa: E402


def assert_linked(dest: Path, source: Path) -> None:
    if inst.use_symlinks():
        assert dest.is_symlink(), dest
        assert dest.resolve() == source.resolve()
        return
    assert dest.exists(), dest
    assert not dest.is_junction()
    assert not dest.is_symlink()
    if source.is_dir():
        assert inst._files_match(dest, source)
    else:
        assert dest.read_bytes() == source.read_bytes()


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
            self.assertIn("will be applied:", out)
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
            self.assertIn("Changes applied, install complete.", out)
            self.assertIn("- Point ", out)
            self.assertRegex(out, r"- Point .+:\n\n")
            for agent in ("codex", "grok"):
                agents_d = home / f".{agent}" / "AGENTS.d"
                comm = agents_d / "clear-precise-communication.md"
                code_file = agents_d / "clean-code-principles.md"
                assert_linked(comm, REPO / "rules" / "clear-precise-communication.md")
                assert_linked(code_file, REPO / "rules" / "clean-code-principles.md")
                agents_md = (home / f".{agent}" / "AGENTS.md").read_text(encoding="utf-8")
                self.assertIn("clear-precise-communication.md", agents_md)
                self.assertIn("clean-code-principles.md", agents_md)
                skill = home / f".{agent}" / "skills" / "write-commit-messages"
                assert_linked(skill, REPO / "skills" / "write-commit-messages")
            writing = home / ".claude" / "rules" / "clear-precise-writing"
            assert_linked(writing, REPO / "claude-rules")
            claude_skill = home / ".claude" / "skills" / "write-commit-messages"
            assert_linked(claude_skill, REPO / "skills" / "write-commit-messages")

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
            self.assertIn(
                "\nBacked up ~/.codex/AGENTS.d/clear-precise-communication.md to ",
                out,
            )
            self.assertIn("\nChanges applied, install complete.", out)
            assert_linked(dest, REPO / "rules" / "clear-precise-communication.md")
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
            assert_linked(writing, REPO / "gitlab" / "claude-rules-economy")

    def test_old_skill_warns_but_doctor_still_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            run(["--yes", "--agents", "codex"], home)
            leftover = home / ".codex" / "skills" / "clear-precise-communication"
            leftover.mkdir()
            code, out = run(["--doctor", "--agents", "codex"], home)
            self.assertEqual(code, 0, out)
            self.assertIn("leftover always-on skill", out)


class WindowsCopyTests(unittest.TestCase):
    def setUp(self) -> None:
        if inst.use_symlinks():
            self.skipTest("directory copies replace junctions on Windows")

    def test_replacing_a_junction_leaves_the_source_in_place(self) -> None:
        import subprocess

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            source = root / "source"
            source.mkdir()
            (source / "rule.md").write_text("rule\n", encoding="utf-8")
            junction = root / "linked"
            completed = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(junction), str(source)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(junction.is_junction())
            inst._mirror_tree(junction, source)
            self.assertFalse(junction.is_junction())
            self.assertEqual((source / "rule.md").read_text(encoding="utf-8"), "rule\n")
            self.assertEqual((junction / "rule.md").read_text(encoding="utf-8"), "rule\n")

    def test_mirror_updates_and_deletes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            source = root / "source"
            dest = root / "dest"
            source.mkdir()
            (source / "keep.md").write_text("new\n", encoding="utf-8")
            dest.mkdir()
            (dest / "keep.md").write_text("old\n", encoding="utf-8")
            (dest / "gone.md").write_text("gone\n", encoding="utf-8")
            inst._mirror_tree(dest, source)
            self.assertEqual((dest / "keep.md").read_text(encoding="utf-8"), "new\n")
            self.assertFalse((dest / "gone.md").exists())

    def test_two_junctions_back_up_to_different_paths(self) -> None:
        import subprocess

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            home = root / "home"
            source = root / "source"
            source.mkdir()
            (source / "rule.md").write_text("rule\n", encoding="utf-8")
            home.mkdir()
            first = home / "a"
            second = home / "b"
            for dest in (first, second):
                completed = subprocess.run(
                    ["cmd", "/c", "mklink", "/J", str(dest), str(source)],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
            backup_root = root / "backup"
            saved = [
                inst.backup_path(dest, backup_root, home) for dest in (first, second)
            ]
            self.assertNotEqual(saved[0], saved[1])
            self.assertEqual((source / "rule.md").read_text(encoding="utf-8"), "rule\n")

    def test_doctor_rejects_a_junction(self) -> None:
        import subprocess

        with tempfile.TemporaryDirectory() as raw:
            home = Path(raw)
            (home / ".claude").mkdir()
            run(["--yes", "--agents", "claude"], home)
            writing = home / ".claude" / "rules" / "clear-precise-writing"
            inst._remove_dest(writing)
            source = REPO / "claude-rules"
            completed = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(writing), str(source)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            code, out = run(["--doctor", "--agents", "claude"], home)
            self.assertEqual(code, 1, out)
            self.assertIn("is a junction", out)
            code, out = run(["--yes", "--agents", "claude"], home)
            self.assertEqual(code, 0, out)
            self.assertFalse(writing.is_junction())
            self.assertTrue((source / "final-scan.md").is_file())


if __name__ == "__main__":
    unittest.main()
