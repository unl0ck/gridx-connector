#!/usr/bin/env bash
# Regenerate gridx_connector_api from APIDefinition/openapi.json.
# Requires: uv sync --dev (openapi-python-client must be installed)
#
# Usage:
#   bash scripts/generate_client.sh
#   uv run bash scripts/generate_client.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "==> Generating gridx_connector_api from APIDefinition/openapi.json ..."

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

# openapi-python-client refuses to write into an existing directory without --overwrite,
# so we point it at a fresh sub-directory and let it create the project there.
OUTPUT_DIR="$TMP_DIR/out"
mkdir -p "$OUTPUT_DIR"

uv run openapi-python-client generate \
    --config APIDefinition/openapi-client-config.yml \
    --path APIDefinition/openapi.json \
    --output-path "$OUTPUT_DIR" \
    --overwrite

# The generated package lands at: $OUTPUT_DIR/<project-name>/gridx_connector_api/
PACKAGE_DIR="$(find "$OUTPUT_DIR" -type d -name "gridx_connector_api" | head -1)"

if [[ -z "$PACKAGE_DIR" ]]; then
    echo "ERROR: gridx_connector_api/ not found in generated output." >&2
    exit 1
fi

rm -rf "$REPO_ROOT/gridx_connector_api"
cp -r "$PACKAGE_DIR" "$REPO_ROOT/gridx_connector_api"

echo "==> Done. gridx_connector_api/ has been updated."
