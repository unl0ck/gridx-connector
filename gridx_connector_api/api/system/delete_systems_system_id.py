from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_systems_system_id_response_403 import DeleteSystemsSystemIDResponse403
from ...models.delete_systems_system_id_response_404 import DeleteSystemsSystemIDResponse404
from ...models.delete_systems_system_id_response_500 import DeleteSystemsSystemIDResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/systems/{system_id}".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500 | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = DeleteSystemsSystemIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteSystemsSystemIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteSystemsSystemIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500
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
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500
]:
    """Delete a System

     Deletes a system.

    **Important**: The system must not have any attached Gateway. Reset any attached Gateway first by
    creating a *reset job*.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500]
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
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500 | None
):
    """Delete a System

     Deletes a system.

    **Important**: The system must not have any attached Gateway. Reset any attached Gateway first by
    creating a *reset job*.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500
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
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500
]:
    """Delete a System

     Deletes a system.

    **Important**: The system must not have any attached Gateway. Reset any attached Gateway first by
    creating a *reset job*.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500]
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
    Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500 | None
):
    """Delete a System

     Deletes a system.

    **Important**: The system must not have any attached Gateway. Reset any attached Gateway first by
    creating a *reset job*.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemsSystemIDResponse403 | DeleteSystemsSystemIDResponse404 | DeleteSystemsSystemIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
