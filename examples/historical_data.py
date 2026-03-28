import json
import time
from datetime import datetime, timedelta, timezone
from importlib.resources import files

from gridx_connector import GridboxConnector

now = datetime.now(timezone(timedelta(hours=1)))
now = now.replace(hour=0, minute=0, second=0, microsecond=0)

today = now.isoformat()
tomorrow = now + timedelta(days=1)

loop = False
config_file = files("gridx_connector").joinpath("config", "eon-home.config.json")
with open(config_file) as file:
    data = json.load(file)
    data["login"]["username"] = "username"
    data["login"]["password"] = "password"
    connector = GridboxConnector(data)
    historical_data = connector.retrieve_historical_data(start=today, end=tomorrow.isoformat())
    print(historical_data)
    while loop:
        historical_data = connector.retrieve_historical_data(start=today, end=tomorrow.isoformat())
        print(historical_data)
        time.sleep(60)
