from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_systems_system_id_ev_profiles_ev_profile_id_response_403 import (
    DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403,
)
from ...models.delete_systems_system_id_ev_profiles_ev_profile_id_response_404 import (
    DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404,
)
from ...models.delete_systems_system_id_ev_profiles_ev_profile_id_response_422 import (
    DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422,
)
from ...models.delete_systems_system_id_ev_profiles_ev_profile_id_response_500 import (
    DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    ev_profile_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/systems/{system_id}/ev-profiles/{ev_profile_id}".format(
            system_id=quote(str(system_id), safe=""),
            ev_profile_id=quote(str(ev_profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
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
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Delete an EV profile

     Deletes an EV profile that belongs to the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500]
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
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Delete an EV profile

     Deletes an EV profile that belongs to the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
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
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Delete an EV profile

     Deletes an EV profile that belongs to the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500]
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
    Any
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422
    | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Delete an EV profile

     Deletes an EV profile that belongs to the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse403 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse404 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse422 | DeleteSystemsSystemIDEvProfilesEvProfileIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            ev_profile_id=ev_profile_id,
            client=client,
        )
    ).parsed
