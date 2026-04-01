from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_systems_embed import GetAccountsAccountIDSystemsEmbed
from ...models.get_accounts_account_id_systems_response_200_item import GetAccountsAccountIDSystemsResponse200Item
from ...models.get_accounts_account_id_systems_response_403 import GetAccountsAccountIDSystemsResponse403
from ...models.get_accounts_account_id_systems_response_422 import GetAccountsAccountIDSystemsResponse422
from ...models.get_accounts_account_id_systems_response_500 import GetAccountsAccountIDSystemsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    embed: GetAccountsAccountIDSystemsEmbed | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    json_embed: str | Unset = UNSET
    if not isinstance(embed, Unset):
        json_embed = embed.value

    params["embed"] = json_embed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/systems".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDSystemsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDSystemsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAccountsAccountIDSystemsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDSystemsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    embed: GetAccountsAccountIDSystemsEmbed | Unset = UNSET,
) -> Response[
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
]:
    """List Account's Systems

    Args:
        account_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        embed (GetAccountsAccountIDSystemsEmbed | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDSystemsResponse403 | GetAccountsAccountIDSystemsResponse422 | GetAccountsAccountIDSystemsResponse500 | list[GetAccountsAccountIDSystemsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        per_page=per_page,
        page=page,
        embed=embed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    embed: GetAccountsAccountIDSystemsEmbed | Unset = UNSET,
) -> (
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
    | None
):
    """List Account's Systems

    Args:
        account_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        embed (GetAccountsAccountIDSystemsEmbed | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDSystemsResponse403 | GetAccountsAccountIDSystemsResponse422 | GetAccountsAccountIDSystemsResponse500 | list[GetAccountsAccountIDSystemsResponse200Item]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        per_page=per_page,
        page=page,
        embed=embed,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    embed: GetAccountsAccountIDSystemsEmbed | Unset = UNSET,
) -> Response[
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
]:
    """List Account's Systems

    Args:
        account_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        embed (GetAccountsAccountIDSystemsEmbed | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDSystemsResponse403 | GetAccountsAccountIDSystemsResponse422 | GetAccountsAccountIDSystemsResponse500 | list[GetAccountsAccountIDSystemsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        per_page=per_page,
        page=page,
        embed=embed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    embed: GetAccountsAccountIDSystemsEmbed | Unset = UNSET,
) -> (
    GetAccountsAccountIDSystemsResponse403
    | GetAccountsAccountIDSystemsResponse422
    | GetAccountsAccountIDSystemsResponse500
    | list[GetAccountsAccountIDSystemsResponse200Item]
    | None
):
    """List Account's Systems

    Args:
        account_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        embed (GetAccountsAccountIDSystemsEmbed | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDSystemsResponse403 | GetAccountsAccountIDSystemsResponse422 | GetAccountsAccountIDSystemsResponse500 | list[GetAccountsAccountIDSystemsResponse200Item]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            per_page=per_page,
            page=page,
            embed=embed,
        )
    ).parsed
