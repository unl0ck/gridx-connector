from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_appliance_id_response_403 import (
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_response_404 import (
    GetGatewaysGatewayIDAppliancesApplianceIDResponse404,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_response_422 import (
    GetGatewaysGatewayIDAppliancesApplianceIDResponse422,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_response_500 import (
    GetGatewaysGatewayIDAppliancesApplianceIDResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesApplianceIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesApplianceIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetGatewaysGatewayIDAppliancesApplianceIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesApplianceIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
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
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Retrieve an Appliance

     Retrieves the details of an existing appliance.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDResponse500]
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
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Retrieve an Appliance

     Retrieves the details of an existing appliance.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
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
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Retrieve an Appliance

     Retrieves the details of an existing appliance.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDResponse500]
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
    GetGatewaysGatewayIDAppliancesApplianceIDResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Retrieve an Appliance

     Retrieves the details of an existing appliance.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
        )
    ).parsed
