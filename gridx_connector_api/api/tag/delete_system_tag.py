from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_system_tag_response_400 import DeleteSystemTagResponse400
from ...models.delete_system_tag_response_403 import DeleteSystemTagResponse403
from ...models.delete_system_tag_response_404 import DeleteSystemTagResponse404
from ...models.delete_system_tag_response_500 import DeleteSystemTagResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    tag_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/systems/{system_id}/tags/{tag_name}".format(
            system_id=quote(str(system_id), safe=""),
            tag_name=quote(str(tag_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteSystemTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = DeleteSystemTagResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteSystemTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteSystemTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
]:
    """Delete a tag for a system

     Deletes a tag for a specific system. If the tag exists, it will be deleted and the status code `204
    OK` will be returned.
    If the tag doesn't exist the status code `404 Created` will be returned.

    Args:
        system_id (UUID):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemTagResponse400 | DeleteSystemTagResponse403 | DeleteSystemTagResponse404 | DeleteSystemTagResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        tag_name=tag_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
    | None
):
    """Delete a tag for a system

     Deletes a tag for a specific system. If the tag exists, it will be deleted and the status code `204
    OK` will be returned.
    If the tag doesn't exist the status code `404 Created` will be returned.

    Args:
        system_id (UUID):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemTagResponse400 | DeleteSystemTagResponse403 | DeleteSystemTagResponse404 | DeleteSystemTagResponse500
    """

    return sync_detailed(
        system_id=system_id,
        tag_name=tag_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
]:
    """Delete a tag for a system

     Deletes a tag for a specific system. If the tag exists, it will be deleted and the status code `204
    OK` will be returned.
    If the tag doesn't exist the status code `404 Created` will be returned.

    Args:
        system_id (UUID):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemTagResponse400 | DeleteSystemTagResponse403 | DeleteSystemTagResponse404 | DeleteSystemTagResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        tag_name=tag_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | DeleteSystemTagResponse400
    | DeleteSystemTagResponse403
    | DeleteSystemTagResponse404
    | DeleteSystemTagResponse500
    | None
):
    """Delete a tag for a system

     Deletes a tag for a specific system. If the tag exists, it will be deleted and the status code `204
    OK` will be returned.
    If the tag doesn't exist the status code `404 Created` will be returned.

    Args:
        system_id (UUID):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemTagResponse400 | DeleteSystemTagResponse403 | DeleteSystemTagResponse404 | DeleteSystemTagResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            tag_name=tag_name,
            client=client,
        )
    ).parsed
