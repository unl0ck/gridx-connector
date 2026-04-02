from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_product_options_response_200_item import (
    GetAccountsAccountIDProductOptionsResponse200Item,
)
from ...models.get_accounts_account_id_product_options_response_403 import GetAccountsAccountIDProductOptionsResponse403
from ...models.get_accounts_account_id_product_options_response_404 import GetAccountsAccountIDProductOptionsResponse404
from ...models.get_accounts_account_id_product_options_response_500 import GetAccountsAccountIDProductOptionsResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/product-options".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDProductOptionsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDProductOptionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccountsAccountIDProductOptionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDProductOptionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
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
) -> Response[
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
]:
    """List Product Options

     Lists all product options created by the given account and its children.

    Product options returned by this endpoint are not necessarily assignable to all systems assigned to
    the given account.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDProductOptionsResponse403 | GetAccountsAccountIDProductOptionsResponse404 | GetAccountsAccountIDProductOptionsResponse500 | list[GetAccountsAccountIDProductOptionsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
    | None
):
    """List Product Options

     Lists all product options created by the given account and its children.

    Product options returned by this endpoint are not necessarily assignable to all systems assigned to
    the given account.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDProductOptionsResponse403 | GetAccountsAccountIDProductOptionsResponse404 | GetAccountsAccountIDProductOptionsResponse500 | list[GetAccountsAccountIDProductOptionsResponse200Item]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
]:
    """List Product Options

     Lists all product options created by the given account and its children.

    Product options returned by this endpoint are not necessarily assignable to all systems assigned to
    the given account.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDProductOptionsResponse403 | GetAccountsAccountIDProductOptionsResponse404 | GetAccountsAccountIDProductOptionsResponse500 | list[GetAccountsAccountIDProductOptionsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDProductOptionsResponse403
    | GetAccountsAccountIDProductOptionsResponse404
    | GetAccountsAccountIDProductOptionsResponse500
    | list[GetAccountsAccountIDProductOptionsResponse200Item]
    | None
):
    """List Product Options

     Lists all product options created by the given account and its children.

    Product options returned by this endpoint are not necessarily assignable to all systems assigned to
    the given account.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDProductOptionsResponse403 | GetAccountsAccountIDProductOptionsResponse404 | GetAccountsAccountIDProductOptionsResponse500 | list[GetAccountsAccountIDProductOptionsResponse200Item]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
