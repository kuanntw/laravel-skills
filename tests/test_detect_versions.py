import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/laravel-vibe/scripts/detect_versions.py"
SPEC = importlib.util.spec_from_file_location("detect_versions", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DetectVersionsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name)

    def write_lock(self, packages, dev=None):
        data = {"packages": packages}
        if dev is not None:
            data["packages-dev"] = dev
        (self.project / "composer.lock").write_text(json.dumps(data), encoding="utf-8")
        return MODULE.detect(self.project)

    def test_fixture_major_routes(self):
        for name, major in (("laravel10-livewire2", 10), ("laravel12-livewire3", 12), ("laravel13-livewire4", 13)):
            with self.subTest(fixture=name):
                text = (ROOT / f"tests/fixtures/{name}.json").read_text(encoding="utf-8")
                (self.project / "composer.lock").write_text(text, encoding="utf-8")
                result = MODULE.detect(self.project)
                self.assertEqual("detected", result["status"])
                self.assertEqual(f"{major}.x", result["laravel_docs_series"])
                self.assertEqual(major, result["packages"]["laravel/framework"]["major"])

    def test_laravel11_and_absent_optional_packages(self):
        result = self.write_lock([{"name": "laravel/framework", "version": "11.1.0"}])
        self.assertEqual("detected", result["status"])
        self.assertEqual("11.x", result["laravel_docs_series"])
        self.assertNotIn("livewire/livewire", result["packages"])

    def test_reads_dev_versions_and_ignores_json_constraint(self):
        (self.project / "composer.json").write_text('{"require":{"laravel/framework":"^13.0"}}')
        result = self.write_lock([{"name": "laravel/framework", "version": "v12.3.0"}],
                                 [{"name": "pestphp/pest", "version": "3.0.0"}])
        self.assertEqual("12.x", result["laravel_docs_series"])
        self.assertEqual("packages-dev", result["packages"]["pestphp/pest"]["section"])

    def test_missing_lock_does_not_fallback_to_composer_json(self):
        (self.project / "composer.json").write_text('{"require":{"laravel/framework":"^12.0"}}')
        self.assertEqual("needs_confirmation", MODULE.detect(self.project)["status"])

    def test_bad_input_shapes_fail_closed(self):
        for raw in ("{", "[]", "{}", '{"packages":null}', '{"packages":[null]}',
                    '{"packages":[{"name":7}]}', '{"packages":[],"packages-dev":{}}',
                    '{"packages":[],"packages":[]}'):
            with self.subTest(raw=raw):
                (self.project / "composer.lock").write_text(raw)
                self.assertEqual("needs_confirmation", MODULE.detect(self.project)["status"])

    def test_non_utf8_is_handled(self):
        (self.project / "composer.lock").write_bytes(b"\xff")
        self.assertEqual("needs_confirmation", MODULE.detect(self.project)["status"])

    def test_lock_directory_is_handled(self):
        (self.project / "composer.lock").mkdir()
        self.assertEqual("needs_confirmation", MODULE.detect(self.project)["status"])

    def test_oversize_lock_is_handled(self):
        original = MODULE.MAX_LOCK_BYTES
        self.addCleanup(setattr, MODULE, "MAX_LOCK_BYTES", original)
        MODULE.MAX_LOCK_BYTES = 4
        self.write_lock([])
        self.assertEqual("needs_confirmation", MODULE.detect(self.project)["status"])

    def test_dev_alias_prerelease_and_constraints_need_confirmation(self):
        for version in ("dev-main", "12.x-dev", "v12.0.0-beta.1", "^12.0", "12", "12.0", "",
                        "12.0.0+.", "12.0.0+a..b", "12.0.0+", "12.00.01", "012.0.0"):
            with self.subTest(version=version):
                result = self.write_lock([{"name": "laravel/framework", "version": version}])
                self.assertEqual("needs_confirmation", result["status"])
                self.assertIsNone(result["laravel_docs_series"])

    def test_unsafe_version_tokens_are_not_echoed(self):
        for version in ("12.0.0\nSECRET", "\x1b[31m12.0.0", "12.0.0 SECRET", "<script>", "v" * 201):
            with self.subTest(version=repr(version)):
                result = self.write_lock([{"name": "laravel/framework", "version": version}])
                self.assertEqual("needs_confirmation", result["status"])
                self.assertEqual({}, result["packages"])
                self.assertNotIn("SECRET", json.dumps(result))

    def test_invalid_version_type_is_handled(self):
        result = self.write_lock([{"name": "laravel/framework", "version": 12}])
        self.assertEqual("needs_confirmation", result["status"])

    def test_stable_build_metadata_is_supported(self):
        result = self.write_lock([{"name": "laravel/framework", "version": "v12.0.1+build.1"}])
        self.assertEqual("detected", result["status"])

    def test_missing_framework_does_not_infer_from_illuminate(self):
        result = self.write_lock([{"name": "illuminate/support", "version": "v12.0.0"}])
        self.assertEqual("needs_confirmation", result["status"])
        self.assertIsNone(result["laravel_docs_series"])

    def test_unknown_major_never_routes_to_latest(self):
        for major in (9, 99):
            with self.subTest(major=major):
                result = self.write_lock([{"name": "laravel/framework", "version": f"{major}.0.0"}])
                self.assertEqual("needs_confirmation", result["status"])
                self.assertIsNone(result["laravel_docs_series"])

    def test_duplicate_relevant_package_is_not_silently_selected(self):
        result = self.write_lock([{"name": "laravel/framework", "version": "12.0.0"}],
                                 [{"name": "laravel/framework", "version": "13.0.0"}])
        self.assertEqual("needs_confirmation", result["status"])
        self.assertEqual({}, result["packages"])

    def test_filament_major_conflict_needs_confirmation(self):
        result = self.write_lock([
            {"name": "laravel/framework", "version": "12.0.0"},
            {"name": "filament/panels", "version": "3.0.0"},
            {"name": "filament/forms", "version": "4.0.0"},
        ])
        self.assertEqual("needs_confirmation", result["status"])
        self.assertTrue(any("disagree" in warning for warning in result["warnings"]))

    def test_unknown_or_dev_optional_package_needs_confirmation(self):
        for name, version in (("livewire/livewire", "9.0.0"), ("laravel/boost", "dev-main")):
            with self.subTest(package=name):
                result = self.write_lock([
                    {"name": "laravel/framework", "version": "12.0.0"},
                    {"name": name, "version": version},
                ])
                self.assertEqual("needs_confirmation", result["status"])

    def test_does_not_execute_composer_scripts_or_emit_unrelated_data(self):
        (self.project / "composer.json").write_text('{"scripts":{"post-install-cmd":"touch SENTINEL"}}')
        result = self.write_lock([
            {"name": "laravel/framework", "version": "12.0.0", "source": {"url": "PRIVATE-URL"}},
            {"name": "private/package", "version": "SECRET"},
        ])
        self.assertNotIn("PRIVATE-URL", json.dumps(result))
        self.assertNotIn("SECRET", json.dumps(result))
        self.assertFalse((self.project / "SENTINEL").exists())

    def test_cli_exit_codes_and_read_only_files(self):
        command = [sys.executable, str(SCRIPT), str(self.project)]
        missing = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(2, missing.returncode)
        self.assertEqual("needs_confirmation", json.loads(missing.stdout)["status"])
        self.write_lock([{"name": "laravel/framework", "version": "12.0.0"}])
        before = {path.name: path.read_bytes() for path in self.project.iterdir()}
        detected = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(0, detected.returncode)
        self.assertEqual("detected", json.loads(detected.stdout)["status"])
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.project.iterdir()})


if __name__ == "__main__":
    unittest.main()
