#!/usr/bin/env python3
"""Verify that the built wheel and sdist actually ship everything they must.

Guards against the hatchling gitignore pitfall that produced the broken
3.0.3/3.0.4 wheels on PyPI: gridx_connector_api/ is generated (gitignored)
and silently fell out of the build artifacts.

Usage: python3 scripts/verify_build_artifacts.py [dist_dir]
"""

from __future__ import annotations

import sys
import tarfile
import zipfile
from pathlib import Path

# The generated client currently has ~1500 files; anything far below that
# means generation or packaging silently failed.
MIN_API_FILES = 500

REQUIRED_FILES = (
    "gridx_connector/__init__.py",
    "gridx_connector/async_connector.py",
    "gridx_connector/config/eon-home.config.json",
    "gridx_connector/py.typed",
    "gridx_connector_api/__init__.py",
    "gridx_connector_api/py.typed",
)


def _check(kind: str, path: Path, names: list[str]) -> list[str]:
    # sdist paths are prefixed with "<name>-<version>/"; strip that.
    if kind == "sdist":
        names = ["/".join(n.split("/")[1:]) for n in names]

    errors = []
    api_count = sum(1 for n in names if n.startswith("gridx_connector_api/"))
    if api_count < MIN_API_FILES:
        errors.append(
            f"{path.name}: only {api_count} gridx_connector_api files "
            f"(expected >= {MIN_API_FILES}) — generated client is missing"
        )
    for required in REQUIRED_FILES:
        if required not in names:
            errors.append(f"{path.name}: missing {required}")
    if not errors:
        print(f"OK {path.name}: {api_count} gridx_connector_api files, all required files present")
    return errors


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    wheels = sorted(dist.glob("*.whl"))
    sdists = sorted(dist.glob("*.tar.gz"))

    errors = []
    if not wheels:
        errors.append(f"no wheel found in {dist}/")
    if not sdists:
        errors.append(f"no sdist found in {dist}/")

    for wheel in wheels:
        errors += _check("wheel", wheel, zipfile.ZipFile(wheel).namelist())
    for sdist in sdists:
        errors += _check("sdist", sdist, tarfile.open(sdist).getnames())

    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
