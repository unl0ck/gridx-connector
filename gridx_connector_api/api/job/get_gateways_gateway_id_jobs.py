from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_jobs_response_200_item import GetGatewaysGatewayIDJobsResponse200Item
from ...models.get_gateways_gateway_id_jobs_response_400 import GetGatewaysGatewayIDJobsResponse400
from ...models.get_gateways_gateway_id_jobs_response_403 import GetGatewaysGatewayIDJobsResponse403
from ...models.get_gateways_gateway_id_jobs_response_404 import GetGatewaysGatewayIDJobsResponse404
from ...models.get_gateways_gateway_id_jobs_response_500 import GetGatewaysGatewayIDJobsResponse500
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/jobs".format(
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetGatewaysGatewayIDJobsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDJobsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDJobsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDJobsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDJobsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
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
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
]:
    """List Gateway's Jobs

     List jobs that belong to the given gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDJobsResponse400 | GetGatewaysGatewayIDJobsResponse403 | GetGatewaysGatewayIDJobsResponse404 | GetGatewaysGatewayIDJobsResponse500 | list[GetGatewaysGatewayIDJobsResponse200Item]]
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
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
    | None
):
    """List Gateway's Jobs

     List jobs that belong to the given gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDJobsResponse400 | GetGatewaysGatewayIDJobsResponse403 | GetGatewaysGatewayIDJobsResponse404 | GetGatewaysGatewayIDJobsResponse500 | list[GetGatewaysGatewayIDJobsResponse200Item]
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
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
]:
    """List Gateway's Jobs

     List jobs that belong to the given gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDJobsResponse400 | GetGatewaysGatewayIDJobsResponse403 | GetGatewaysGatewayIDJobsResponse404 | GetGatewaysGatewayIDJobsResponse500 | list[GetGatewaysGatewayIDJobsResponse200Item]]
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
    GetGatewaysGatewayIDJobsResponse400
    | GetGatewaysGatewayIDJobsResponse403
    | GetGatewaysGatewayIDJobsResponse404
    | GetGatewaysGatewayIDJobsResponse500
    | list[GetGatewaysGatewayIDJobsResponse200Item]
    | None
):
    """List Gateway's Jobs

     List jobs that belong to the given gateway.

    Args:
        gateway_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDJobsResponse400 | GetGatewaysGatewayIDJobsResponse403 | GetGatewaysGatewayIDJobsResponse404 | GetGatewaysGatewayIDJobsResponse500 | list[GetGatewaysGatewayIDJobsResponse200Item]
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            client=client,
        )
    ).parsed
