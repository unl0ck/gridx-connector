from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_scans_response_400 import GetGatewaysGatewayIDScansResponse400
from ...models.get_gateways_gateway_id_scans_response_403 import GetGatewaysGatewayIDScansResponse403
from ...models.get_gateways_gateway_id_scans_response_500 import GetGatewaysGatewayIDScansResponse500
from ...types import UNSET, Response


def _get_kwargs(
    gateway_id: UUID,
    *,
    interval: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/scans".format(
            gateway_id=quote(str(gateway_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDScansResponse400
    | GetGatewaysGatewayIDScansResponse403
    | GetGatewaysGatewayIDScansResponse500
    | None
):
    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDScansResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDScansResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDScansResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> Response[
    GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500
]:
    """List Gateway's Scans

     List of scans for the given gateway and the given interval.

    If no interval is specified, the entire period is considered and all scans are listed.

    Args:
        gateway_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        interval=interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> (
    GetGatewaysGatewayIDScansResponse400
    | GetGatewaysGatewayIDScansResponse403
    | GetGatewaysGatewayIDScansResponse500
    | None
):
    """List Gateway's Scans

     List of scans for the given gateway and the given interval.

    If no interval is specified, the entire period is considered and all scans are listed.

    Args:
        gateway_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        client=client,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> Response[
    GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500
]:
    """List Gateway's Scans

     List of scans for the given gateway and the given interval.

    If no interval is specified, the entire period is considered and all scans are listed.

    Args:
        gateway_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        interval=interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> (
    GetGatewaysGatewayIDScansResponse400
    | GetGatewaysGatewayIDScansResponse403
    | GetGatewaysGatewayIDScansResponse500
    | None
):
    """List Gateway's Scans

     List of scans for the given gateway and the given interval.

    If no interval is specified, the entire period is considered and all scans are listed.

    Args:
        gateway_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDScansResponse400 | GetGatewaysGatewayIDScansResponse403 | GetGatewaysGatewayIDScansResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            client=client,
            interval=interval,
        )
    ).parsed
