from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_tokens_response_200_item import GetUserTokensResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/tokens",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[GetUserTokensResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetUserTokensResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[GetUserTokensResponse200Item]]:
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
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[Any | list[GetUserTokensResponse200Item]]:
    """List all Tokens

     Lists all the API tokens for the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[GetUserTokensResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
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
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Any | list[GetUserTokensResponse200Item] | None:
    """List all Tokens

     Lists all the API tokens for the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[GetUserTokensResponse200Item]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[Any | list[GetUserTokensResponse200Item]]:
    """List all Tokens

     Lists all the API tokens for the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[GetUserTokensResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Any | list[GetUserTokensResponse200Item] | None:
    """List all Tokens

     Lists all the API tokens for the authenticated user.

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[GetUserTokensResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            order=order,
        )
    ).parsed
