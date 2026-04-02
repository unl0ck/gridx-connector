from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_response_400 import GetGatewaysGatewayIDResponse400
from ...models.get_gateways_gateway_id_response_403 import GetGatewaysGatewayIDResponse403
from ...models.get_gateways_gateway_id_response_404 import GetGatewaysGatewayIDResponse404
from ...models.get_gateways_gateway_id_response_500 import GetGatewaysGatewayIDResponse500
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}".format(
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
    | None
):
    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
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
) -> Response[
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
]:
    """Retrieve a Gateway

     Retrieves the details of an existing gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDResponse400 | GetGatewaysGatewayIDResponse403 | GetGatewaysGatewayIDResponse404 | GetGatewaysGatewayIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
    | None
):
    """Retrieve a Gateway

     Retrieves the details of an existing gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDResponse400 | GetGatewaysGatewayIDResponse403 | GetGatewaysGatewayIDResponse404 | GetGatewaysGatewayIDResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
]:
    """Retrieve a Gateway

     Retrieves the details of an existing gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDResponse400 | GetGatewaysGatewayIDResponse403 | GetGatewaysGatewayIDResponse404 | GetGatewaysGatewayIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDResponse400
    | GetGatewaysGatewayIDResponse403
    | GetGatewaysGatewayIDResponse404
    | GetGatewaysGatewayIDResponse500
    | None
):
    """Retrieve a Gateway

     Retrieves the details of an existing gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDResponse400 | GetGatewaysGatewayIDResponse403 | GetGatewaysGatewayIDResponse404 | GetGatewaysGatewayIDResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            client=client,
        )
    ).parsed
