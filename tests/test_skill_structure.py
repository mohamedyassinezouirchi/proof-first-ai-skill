import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SkillStructureTests(unittest.TestCase):
    def test_skill_file_present(self):
        self.assertTrue((ROOT / "SKILL.md").is_file())

    def test_skill_frontmatter(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        self.assertIn("name: proof-first-release-audit", content)
        self.assertIn("description:", content)

    def test_statuses(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for status in ("PASS", "FAIL", "BLOCKED", "NOT VERIFIED", "NOT APPLICABLE"):
            self.assertIn(status, content)

    def test_template_present(self):
        self.assertIn("Evidence ledger", (ROOT / "references/report-template.md").read_text(encoding="utf-8"))

    def test_example_marked_synthetic(self):
        self.assertIn("synthetic example", (ROOT / "examples/example-report.md").read_text(encoding="utf-8").lower())

if __name__ == "__main__":
    unittest.main()
