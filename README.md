# Gridx Connector

<h3 align="center">This is not an Official GridX Library</h3>

> **⚠️ Deprecation Notice — Viessmann realm**
> The Viessmann realm was shut down at the end of 2025. The `viessmann` OEM is deprecated
> and will be removed in a future major release. Please switch to **eon Home**.

Harness the power of your photovoltaic system with the GridboxConnector library. This versatile tool taps into the same REST API as the official dashboard and app, providing you with direct access to your data from the cloud.

Whether you're a developer looking to integrate solar data into your own project, or a power user seeking command-line access, GridboxConnector has you covered.

**Take control of your solar data with GridboxConnector, and unlock the full potential of your photovoltaic system.**

![Screenshot vom mygridbox](images/screenshot.png)

## Supported Realms

| Realm | Status |
|---|---|
| **eon Home** | ✅ Active |
| Viessmann | ⚠️ Deprecated — shut down end of 2025 |

## Installation

```shell
pip install gridx-connector
# or with uv
uv add gridx-connector
```

## Usage

Use your login credentials from the app or from <https://company.gridx.de/login>.

### CLI

The `gridx` command authenticates with your credentials, discovers all energy systems
linked to your account, and prints their current live measurements to stdout as JSON.

```
usage: gridx [-h] -u USERNAME -p PASSWORD [-o {eon-home}]

options:
  -h, --help            show this help message and exit
  -u, --username        Login username (e-mail address from the app)
  -p, --password        Login password
  -o, --oem             OEM configuration to use (default: eon-home)
```

**Examples**

```shell
# Minimal — prints live data for all systems on your account
gridx -u your@email.com -p yourpassword

# Explicit OEM (currently only eon-home is supported)
gridx -u your@email.com -p yourpassword -o eon-home

# Pretty-print with jq
gridx -u your@email.com -p yourpassword | jq .

# Store the result in a file
gridx -u your@email.com -p yourpassword > live.json
```

**What the command does internally**

1. Loads `eon-home.config.json` bundled with the package.
2. Exchanges your credentials for an OAuth2 token via Auth0.
3. Calls `GET /systems` to discover all energy systems on your account.
4. Calls `GET /systems/{id}/live` for each system.
5. Prints the combined list of measurement dicts as JSON to stdout.

### As a library

```python
from gridx_connector import GridboxConnector, SupportedOEM
from importlib.resources import files
import json

config_file = files("gridx_connector").joinpath("config", f"{SupportedOEM.EON_HOME}.config.json")
with open(config_file) as f:
    config = json.load(f)

config["login"]["username"] = "your@email.com"
config["login"]["password"] = "yourpassword"

connector = GridboxConnector(config)

# Live data (all systems)
live_data = connector.retrieve_live_data()

# Historical data
historical = connector.retrieve_historical_data(
    start="2024-01-01T00:00:00+01:00",
    end="2024-01-02T00:00:00+01:00",
    resolution="1h",  # 15m | 1h | 1d | 1w | 1M
)
```

### Example Output

```json
{
    "consumption": 496,
    "directConsumption": 413,
    "directConsumptionEV": 0,
    "directConsumptionHeatPump": 0,
    "directConsumptionHeater": 0,
    "directConsumptionHousehold": 413,
    "directConsumptionRate": 1,
    "grid": 83,
    "gridMeterReadingNegative": 4318200000,
    "gridMeterReadingPositive": 14499360000,
    "measuredAt": "2023-08-04T11:29:43Z",
    "photovoltaic": 413,
    "production": 413,
    "selfConsumption": 413,
    "selfConsumptionRate": 1,
    "selfSufficiencyRate": 0.8326612903225806,
    "selfSupply": 413,
    "totalConsumption": 496
}
```

## How it works — Getting your data step by step

The diagram below shows the full journey from credentials to measurements.

```
┌─────────────────────────────────────────────────────────────┐
│  1. Load config                                             │
│     Read eon-home.config.json (or set USERNAME / PASSWORD   │
│     env vars to avoid storing credentials in a file).       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Authenticate  (OAuth2 / Auth0)                          │
│     GridboxConnector calls POST /oauth/token on the login   │
│     URL with your credentials and receives an id_token.     │
│     The token is refreshed automatically when it expires.   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Discover systems  (GET /systems)                        │
│     The connector fetches all energy systems linked to your │
│     account and stores their UUIDs in connector.gateways.   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  4a. Live data  (GET /systems/{id}/live)                    │
│      Returns the latest snapshot: PV production, grid feed- │
│      in/draw, battery state, household consumption, etc.    │
├─────────────────────────────────────────────────────────────┤
│  4b. Historical data  (GET /systems/{id}/historical)        │
│      Returns measurements aggregated over a time interval   │
│      and a chosen resolution (15m / 1h / 1d / 1w / 1M).    │
└─────────────────────────────────────────────────────────────┘
```

### Minimal working example

```python
import json
from importlib.resources import files
from gridx_connector import GridboxConnector, SupportedOEM

# 1. Load config
config_path = files("gridx_connector").joinpath("config", f"{SupportedOEM.EON_HOME}.config.json")
config = json.loads(config_path.read_text())

# Inject credentials (or set USERNAME / PASSWORD env vars instead)
config["login"]["username"] = "your@email.com"
config["login"]["password"] = "yourpassword"

# 2+3. Authenticate and discover systems automatically
connector = GridboxConnector(config)
print("Systems found:", connector.get_gateways())

# 4a. Live snapshot for all systems
for measurement in connector.retrieve_live_data():
    print(f"PV: {measurement['photovoltaic']} W  "
          f"Grid: {measurement['grid']} W  "
          f"Consumption: {measurement['consumption']} W")

# 4b. Yesterday's data in 1-hour buckets
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
historical = connector.retrieve_historical_data(
    start=f"{yesterday}T00:00:00+01:00",
    end=f"{yesterday}T23:59:59+01:00",
    resolution="1h",   # 15m | 1h | 1d | 1w | 1M
)
for entry in historical:
    for bucket in entry.get("measurements", []):
        print(bucket["measuredAt"], "→", bucket["photovoltaic"], "W")
```

### Credential handling

| Option | How |
|---|---|
| Config file | Set `login.username` / `login.password` in `eon-home.config.json` |
| Environment variables | Export `USERNAME=...` and `PASSWORD=...` — these override the config file |
| CLI | Pass `-u <user> -p <pass>` on the command line |

## Examples

Ready-to-run scripts are in the [`examples/`](examples/) directory:

| Script | Description |
|---|---|
| [`read_live_data.py`](examples/read_live_data.py) | Poll live data every 60 s |
| [`historical_data.py`](examples/historical_data.py) | Fetch today's historical data |
| [`openapi_test.py`](examples/openapi_test.py) | Use the low-level `gridx_connector_api` client directly |

## Generated API Client

`gridx_connector_api/` is an auto-generated Python client derived directly from
[`APIDefinition/openapi.json`](APIDefinition/openapi.json) using
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

The client is regenerated automatically via GitHub Actions whenever `openapi.json` changes.
To regenerate locally after replacing `openapi.json`:

```shell
uv sync --dev
bash scripts/generate_client.sh
```

## Dependencies

- `requests` — HTTP client
- `authlib` — OAuth2 authentication

## License

MIT


## Contributing

If you'd like to contribute to gridx-connector, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and write tests if possible.
Run tests and ensure they pass.
Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
