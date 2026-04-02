from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_ev_profiles_ev_profile_id_response_200 import (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200,
)
from ...models.get_systems_system_id_ev_profiles_ev_profile_id_response_403 import (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse403,
)
from ...models.get_systems_system_id_ev_profiles_ev_profile_id_response_404 import (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse404,
)
from ...models.get_systems_system_id_ev_profiles_ev_profile_id_response_500 import (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    ev_profile_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/ev-profiles/{ev_profile_id}".format(
            system_id=quote(str(system_id), safe=""),
            ev_profile_id=quote(str(ev_profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDEvProfilesEvProfileIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDEvProfilesEvProfileIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDEvProfilesEvProfileIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDEvProfilesEvProfileIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Retrieve an EV profile

     Retrieve an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvProfilesEvProfileIDResponse200 | GetSystemsSystemIDEvProfilesEvProfileIDResponse403 | GetSystemsSystemIDEvProfilesEvProfileIDResponse404 | GetSystemsSystemIDEvProfilesEvProfileIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Retrieve an EV profile

     Retrieve an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvProfilesEvProfileIDResponse200 | GetSystemsSystemIDEvProfilesEvProfileIDResponse403 | GetSystemsSystemIDEvProfilesEvProfileIDResponse404 | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
    """

    return sync_detailed(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Retrieve an EV profile

     Retrieve an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvProfilesEvProfileIDResponse200 | GetSystemsSystemIDEvProfilesEvProfileIDResponse403 | GetSystemsSystemIDEvProfilesEvProfileIDResponse404 | GetSystemsSystemIDEvProfilesEvProfileIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDEvProfilesEvProfileIDResponse200
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse403
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse404
    | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Retrieve an EV profile

     Retrieve an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvProfilesEvProfileIDResponse200 | GetSystemsSystemIDEvProfilesEvProfileIDResponse403 | GetSystemsSystemIDEvProfilesEvProfileIDResponse404 | GetSystemsSystemIDEvProfilesEvProfileIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            ev_profile_id=ev_profile_id,
            client=client,
        )
    ).parsed
