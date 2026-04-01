"""Build hook to generate gridx_connector_api during package builds."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    """Generate the OpenAPI client package before building artifacts."""

    def initialize(self, version: str, build_data: dict) -> None:
        root = Path(self.root)
        package_dir = root / "gridx_connector_api"
        if package_dir.exists():
            shutil.rmtree(package_dir)

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
