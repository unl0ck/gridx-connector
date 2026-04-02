from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_systems_system_id_body import PatchSystemsSystemIDBody
from ...models.patch_systems_system_id_response_403 import PatchSystemsSystemIDResponse403
from ...models.patch_systems_system_id_response_404 import PatchSystemsSystemIDResponse404
from ...models.patch_systems_system_id_response_422 import PatchSystemsSystemIDResponse422
from ...models.patch_systems_system_id_response_500 import PatchSystemsSystemIDResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PatchSystemsSystemIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}".format(
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
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
    | None
):
    if response.status_code == 403:
        response_403 = PatchSystemsSystemIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemsSystemIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchSystemsSystemIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchSystemsSystemIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
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
    body: PatchSystemsSystemIDBody,
) -> Response[
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
]:
    """Update a System

     Updates the specific system by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDResponse403 | PatchSystemsSystemIDResponse404 | PatchSystemsSystemIDResponse422 | PatchSystemsSystemIDResponse500]
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
    body: PatchSystemsSystemIDBody,
) -> (
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
    | None
):
    """Update a System

     Updates the specific system by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDResponse403 | PatchSystemsSystemIDResponse404 | PatchSystemsSystemIDResponse422 | PatchSystemsSystemIDResponse500
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
    body: PatchSystemsSystemIDBody,
) -> Response[
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
]:
    """Update a System

     Updates the specific system by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDResponse403 | PatchSystemsSystemIDResponse404 | PatchSystemsSystemIDResponse422 | PatchSystemsSystemIDResponse500]
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
    body: PatchSystemsSystemIDBody,
) -> (
    PatchSystemsSystemIDResponse403
    | PatchSystemsSystemIDResponse404
    | PatchSystemsSystemIDResponse422
    | PatchSystemsSystemIDResponse500
    | None
):
    """Update a System

     Updates the specific system by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDResponse403 | PatchSystemsSystemIDResponse404 | PatchSystemsSystemIDResponse422 | PatchSystemsSystemIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
