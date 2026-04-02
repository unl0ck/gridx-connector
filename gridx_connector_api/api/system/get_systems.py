from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_embed import GetSystemsEmbed
from ...models.get_systems_include_item import GetSystemsIncludeItem
from ...models.get_systems_response_200_item import GetSystemsResponse200Item
from ...models.get_systems_response_403 import GetSystemsResponse403
from ...models.get_systems_response_500 import GetSystemsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    embed: GetSystemsEmbed | Unset = UNSET,
    include: list[GetSystemsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_embed: str | Unset = UNSET
    if not isinstance(embed, Unset):
        json_embed = embed.value

    params["embed"] = json_embed

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetSystemsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetSystemsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    embed: GetSystemsEmbed | Unset = UNSET,
    include: list[GetSystemsIncludeItem] | Unset = UNSET,
) -> Response[GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]]:
    """List all Systems

     List systems that are accessible to the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        embed (GetSystemsEmbed | Unset):
        include (list[GetSystemsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        embed=embed,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    embed: GetSystemsEmbed | Unset = UNSET,
    include: list[GetSystemsIncludeItem] | Unset = UNSET,
) -> GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item] | None:
    """List all Systems

     List systems that are accessible to the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        embed (GetSystemsEmbed | Unset):
        include (list[GetSystemsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        embed=embed,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    embed: GetSystemsEmbed | Unset = UNSET,
    include: list[GetSystemsIncludeItem] | Unset = UNSET,
) -> Response[GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]]:
    """List all Systems

     List systems that are accessible to the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        embed (GetSystemsEmbed | Unset):
        include (list[GetSystemsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        embed=embed,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    embed: GetSystemsEmbed | Unset = UNSET,
    include: list[GetSystemsIncludeItem] | Unset = UNSET,
) -> GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item] | None:
    """List all Systems

     List systems that are accessible to the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        embed (GetSystemsEmbed | Unset):
        include (list[GetSystemsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsResponse403 | GetSystemsResponse500 | list[GetSystemsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            embed=embed,
            include=include,
        )
    ).parsed
