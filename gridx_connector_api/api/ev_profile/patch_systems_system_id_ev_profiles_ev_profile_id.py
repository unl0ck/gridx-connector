from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_systems_system_id_ev_profiles_ev_profile_id_body import (
    PatchSystemsSystemIDEvProfilesEvProfileIDBody,
)
from ...models.patch_systems_system_id_ev_profiles_ev_profile_id_response_200 import (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200,
)
from ...models.patch_systems_system_id_ev_profiles_ev_profile_id_response_403 import (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse403,
)
from ...models.patch_systems_system_id_ev_profiles_ev_profile_id_response_404 import (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse404,
)
from ...models.patch_systems_system_id_ev_profiles_ev_profile_id_response_500 import (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    body: PatchSystemsSystemIDEvProfilesEvProfileIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}/ev-profiles/{ev_profile_id}".format(
            system_id=quote(str(system_id), safe=""),
            ev_profile_id=quote(str(ev_profile_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchSystemsSystemIDEvProfilesEvProfileIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PatchSystemsSystemIDEvProfilesEvProfileIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemsSystemIDEvProfilesEvProfileIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PatchSystemsSystemIDEvProfilesEvProfileIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
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
    body: PatchSystemsSystemIDEvProfilesEvProfileIDBody,
) -> Response[
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Update an EV profile

     Update an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):
        body (PatchSystemsSystemIDEvProfilesEvProfileIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDEvProfilesEvProfileIDResponse200 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
        body=body,
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
    body: PatchSystemsSystemIDEvProfilesEvProfileIDBody,
) -> (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Update an EV profile

     Update an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):
        body (PatchSystemsSystemIDEvProfilesEvProfileIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDEvProfilesEvProfileIDResponse200 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
    """

    return sync_detailed(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchSystemsSystemIDEvProfilesEvProfileIDBody,
) -> Response[
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
]:
    """Update an EV profile

     Update an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):
        body (PatchSystemsSystemIDEvProfilesEvProfileIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDEvProfilesEvProfileIDResponse200 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        ev_profile_id=ev_profile_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    ev_profile_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchSystemsSystemIDEvProfilesEvProfileIDBody,
) -> (
    PatchSystemsSystemIDEvProfilesEvProfileIDResponse200
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404
    | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
    | None
):
    """Update an EV profile

     Update an EV profile that belong the the specified system.

    Args:
        system_id (UUID):
        ev_profile_id (UUID):
        body (PatchSystemsSystemIDEvProfilesEvProfileIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDEvProfilesEvProfileIDResponse200 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse403 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse404 | PatchSystemsSystemIDEvProfilesEvProfileIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            ev_profile_id=ev_profile_id,
            client=client,
            body=body,
        )
    ).parsed
