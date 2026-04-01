from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_account_account import GetAccountAccount
from ...models.get_account_response_403 import GetAccountResponse403
from ...models.get_account_response_404 import GetAccountResponse404
from ...models.get_account_response_500 import GetAccountResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountAccount.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccountResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccountResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500]:
    """Retrieve the authenticated Account

     Get the account that is currently logged in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500 | None:
    """Retrieve the authenticated Account

     Get the account that is currently logged in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500]:
    """Retrieve the authenticated Account

     Get the account that is currently logged in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500 | None:
    """Retrieve the authenticated Account

     Get the account that is currently logged in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountAccount | GetAccountResponse403 | GetAccountResponse404 | GetAccountResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
