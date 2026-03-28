import json
import time
from importlib.resources import files

from gridx_connector import GridboxConnector

loop = True
config_file = files("gridx_connector").joinpath("config", "eon-home.config.json")
with open(config_file) as file:
    data = json.load(file)
    data["login"]["username"] = "username"
    data["login"]["password"] = "password"
    connector = GridboxConnector(data)
    live_data = connector.retrieve_live_data()
    print(live_data)
    while loop:
        live_data = connector.retrieve_live_data()
        print(live_data)
        time.sleep(60)
