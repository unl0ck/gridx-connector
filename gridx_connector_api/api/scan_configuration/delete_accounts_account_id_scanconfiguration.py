from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_accounts_account_id_scanconfiguration_response_422 import (
    DeleteAccountsAccountIDScanconfigurationResponse422,
)
from ...models.delete_accounts_account_id_scanconfiguration_response_500 import (
    DeleteAccountsAccountIDScanconfigurationResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{account_id}/scanconfiguration".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAccountsAccountIDScanconfigurationResponse422
    | DeleteAccountsAccountIDScanconfigurationResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 422:
        response_422 = DeleteAccountsAccountIDScanconfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeleteAccountsAccountIDScanconfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500
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
    Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500
]:
    """Delete a Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500]
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
    Any
    | DeleteAccountsAccountIDScanconfigurationResponse422
    | DeleteAccountsAccountIDScanconfigurationResponse500
    | None
):
    """Delete a Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500
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
    Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500
]:
    """Delete a Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500]
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
    Any
    | DeleteAccountsAccountIDScanconfigurationResponse422
    | DeleteAccountsAccountIDScanconfigurationResponse500
    | None
):
    """Delete a Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountsAccountIDScanconfigurationResponse422 | DeleteAccountsAccountIDScanconfigurationResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
