#!/usr/bin/env python3
"""Read selected locked package versions without loading PHP or running Composer."""

import argparse
import json
from pathlib import Path
import re

PACKAGES = (
    "laravel/framework",
    "livewire/livewire",
    "filament/filament",
    "filament/panels",
    "filament/forms",
    "filament/tables",
    "filament/actions",
    "filament/schemas",
    "laravel/boost",
    "pestphp/pest",
    "phpunit/phpunit",
)
GUIDANCE_MAJORS = {
    "laravel/framework": {10, 11, 12, 13},
    "livewire/livewire": {2, 3, 4},
}
STABLE_VERSION = re.compile(
    r"v?(0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
SAFE_VERSION_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+/-]{0,199}")
MAX_LOCK_BYTES = 16 * 1024 * 1024


def unique_object(pairs):
    """Do not silently accept duplicate JSON keys in version evidence."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def detect(project):
    result = {
        "source": "composer.lock",
        "status": "needs_confirmation",
        "packages": {},
        "laravel_docs_series": None,
        "warnings": [],
    }
    warnings = result["warnings"]
    try:
        with (Path(project) / "composer.lock").open("rb") as lock:
            contents = lock.read(MAX_LOCK_BYTES + 1)
        if len(contents) > MAX_LOCK_BYTES:
            raise ValueError("lock too large")
        data = json.loads(contents.decode("utf-8"), object_pairs_hook=unique_object)
        if not isinstance(data, dict) or "packages" not in data:
            raise ValueError("missing packages")
        for section in ("packages", "packages-dev"):
            entries = data.get(section, [])
            if not isinstance(entries, list):
                raise ValueError("invalid package list")
            for entry in entries:
                if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
                    raise ValueError("invalid package record")
                name = entry["name"]
                if name not in PACKAGES:
                    continue
                if name in result["packages"]:
                    raise ValueError("duplicate relevant package")
                version = entry.get("version")
                if not isinstance(version, str) or not SAFE_VERSION_TOKEN.fullmatch(version):
                    raise ValueError("invalid relevant version")
                match = STABLE_VERSION.fullmatch(version)
                major = int(match.group(1)) if match else None
                result["packages"][name] = {
                    "version": version,
                    "major": major,
                    "section": section,
                }
                supported = {2, 3, 4, 5} if name.startswith("filament/") else GUIDANCE_MAJORS.get(name)
                if major is None:
                    warnings.append(f"{name}: non-stable version; confirm exact documentation manually")
                elif supported is not None and major not in supported:
                    warnings.append(f"{name}: no reviewed guidance for this major")
    except (OSError, UnicodeError, ValueError, RecursionError):
        # Never echo lock contents, repository URLs, or filesystem exception text.
        result["packages"] = {}
        warnings[:] = ["composer.lock is missing, unreadable, too large, or malformed; confirm versions manually"]
        return result

    laravel = result["packages"].get("laravel/framework")
    if laravel is None:
        warnings.append("laravel/framework is absent from composer.lock; do not infer Laravel from constraints or components")
    elif laravel["major"] in GUIDANCE_MAJORS["laravel/framework"]:
        result["laravel_docs_series"] = f"{laravel['major']}.x"

    filament_majors = {
        package["major"]
        for name, package in result["packages"].items()
        if name.startswith("filament/") and package["major"] is not None
    }
    if len(filament_majors) > 1:
        warnings.append("Filament package majors disagree; confirm the project dependency state")
    if not warnings:
        result["status"] = "detected"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Target application directory containing composer.lock")
    args = parser.parse_args()
    result = detect(args.project)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "detected" else 2


if __name__ == "__main__":
    raise SystemExit(main())
