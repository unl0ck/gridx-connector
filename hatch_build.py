"""Build hook to generate gridx_connector_api during package builds.

gridx_connector_api/ is normally committed to the repository so no
regeneration is needed at build time.  This hook only runs the generator
when the directory is missing (e.g. a fresh checkout that predates the
committed package).  Run ``bash scripts/generate_client.sh`` manually
whenever the OpenAPI definition changes and commit the result.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    """Generate the OpenAPI client package when it is not already present."""

    def initialize(self, version: str, build_data: dict) -> None:
        root = Path(self.root)
        package_dir = root / "gridx_connector_api"

        # Skip generation if the package is already present (normal case).
        if package_dir.exists() and any(package_dir.iterdir()):
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "out"
            output_dir.mkdir(parents=True, exist_ok=True)

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "openapi_python_client",
                    "generate",
                    "--config",
                    str(root / "APIDefinition" / "openapi-client-config.yml"),
                    "--path",
                    str(root / "APIDefinition" / "openapi.json"),
                    "--output-path",
                    str(output_dir),
                    "--overwrite",
                ],
                check=True,
                cwd=root,
            )

            generated_package = next(output_dir.rglob("gridx_connector_api"), None)
            if generated_package is None:
                raise RuntimeError("gridx_connector_api generation failed")

            shutil.copytree(generated_package, package_dir)
