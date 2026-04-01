from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_systems_system_id_gateways_gateway_id_import_power_limit_body import (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
)
from ...models.put_systems_system_id_gateways_gateway_id_import_power_limit_response_201 import (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201,
)
from ...models.put_systems_system_id_gateways_gateway_id_import_power_limit_response_422 import (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422,
)
from ...models.put_systems_system_id_gateways_gateway_id_import_power_limit_response_500 import (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    gateway_id: UUID,
    *,
    body: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/systems/{system_id}/gateways/{gateway_id}/import-power-limit".format(
            system_id=quote(str(system_id), safe=""),
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
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
    body: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
) -> Response[
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Set gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):
        body (PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        gateway_id=gateway_id,
        body=body,
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
    body: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
) -> (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Set gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):
        body (PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    """

    return sync_detailed(
        system_id=system_id,
        gateway_id=gateway_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
) -> Response[
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
]:
    """Set gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):
        body (PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        gateway_id=gateway_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody,
) -> (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422
    | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    | None
):
    """Set gateway's import power limit.

    Args:
        system_id (UUID):
        gateway_id (UUID):
        body (PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse422 | PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            gateway_id=gateway_id,
            client=client,
            body=body,
        )
    ).parsed
