"""Preserve the intentionally unsafe baseline rather than silently fixing it."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "labs" / "01-vulnerable-file-agent"
spec = importlib.util.spec_from_file_location("enrion_lab01_tools", LAB / "tools.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BaselineTests(unittest.TestCase):
    def test_synthetic_restricted_file_is_exposed(self):
        self.assertIn("ENRION_FAKE_SECRET=", module.read_file("restricted/secret.txt"))

    def test_workspace_escape_is_blocked(self):
        with self.assertRaises(ValueError):
            module.read_file("../tools.py")

    def test_offline_baseline_reproduces_exposure(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(LAB / "offline_demo.py")],
                                text=True, encoding="utf-8", capture_output=True, check=True)
        self.assertIn("[SECURITY RESULT] SECRET EXPOSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
