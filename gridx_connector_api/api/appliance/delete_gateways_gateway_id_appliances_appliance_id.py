from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_gateways_gateway_id_appliances_appliance_id_response_403 import (
    DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403,
)
from ...models.delete_gateways_gateway_id_appliances_appliance_id_response_404 import (
    DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404,
)
from ...models.delete_gateways_gateway_id_appliances_appliance_id_response_422 import (
    DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422,
)
from ...models.delete_gateways_gateway_id_appliances_appliance_id_response_500 import (
    DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
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
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Delete an Appliance

     Deletes an appliances.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500]
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
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Delete an Appliance

     Deletes an appliances.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
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
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Delete an Appliance

     Deletes an appliances.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500]
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
    Any
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422
    | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Delete an Appliance

     Deletes an appliances.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse403 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse404 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse422 | DeleteGatewaysGatewayIDAppliancesApplianceIDResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
        )
    ).parsed
