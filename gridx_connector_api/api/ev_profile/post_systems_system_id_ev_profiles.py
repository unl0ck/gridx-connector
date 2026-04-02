from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_system_id_ev_profiles_body import PostSystemsSystemIDEvProfilesBody
from ...models.post_systems_system_id_ev_profiles_response_201 import PostSystemsSystemIDEvProfilesResponse201
from ...models.post_systems_system_id_ev_profiles_response_403 import PostSystemsSystemIDEvProfilesResponse403
from ...models.post_systems_system_id_ev_profiles_response_404 import PostSystemsSystemIDEvProfilesResponse404
from ...models.post_systems_system_id_ev_profiles_response_500 import PostSystemsSystemIDEvProfilesResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PostSystemsSystemIDEvProfilesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systems/{system_id}/ev-profiles".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostSystemsSystemIDEvProfilesResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = PostSystemsSystemIDEvProfilesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemsSystemIDEvProfilesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PostSystemsSystemIDEvProfilesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
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
    body: PostSystemsSystemIDEvProfilesBody,
) -> Response[
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
]:
    """Create a new EV profile

     Creates an EV profile.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDEvProfilesResponse201 | PostSystemsSystemIDEvProfilesResponse403 | PostSystemsSystemIDEvProfilesResponse404 | PostSystemsSystemIDEvProfilesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvProfilesBody,
) -> (
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
    | None
):
    """Create a new EV profile

     Creates an EV profile.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDEvProfilesResponse201 | PostSystemsSystemIDEvProfilesResponse403 | PostSystemsSystemIDEvProfilesResponse404 | PostSystemsSystemIDEvProfilesResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvProfilesBody,
) -> Response[
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
]:
    """Create a new EV profile

     Creates an EV profile.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDEvProfilesResponse201 | PostSystemsSystemIDEvProfilesResponse403 | PostSystemsSystemIDEvProfilesResponse404 | PostSystemsSystemIDEvProfilesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvProfilesBody,
) -> (
    PostSystemsSystemIDEvProfilesResponse201
    | PostSystemsSystemIDEvProfilesResponse403
    | PostSystemsSystemIDEvProfilesResponse404
    | PostSystemsSystemIDEvProfilesResponse500
    | None
):
    """Create a new EV profile

     Creates an EV profile.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDEvProfilesResponse201 | PostSystemsSystemIDEvProfilesResponse403 | PostSystemsSystemIDEvProfilesResponse404 | PostSystemsSystemIDEvProfilesResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
