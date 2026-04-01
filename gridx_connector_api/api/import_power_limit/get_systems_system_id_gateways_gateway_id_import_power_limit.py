from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_gateways_gateway_id_import_power_limit_response_200 import (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200,
)
from ...models.get_systems_system_id_gateways_gateway_id_import_power_limit_response_403 import (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403,
)
from ...models.get_systems_system_id_gateways_gateway_id_import_power_limit_response_404 import (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404,
)
from ...models.get_systems_system_id_gateways_gateway_id_import_power_limit_response_422 import (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422,
)
from ...models.get_systems_system_id_gateways_gateway_id_import_power_limit_response_500 import (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    gateway_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/gateways/{gateway_id}/import-power-limit".format(
            system_id=quote(str(system_id), safe=""),
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Retrieve gateway's current import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        gateway_id=gateway_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Retrieve gateway's current import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    """

    return sync_detailed(
        system_id=system_id,
        gateway_id=gateway_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Retrieve gateway's current import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        gateway_id=gateway_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Retrieve gateway's current import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse200 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse403 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse404 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | GetSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            gateway_id=gateway_id,
            client=client,
        )
    ).parsed
