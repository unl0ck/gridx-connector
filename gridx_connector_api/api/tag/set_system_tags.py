from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_system_tags_body_item import SetSystemTagsBodyItem
from ...models.set_system_tags_response_200_item import SetSystemTagsResponse200Item
from ...models.set_system_tags_response_400 import SetSystemTagsResponse400
from ...models.set_system_tags_response_403 import SetSystemTagsResponse403
from ...models.set_system_tags_response_404 import SetSystemTagsResponse404
from ...models.set_system_tags_response_500 import SetSystemTagsResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: list[SetSystemTagsBodyItem],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
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
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SetSystemTagsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = SetSystemTagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SetSystemTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetSystemTagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = SetSystemTagsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
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
    body: list[SetSystemTagsBodyItem],
) -> Response[
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
]:
    """Replace and create all tags for a specific system

     Replaces all tags associated with a specific system. If the request payload contains tags,
    all existing tags will be removed and replaced with the ones provided.
    If an empty array is provided, all tags will be removed for the system.

    Args:
        system_id (UUID):
        body (list[SetSystemTagsBodyItem]): An array of tags where each tag includes a name and a
            value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetSystemTagsResponse400 | SetSystemTagsResponse403 | SetSystemTagsResponse404 | SetSystemTagsResponse500 | list[SetSystemTagsResponse200Item]]
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
    body: list[SetSystemTagsBodyItem],
) -> (
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
    | None
):
    """Replace and create all tags for a specific system

     Replaces all tags associated with a specific system. If the request payload contains tags,
    all existing tags will be removed and replaced with the ones provided.
    If an empty array is provided, all tags will be removed for the system.

    Args:
        system_id (UUID):
        body (list[SetSystemTagsBodyItem]): An array of tags where each tag includes a name and a
            value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetSystemTagsResponse400 | SetSystemTagsResponse403 | SetSystemTagsResponse404 | SetSystemTagsResponse500 | list[SetSystemTagsResponse200Item]
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
    body: list[SetSystemTagsBodyItem],
) -> Response[
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
]:
    """Replace and create all tags for a specific system

     Replaces all tags associated with a specific system. If the request payload contains tags,
    all existing tags will be removed and replaced with the ones provided.
    If an empty array is provided, all tags will be removed for the system.

    Args:
        system_id (UUID):
        body (list[SetSystemTagsBodyItem]): An array of tags where each tag includes a name and a
            value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetSystemTagsResponse400 | SetSystemTagsResponse403 | SetSystemTagsResponse404 | SetSystemTagsResponse500 | list[SetSystemTagsResponse200Item]]
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
    body: list[SetSystemTagsBodyItem],
) -> (
    SetSystemTagsResponse400
    | SetSystemTagsResponse403
    | SetSystemTagsResponse404
    | SetSystemTagsResponse500
    | list[SetSystemTagsResponse200Item]
    | None
):
    """Replace and create all tags for a specific system

     Replaces all tags associated with a specific system. If the request payload contains tags,
    all existing tags will be removed and replaced with the ones provided.
    If an empty array is provided, all tags will be removed for the system.

    Args:
        system_id (UUID):
        body (list[SetSystemTagsBodyItem]): An array of tags where each tag includes a name and a
            value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetSystemTagsResponse400 | SetSystemTagsResponse403 | SetSystemTagsResponse404 | SetSystemTagsResponse500 | list[SetSystemTagsResponse200Item]
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
