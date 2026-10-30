"""Tests for eis_ops.py. Run: python3 -m unittest discover eis-ops"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("eis_ops.py")


class EisOps(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.env = dict(os.environ, EIS_OPS_POINTER=str(self.tmp / "cfg" / "eis-ops-pointer.json"))

    def run_cmd(self, *args):
        r = subprocess.run([sys.executable, str(SCRIPT), *args], env=self.env, capture_output=True, text=True, check=True)
        return json.loads(r.stdout)

    def test_flow(self):
        self.assertEqual(self.run_cmd("find")["status"], "missing")
        self.assertEqual(self.run_cmd("resolve", str(self.tmp))["status"], "absent")
        r = self.run_cmd("init", str(self.tmp))
        ops = self.tmp / "eis-ops"
        self.assertEqual((r["status"], r["pointer"]), ("created", "written"))
        self.assertEqual((ops / "CLAUDE.md").read_text(), "@AGENTS.md\n")
        self.assertEqual(self.run_cmd("find"), {"status": "found", "path": str(ops.resolve())})
        self.run_cmd("register", "--plugin", "eis-task-manager", "--desc", "Daily | tasks")
        self.run_cmd("register", "--plugin", "eis-answer", "--desc", "Replies")
        self.assertTrue((ops / "task-manager").is_dir())
        (ops / "task-manager").rmdir()
        self.run_cmd("register", "--plugin", "eis-answer", "--desc", "Replies v2")
        text = (ops / "AGENTS.md").read_text()
        self.assertIn("| eis-task-manager | task-manager/ | Daily / tasks | not_found |", text)
        self.assertIn("| eis-answer | answer/ | Replies v2 | active |", text)
        self.assertEqual(text.count("eis-answer"), 1)

    def test_existing_folder_keeps_files_and_rewrites_pointer(self):
        ops = self.tmp / "eis-ops"
        (ops / "other").mkdir(parents=True)
        (ops / "AGENTS.md").write_text("mine\n")
        self.assertEqual(self.run_cmd("resolve", str(ops))["status"], "exists")
        r = self.run_cmd("init", str(ops))
        self.assertEqual(r["status"], "existing")
        self.assertEqual((ops / "AGENTS.md").read_text(), "mine\n")
        self.assertTrue((ops / "other").is_dir())
        self.assertEqual(self.run_cmd("find")["status"], "found")

    def test_stale_pointer(self):
        self.run_cmd("init", str(self.tmp / "x"))
        (self.tmp / "x" / "eis-ops" / "AGENTS.md").unlink()
        (self.tmp / "x" / "eis-ops" / "CLAUDE.md").unlink()
        (self.tmp / "x" / "eis-ops").rmdir()
        self.assertEqual(self.run_cmd("find")["status"], "stale")


if __name__ == "__main__":
    unittest.main()
