from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_live_response_403 import GetSystemsSystemIDLiveResponse403
from ...models.get_systems_system_id_live_response_404 import GetSystemsSystemIDLiveResponse404
from ...models.get_systems_system_id_live_response_422 import GetSystemsSystemIDLiveResponse422
from ...models.get_systems_system_id_live_response_500 import GetSystemsSystemIDLiveResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/live".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
    | None
):
    if response.status_code == 403:
        response_403 = GetSystemsSystemIDLiveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDLiveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDLiveResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDLiveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
]:
    """Retrieve System's Live Measurement.

     Retrieves a system's latest aggregated measurement.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDLiveResponse403 | GetSystemsSystemIDLiveResponse404 | GetSystemsSystemIDLiveResponse422 | GetSystemsSystemIDLiveResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
    | None
):
    """Retrieve System's Live Measurement.

     Retrieves a system's latest aggregated measurement.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDLiveResponse403 | GetSystemsSystemIDLiveResponse404 | GetSystemsSystemIDLiveResponse422 | GetSystemsSystemIDLiveResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
]:
    """Retrieve System's Live Measurement.

     Retrieves a system's latest aggregated measurement.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDLiveResponse403 | GetSystemsSystemIDLiveResponse404 | GetSystemsSystemIDLiveResponse422 | GetSystemsSystemIDLiveResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDLiveResponse403
    | GetSystemsSystemIDLiveResponse404
    | GetSystemsSystemIDLiveResponse422
    | GetSystemsSystemIDLiveResponse500
    | None
):
    """Retrieve System's Live Measurement.

     Retrieves a system's latest aggregated measurement.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDLiveResponse403 | GetSystemsSystemIDLiveResponse404 | GetSystemsSystemIDLiveResponse422 | GetSystemsSystemIDLiveResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
