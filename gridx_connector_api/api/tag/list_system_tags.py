from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_system_tags_response_200_item import ListSystemTagsResponse200Item
from ...models.list_system_tags_response_400 import ListSystemTagsResponse400
from ...models.list_system_tags_response_403 import ListSystemTagsResponse403
from ...models.list_system_tags_response_404 import ListSystemTagsResponse404
from ...models.list_system_tags_response_500 import ListSystemTagsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_id: UUID,
    *,
    name_has_prefix: str | Unset = UNSET,
    name_has_suffix: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_has_prefix: str | Unset = UNSET,
    value_has_suffix: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["nameHasPrefix"] = name_has_prefix

    params["nameHasSuffix"] = name_has_suffix

    params["nameContains"] = name_contains

    params["value"] = value

    params["valueHasPrefix"] = value_has_prefix

    params["valueHasSuffix"] = value_has_suffix

    params["valueContains"] = value_contains

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/tags".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListSystemTagsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ListSystemTagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ListSystemTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListSystemTagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ListSystemTagsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
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
    name_has_prefix: str | Unset = UNSET,
    name_has_suffix: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_has_prefix: str | Unset = UNSET,
    value_has_suffix: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
) -> Response[
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
]:
    """List Tags for a Specific System

     Retrieves a list of tags associated with a specific system. Optionally filters tags by their names
    and values using prefix, suffix, and substring filters. All provided filters are combined using
    logical AND, meaning only tags that satisfy **all** filter conditions will be returned. If no
    filters are provided, all tags for the specified post are returned. **Note:** All filtering is case-
    sensitive.

    Args:
        system_id (UUID):
        name_has_prefix (str | Unset):  Example: cat.
        name_has_suffix (str | Unset):  Example: ory.
        name_contains (str | Unset):  Example: ate.
        value (str | Unset):  Example: technology.
        value_has_prefix (str | Unset):  Example: tech.
        value_has_suffix (str | Unset):  Example: logy.
        value_contains (str | Unset):  Example: chnol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSystemTagsResponse400 | ListSystemTagsResponse403 | ListSystemTagsResponse404 | ListSystemTagsResponse500 | list[ListSystemTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        name_has_prefix=name_has_prefix,
        name_has_suffix=name_has_suffix,
        name_contains=name_contains,
        value=value,
        value_has_prefix=value_has_prefix,
        value_has_suffix=value_has_suffix,
        value_contains=value_contains,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    name_has_prefix: str | Unset = UNSET,
    name_has_suffix: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_has_prefix: str | Unset = UNSET,
    value_has_suffix: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
) -> (
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
    | None
):
    """List Tags for a Specific System

     Retrieves a list of tags associated with a specific system. Optionally filters tags by their names
    and values using prefix, suffix, and substring filters. All provided filters are combined using
    logical AND, meaning only tags that satisfy **all** filter conditions will be returned. If no
    filters are provided, all tags for the specified post are returned. **Note:** All filtering is case-
    sensitive.

    Args:
        system_id (UUID):
        name_has_prefix (str | Unset):  Example: cat.
        name_has_suffix (str | Unset):  Example: ory.
        name_contains (str | Unset):  Example: ate.
        value (str | Unset):  Example: technology.
        value_has_prefix (str | Unset):  Example: tech.
        value_has_suffix (str | Unset):  Example: logy.
        value_contains (str | Unset):  Example: chnol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSystemTagsResponse400 | ListSystemTagsResponse403 | ListSystemTagsResponse404 | ListSystemTagsResponse500 | list[ListSystemTagsResponse200Item]
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        name_has_prefix=name_has_prefix,
        name_has_suffix=name_has_suffix,
        name_contains=name_contains,
        value=value,
        value_has_prefix=value_has_prefix,
        value_has_suffix=value_has_suffix,
        value_contains=value_contains,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    name_has_prefix: str | Unset = UNSET,
    name_has_suffix: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_has_prefix: str | Unset = UNSET,
    value_has_suffix: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
) -> Response[
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
]:
    """List Tags for a Specific System

     Retrieves a list of tags associated with a specific system. Optionally filters tags by their names
    and values using prefix, suffix, and substring filters. All provided filters are combined using
    logical AND, meaning only tags that satisfy **all** filter conditions will be returned. If no
    filters are provided, all tags for the specified post are returned. **Note:** All filtering is case-
    sensitive.

    Args:
        system_id (UUID):
        name_has_prefix (str | Unset):  Example: cat.
        name_has_suffix (str | Unset):  Example: ory.
        name_contains (str | Unset):  Example: ate.
        value (str | Unset):  Example: technology.
        value_has_prefix (str | Unset):  Example: tech.
        value_has_suffix (str | Unset):  Example: logy.
        value_contains (str | Unset):  Example: chnol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSystemTagsResponse400 | ListSystemTagsResponse403 | ListSystemTagsResponse404 | ListSystemTagsResponse500 | list[ListSystemTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        name_has_prefix=name_has_prefix,
        name_has_suffix=name_has_suffix,
        name_contains=name_contains,
        value=value,
        value_has_prefix=value_has_prefix,
        value_has_suffix=value_has_suffix,
        value_contains=value_contains,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    name_has_prefix: str | Unset = UNSET,
    name_has_suffix: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_has_prefix: str | Unset = UNSET,
    value_has_suffix: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
) -> (
    ListSystemTagsResponse400
    | ListSystemTagsResponse403
    | ListSystemTagsResponse404
    | ListSystemTagsResponse500
    | list[ListSystemTagsResponse200Item]
    | None
):
    """List Tags for a Specific System

     Retrieves a list of tags associated with a specific system. Optionally filters tags by their names
    and values using prefix, suffix, and substring filters. All provided filters are combined using
    logical AND, meaning only tags that satisfy **all** filter conditions will be returned. If no
    filters are provided, all tags for the specified post are returned. **Note:** All filtering is case-
    sensitive.

    Args:
        system_id (UUID):
        name_has_prefix (str | Unset):  Example: cat.
        name_has_suffix (str | Unset):  Example: ory.
        name_contains (str | Unset):  Example: ate.
        value (str | Unset):  Example: technology.
        value_has_prefix (str | Unset):  Example: tech.
        value_has_suffix (str | Unset):  Example: logy.
        value_contains (str | Unset):  Example: chnol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSystemTagsResponse400 | ListSystemTagsResponse403 | ListSystemTagsResponse404 | ListSystemTagsResponse500 | list[ListSystemTagsResponse200Item]
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            name_has_prefix=name_has_prefix,
            name_has_suffix=name_has_suffix,
            name_contains=name_contains,
            value=value,
            value_has_prefix=value_has_prefix,
            value_has_suffix=value_has_suffix,
            value_contains=value_contains,
        )
    ).parsed
