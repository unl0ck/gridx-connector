import argparse
from gridx_connector import GridboxConnector
from importlib.resources import files
import json
from supported_oem import SupportedOEM

def retrieve_live_data(username: str, password: str, oem: str = SupportedOEM.VIESSMANN):
    config_file = files('gridx_connector').joinpath(f'{oem}.config.json')
    with open(config_file, 'r') as file:
        data = json.load(file)
        data["login"]["username"] = username
        data["login"]["password"] = password
        connector = GridboxConnector(data)
        # Retrieve live data
        live_data = connector.retrieve_live_data()
        return live_data

def main():
    parser = argparse.ArgumentParser(description='Retrieve live data from GridX Gridbox.')
    parser.add_argument('-u', '--username', required=True, help='The username to use.')
    parser.add_argument('-p', '--password', required=True, help='The password to use.')
    parser.add_argument('-o', '--oem', default=SupportedOEM.VIESSMANN, help='The OEM configuration to use.', choices=[SupportedOEM.VIESSMANN, SupportedOEM.EON_HOME])
    args = parser.parse_args()

    live_data = retrieve_live_data(args.username, args.password, args.oem)
    print(live_data)

if __name__ == '__main__':
    main()