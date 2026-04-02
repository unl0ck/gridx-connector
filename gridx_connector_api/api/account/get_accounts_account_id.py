from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_account import GetAccountsAccountIDAccount
from ...models.get_accounts_account_id_response_403 import GetAccountsAccountIDResponse403
from ...models.get_accounts_account_id_response_404 import GetAccountsAccountIDResponse404
from ...models.get_accounts_account_id_response_500 import GetAccountsAccountIDResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetAccountsAccountIDAccount.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccountsAccountIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
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
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
]:
    """Retrieve an Account

     Get an Account by its ID. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDAccount | GetAccountsAccountIDResponse403 | GetAccountsAccountIDResponse404 | GetAccountsAccountIDResponse500]
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
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
    | None
):
    """Retrieve an Account

     Get an Account by its ID. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDAccount | GetAccountsAccountIDResponse403 | GetAccountsAccountIDResponse404 | GetAccountsAccountIDResponse500
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
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
]:
    """Retrieve an Account

     Get an Account by its ID. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDAccount | GetAccountsAccountIDResponse403 | GetAccountsAccountIDResponse404 | GetAccountsAccountIDResponse500]
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
    GetAccountsAccountIDAccount
    | GetAccountsAccountIDResponse403
    | GetAccountsAccountIDResponse404
    | GetAccountsAccountIDResponse500
    | None
):
    """Retrieve an Account

     Get an Account by its ID. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDAccount | GetAccountsAccountIDResponse403 | GetAccountsAccountIDResponse404 | GetAccountsAccountIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
