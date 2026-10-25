"""Lightweight repository checks; these do not execute Laravel or PHP examples."""

import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/laravel-vibe"


class RepositoryTests(unittest.TestCase):
    def test_standard_entry_is_thin_and_preserves_governance(self):
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(entry.startswith("---\nname: laravel-vibe\ndescription: "))
        self.assertLess(len(entry.splitlines()), 40)
        self.assertIn("SKILLS_INDEX.md", entry)
        self.assertIn("根目錄存在 `WORKFLOW.md`", entry)
        self.assertNotIn("../../WORKFLOW.md", entry)
        self.assertNotIn("allowed-tools:", entry)

    def test_all_indexed_skills_resolve_once(self):
        index = (SKILL / "SKILLS_INDEX.md").read_text(encoding="utf-8")
        slugs = re.findall(r"^\| \d+ \| `([^`]+)`", index, flags=re.MULTILINE)
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertIn("version-detection-and-routing", slugs)
        self.assertIn("authorization-and-tenant-tests", slugs)
        for slug in slugs:
            with self.subTest(skill=slug):
                matches = list(SKILL.glob(f"[0-9]*/*{slug}.md"))
                self.assertEqual(1, len(matches), f"Missing or ambiguous indexed skill: {slug}")
        indexed = {path.resolve() for slug in slugs for path in SKILL.glob(f"[0-9]*/{slug}.md")}
        self.assertEqual(indexed, {path.resolve() for path in SKILL.glob("[0-9]*/*.md")})

    def test_relative_markdown_links_resolve_inside_repository(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            # This repo uses simple inline links; ignore examples inside fenced code.
            content = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
            for target in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", content):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    resolved = (path.parent / unquote(parsed.path)).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.exists(), f"Broken link: {target}")

    def test_security_matrix_has_explicit_acceptance_ids(self):
        matrix = (SKILL / "templates/security-acceptance-matrix.md").read_text(encoding="utf-8")
        for case in ("AUTH-01", "AUTH-02", "AUTH-03", "VAL-01", "TEN-01", "TEN-02", "TEN-03", "TEN-04", "TEN-05", "MASS-01", "MASS-02", "QUERY-01", "QUERY-02"):
            with self.subTest(case=case):
                self.assertEqual(1, matrix.count(f"| {case} "))

    def test_skill_package_relative_links_are_portable(self):
        for path in SKILL.rglob("*.md"):
            content = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
            for target in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", content):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                with self.subTest(file=str(path.relative_to(SKILL)), target=target):
                    self.assertTrue((path.parent / unquote(parsed.path)).resolve().is_relative_to(SKILL))

    def test_json_leak_example_checks_decoded_nested_text(self):
        example = (SKILL / "templates/authorization-test-example.md").read_text(encoding="utf-8")
        self.assertIn("json_decode($response->getContent(), true, 512, JSON_THROW_ON_ERROR)", example)
        self.assertIn("JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR", example)
        self.assertIn("assertStringNotContainsString('B 的標題', $normalized)", example)
        self.assertNotIn("assertDontSee('B 的標題')", example)
        # Demonstrate the regression payload; this is not execution of the PHP template.
        protected = "B 的標題"
        raw = json.dumps({"error": {"message": f"Cannot access {protected}"}}, ensure_ascii=True)
        self.assertNotIn(protected, raw)
        self.assertIn(protected, json.dumps(json.loads(raw), ensure_ascii=False))


if __name__ == "__main__":
    unittest.main()
