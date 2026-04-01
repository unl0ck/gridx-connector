from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.partial_set_system_tags_body_item import PartialSetSystemTagsBodyItem
from ...models.partial_set_system_tags_response_200_item import PartialSetSystemTagsResponse200Item
from ...models.partial_set_system_tags_response_400 import PartialSetSystemTagsResponse400
from ...models.partial_set_system_tags_response_403 import PartialSetSystemTagsResponse403
from ...models.partial_set_system_tags_response_404 import PartialSetSystemTagsResponse404
from ...models.partial_set_system_tags_response_500 import PartialSetSystemTagsResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: list[PartialSetSystemTagsBodyItem],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}/tags".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PartialSetSystemTagsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = PartialSetSystemTagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PartialSetSystemTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PartialSetSystemTagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PartialSetSystemTagsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
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
    body: list[PartialSetSystemTagsBodyItem],
) -> Response[
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
]:
    """Update or create tags for a system

     Partially set or update tags for a specific system.
    If a tag with the given name exists, its value will be updated.
    If the tag does not exist, it will be created.
    The response status code is always `200 OK`, even if new tags are created.

    Args:
        system_id (UUID):
        body (list[PartialSetSystemTagsBodyItem]): An array of tags where each tag includes a name
            and a value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialSetSystemTagsResponse400 | PartialSetSystemTagsResponse403 | PartialSetSystemTagsResponse404 | PartialSetSystemTagsResponse500 | list[PartialSetSystemTagsResponse200Item]]
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
    body: list[PartialSetSystemTagsBodyItem],
) -> (
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
    | None
):
    """Update or create tags for a system

     Partially set or update tags for a specific system.
    If a tag with the given name exists, its value will be updated.
    If the tag does not exist, it will be created.
    The response status code is always `200 OK`, even if new tags are created.

    Args:
        system_id (UUID):
        body (list[PartialSetSystemTagsBodyItem]): An array of tags where each tag includes a name
            and a value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialSetSystemTagsResponse400 | PartialSetSystemTagsResponse403 | PartialSetSystemTagsResponse404 | PartialSetSystemTagsResponse500 | list[PartialSetSystemTagsResponse200Item]
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
    body: list[PartialSetSystemTagsBodyItem],
) -> Response[
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
]:
    """Update or create tags for a system

     Partially set or update tags for a specific system.
    If a tag with the given name exists, its value will be updated.
    If the tag does not exist, it will be created.
    The response status code is always `200 OK`, even if new tags are created.

    Args:
        system_id (UUID):
        body (list[PartialSetSystemTagsBodyItem]): An array of tags where each tag includes a name
            and a value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialSetSystemTagsResponse400 | PartialSetSystemTagsResponse403 | PartialSetSystemTagsResponse404 | PartialSetSystemTagsResponse500 | list[PartialSetSystemTagsResponse200Item]]
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
    body: list[PartialSetSystemTagsBodyItem],
) -> (
    PartialSetSystemTagsResponse400
    | PartialSetSystemTagsResponse403
    | PartialSetSystemTagsResponse404
    | PartialSetSystemTagsResponse500
    | list[PartialSetSystemTagsResponse200Item]
    | None
):
    """Update or create tags for a system

     Partially set or update tags for a specific system.
    If a tag with the given name exists, its value will be updated.
    If the tag does not exist, it will be created.
    The response status code is always `200 OK`, even if new tags are created.

    Args:
        system_id (UUID):
        body (list[PartialSetSystemTagsBodyItem]): An array of tags where each tag includes a name
            and a value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialSetSystemTagsResponse400 | PartialSetSystemTagsResponse403 | PartialSetSystemTagsResponse404 | PartialSetSystemTagsResponse500 | list[PartialSetSystemTagsResponse200Item]
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
