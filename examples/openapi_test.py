# Example: direct usage of the auto-generated gridx_connector_api client.
# Run `bash scripts/generate_client.sh` first to create gridx_connector_api/.
import json
import logging
import os
from importlib.resources import files

from authlib.integrations.requests_client import OAuth2Session
from gridx_connector_api import AuthenticatedClient
from gridx_connector_api.api.gateway.get_gateways import sync as get_gateways
from gridx_connector_api.api.gateway.get_gateways_gateway_id import sync as get_gateway
from gridx_connector_api.api.system.get_systems import sync as get_systems
from gridx_connector_api.api.system.get_systems_system_id_historical import sync_detailed as get_historical_data
from gridx_connector_api.api.system.get_systems_system_id_live import sync_detailed as get_live_data


class GridboxConnector:
    def __init__(self, config):
        self.config = config
        self.login_url = config["urls"]["login"]
        self.login_body = config["login"]
        self.gateway_url = config["urls"]["gateways"]
        self.gateways = []
        self.token = None
        self.oauth_client = None
        self.client: AuthenticatedClient = None
        self.logger = logging.getLogger(__name__)
        self._init_oauth()
        self._fetch_token()
        self.client = AuthenticatedClient(base_url="https://api.gridx.de", token=self.token["id_token"])
        self.get_gateways()

    def _init_oauth(self):
        self.oauth_client = OAuth2Session(
            self.login_body["client_id"],
            self.login_body["client_secret"],
            scope=self.login_body["scope"],
        )

    def _fetch_token(self):
        self.token = self.oauth_client.fetch_token(
            self.login_url,
            username=self.login_body["username"],
            password=self.login_body["password"],
            grant_type=self.login_body["grant_type"],
            audience=self.login_body["audience"],
            realm=self.login_body["realm"],
            scope=self.login_body["scope"],
        )

    def get_gateways(self):
        self.gateways = get_gateways(client=self.client)
        return self.gateways

    def get_systems(self):
        return get_systems(client=self.client)

    def get_live_data(self, system_id):
        return get_live_data(client=self.client, system_id=system_id)

    def get_historical_data(self, system_id):
        return get_historical_data(client=self.client, system_id=system_id)


if __name__ == "__main__":
    config_file = files("gridx_connector").joinpath("config", "eon-home.config.json")
    with open(config_file) as file:
        data = json.load(file)
        data["login"]["username"] = os.environ["GRIDX_USERNAME"]
        data["login"]["password"] = os.environ["GRIDX_PASSWORD"]
        connector = GridboxConnector(data)
        systems = connector.get_systems()
        system_id = systems[0]["id"]
        live_data = connector.get_live_data(system_id)
        print(live_data)


class GridboxConnector:
    def __init__(self, config):
        self.config = config
        self.login_url = config["urls"]["login"]
        self.login_body = config["login"]
        self.gateway_url = config["urls"]["gateways"]
        self.live_url = config["urls"]["live"]
        self.historical_url = config["urls"]["historical"]
        self.username = os.getenv("USERNAME", self.login_body["username"])
        self.password = os.getenv("PASSWORD", self.login_body["password"])
        self.gateways = []
        self.token = None
        self.oauth_client = None
        self.client: AuthenticatedClient = None
        self.logger = None
        self.init_logging()
        self.get_oauth_client()
        self.get_token()
        self.client = self.get_client()

        self.get_gateways()

    def init_logging(self):
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_oauth_client(self) -> OAuth2Session:
        if self.oauth_client is None:
            client_id = self.login_body["client_id"]
            client_secret = self.login_body["client_secret"]
            self.oauth_client = OAuth2Session(client_id, client_secret, scope=self.login_body["scope"])
        return self.oauth_client

    def get_client(self) -> AuthenticatedClient:
        if self.client is None:
            self.client = AuthenticatedClient(base_url="https://api.gridx.de", token=self.token["id_token"])
        return self.client

    def get_token(self) -> dict:
        self.token = self.oauth_client.fetch_token(
            self.login_url,
            username=self.login_body["username"],
            password=self.login_body["password"],
            grant_type=self.login_body["grant_type"],
            audience=self.login_body["audience"],
            realm=self.login_body["realm"],
            scope=self.login_body["scope"],
        )
        self.logger.debug(f"Token expires at {self.token['expires_at']}")
        return self.token

    def get_gateways(self):
        response = get_gateways(client=self.get_client())
        self.gateways = response
        return self.gateways

    def get_gateway(self, gateway_id):
        response = get_gateway(client=self.get_client(), gateway_id=gateway_id)
        return response

    def get_systems(self):
        response = get_systems(client=self.get_client())
        return response

    def get_live_data(self, system_id):
        response = get_live_data(client=self.get_client(), system_id=system_id)
        return response

    def get_historical_data(self, system_id):
        response = get_historical_data(client=self.get_client(), system_id=system_id)
        return response


if __name__ == "__main__":
    config_file = files("gridx_connector").joinpath("eon-home.config.json")
    with open(config_file) as file:
        data = json.load(file)
        connector = GridboxConnector(data)
        gateways = connector.get_gateways()
        gateway_id = gateways[0]["system"]
        systems = connector.get_systems()
        systems_id = systems[0]["id"]
        live_data = connector.get_live_data(systems_id)

        print(live_data)
