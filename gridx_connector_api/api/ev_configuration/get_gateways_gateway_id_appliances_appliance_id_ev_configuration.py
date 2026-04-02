from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200 import (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_403 import (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_404 import (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_422 import (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_500 import (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/ev/configuration".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Retrieve an EV configuration

     Returns an EV charging station's configuration.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Retrieve an EV configuration

     Returns an EV charging station's configuration.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Retrieve an EV configuration

     Returns an EV charging station's configuration.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Retrieve an EV configuration

     Returns an EV charging station's configuration.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
        )
    ).parsed
