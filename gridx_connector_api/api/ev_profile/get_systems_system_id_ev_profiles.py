from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_ev_profiles_response_200_item import GetSystemsSystemIDEvProfilesResponse200Item
from ...models.get_systems_system_id_ev_profiles_response_403 import GetSystemsSystemIDEvProfilesResponse403
from ...models.get_systems_system_id_ev_profiles_response_404 import GetSystemsSystemIDEvProfilesResponse404
from ...models.get_systems_system_id_ev_profiles_response_500 import GetSystemsSystemIDEvProfilesResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/ev-profiles".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetSystemsSystemIDEvProfilesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDEvProfilesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDEvProfilesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDEvProfilesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
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
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
]:
    """List available EV profiles

     Lists EV profiles that belong the the specified system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvProfilesResponse403 | GetSystemsSystemIDEvProfilesResponse404 | GetSystemsSystemIDEvProfilesResponse500 | list[GetSystemsSystemIDEvProfilesResponse200Item]]
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
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
    | None
):
    """List available EV profiles

     Lists EV profiles that belong the the specified system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvProfilesResponse403 | GetSystemsSystemIDEvProfilesResponse404 | GetSystemsSystemIDEvProfilesResponse500 | list[GetSystemsSystemIDEvProfilesResponse200Item]
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
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
]:
    """List available EV profiles

     Lists EV profiles that belong the the specified system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvProfilesResponse403 | GetSystemsSystemIDEvProfilesResponse404 | GetSystemsSystemIDEvProfilesResponse500 | list[GetSystemsSystemIDEvProfilesResponse200Item]]
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
    GetSystemsSystemIDEvProfilesResponse403
    | GetSystemsSystemIDEvProfilesResponse404
    | GetSystemsSystemIDEvProfilesResponse500
    | list[GetSystemsSystemIDEvProfilesResponse200Item]
    | None
):
    """List available EV profiles

     Lists EV profiles that belong the the specified system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvProfilesResponse403 | GetSystemsSystemIDEvProfilesResponse404 | GetSystemsSystemIDEvProfilesResponse500 | list[GetSystemsSystemIDEvProfilesResponse200Item]
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
