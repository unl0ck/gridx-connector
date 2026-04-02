from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_accounts_account_id_account import PatchAccountsAccountIDAccount
from ...models.patch_accounts_account_id_body import PatchAccountsAccountIDBody
from ...models.patch_accounts_account_id_response_403 import PatchAccountsAccountIDResponse403
from ...models.patch_accounts_account_id_response_404 import PatchAccountsAccountIDResponse404
from ...models.patch_accounts_account_id_response_422 import PatchAccountsAccountIDResponse422
from ...models.patch_accounts_account_id_response_500 import PatchAccountsAccountIDResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: PatchAccountsAccountIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/accounts/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchAccountsAccountIDAccount.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PatchAccountsAccountIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchAccountsAccountIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchAccountsAccountIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchAccountsAccountIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
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
    body: PatchAccountsAccountIDBody,
) -> Response[
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
]:
    """Update an Account

     Update an Account's information. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountsAccountIDAccount | PatchAccountsAccountIDResponse403 | PatchAccountsAccountIDResponse404 | PatchAccountsAccountIDResponse422 | PatchAccountsAccountIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountsAccountIDBody,
) -> (
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
    | None
):
    """Update an Account

     Update an Account's information. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountsAccountIDAccount | PatchAccountsAccountIDResponse403 | PatchAccountsAccountIDResponse404 | PatchAccountsAccountIDResponse422 | PatchAccountsAccountIDResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountsAccountIDBody,
) -> Response[
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
]:
    """Update an Account

     Update an Account's information. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountsAccountIDAccount | PatchAccountsAccountIDResponse403 | PatchAccountsAccountIDResponse404 | PatchAccountsAccountIDResponse422 | PatchAccountsAccountIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountsAccountIDBody,
) -> (
    PatchAccountsAccountIDAccount
    | PatchAccountsAccountIDResponse403
    | PatchAccountsAccountIDResponse404
    | PatchAccountsAccountIDResponse422
    | PatchAccountsAccountIDResponse500
    | None
):
    """Update an Account

     Update an Account's information. Make sure you have the necessary permissions.

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountsAccountIDAccount | PatchAccountsAccountIDResponse403 | PatchAccountsAccountIDResponse404 | PatchAccountsAccountIDResponse422 | PatchAccountsAccountIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
