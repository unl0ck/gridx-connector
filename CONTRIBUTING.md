# Contributing to gridx-connector

## Prerequisites

- [uv](https://docs.astral.sh/uv/) — the Python package manager used by this project
- Python 3.11+

## Dev Setup

```shell
git clone https://github.com/unl0ck/gridx-connector.git
cd gridx-connector
uv sync --dev
```

`uv sync --dev` creates a virtual environment in `.venv/` and installs all dependencies
(including dev tools like `ruff`, `pytest`, `openapi-python-client`).

After cloning you must also generate the API client, which is **not stored in git**:

```shell
bash scripts/generate_client.sh
```

This creates `gridx_connector_api/` locally from `APIDefinition/openapi.json`.
Run it again whenever `openapi.json` changes.

## Running Tests

```shell
uv run pytest
```

For verbose output:

```shell
uv run pytest -v
```

## Linting & Formatting

```shell
uv run ruff check .        # lint
uv run ruff format .       # auto-format
uv run ruff format --check .   # check only (no writes)
```

The CI pipeline runs both checks. Fix all lint issues before opening a PR.

## Updating the OpenAPI Client (`gridx_connector_api`)

`gridx_connector_api/` is auto-generated from `APIDefinition/openapi.json` using
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
**It is not stored in git** — it lives only on your local checkout and inside built wheels.

### Why it is not committed

The directory contains ~1 500 generated files that change wholesale with every
regeneration. Keeping them out of git keeps diffs readable and avoids merge
conflicts on upstream OpenAPI spec updates.

### How it ends up in the published wheel

The GitHub Actions publish workflow ([`python-publish.yml`](.github/workflows/python-publish.yml))
runs `bash scripts/generate_client.sh` before `uv build`, so every wheel
shipped to PyPI contains a freshly generated `gridx_connector_api/`.

### When to regenerate locally

```shell
# Replace APIDefinition/openapi.json with the new spec, then:
bash scripts/generate_client.sh
# Commit only the updated openapi.json (not the generated code):
git add APIDefinition/openapi.json
git commit -m "chore: update OpenAPI spec"
```

The GitHub Actions workflow [`generate-client.yml`](.github/workflows/generate-client.yml)
runs this automatically on every push that changes `APIDefinition/openapi.json`.

## OEM Config Files

OEM-specific auth configuration lives in `gridx_connector/config/`:

| File | Realm | Status |
|---|---|---|
| `eon-home.config.json` | eon-home-authentication-db | ✅ Active |
| `viessmann.config.json` | viessmann-authentication-db | ⚠️ Deprecated |

To add a new OEM, create a new `<oem-name>.config.json` following the same structure and
add the OEM name to `gridx_connector/cli.py`'s `_ALL_OEMS` list.

## Release Process

Versions follow [SemVer](https://semver.org/). The release workflow uses
[bump-my-version](https://github.com/callowayproject/bump-my-version).

1. Run the **Version Workflow** in GitHub Actions and select the bump type
   (`patch` / `minor` / `major`). This commits a version bump and creates a git tag.
2. Create a **GitHub Release** from that tag.
3. The **publish workflow** fires automatically and pushes the new version to PyPI via
   OIDC Trusted Publishing (no API token required).

To bump locally:

```shell
uvx bump-my-version bump patch   # or minor / major
```
