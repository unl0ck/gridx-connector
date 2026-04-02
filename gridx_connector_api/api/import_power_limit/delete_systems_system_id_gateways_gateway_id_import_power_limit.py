from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_systems_system_id_gateways_gateway_id_import_power_limit_response_422 import (
    DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422,
)
from ...models.delete_systems_system_id_gateways_gateway_id_import_power_limit_response_500 import (
    DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    gateway_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/systems/{system_id}/gateways/{gateway_id}/import-power-limit".format(
            system_id=quote(str(system_id), safe=""),
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 422:
        response_422 = DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
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
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Delete gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
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
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Delete gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
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
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Delete gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
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
    Any
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Delete gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | DeleteSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            gateway_id=gateway_id,
            client=client,
        )
    ).parsed
