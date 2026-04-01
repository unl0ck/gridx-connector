from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_accounts_account_id_systems_account import DeleteAccountsAccountIDSystemsAccount
from ...models.delete_accounts_account_id_systems_response_403 import DeleteAccountsAccountIDSystemsResponse403
from ...models.delete_accounts_account_id_systems_response_404 import DeleteAccountsAccountIDSystemsResponse404
from ...models.delete_accounts_account_id_systems_response_422 import DeleteAccountsAccountIDSystemsResponse422
from ...models.delete_accounts_account_id_systems_response_500 import DeleteAccountsAccountIDSystemsResponse500
from ...models.delete_accounts_account_id_systems_system_account_unassignment import (
    DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{account_id}/systems".format(
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
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteAccountsAccountIDSystemsAccount.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DeleteAccountsAccountIDSystemsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteAccountsAccountIDSystemsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = DeleteAccountsAccountIDSystemsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeleteAccountsAccountIDSystemsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
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
    body: DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
) -> Response[
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
]:
    """Unassign a System from an Account

    Args:
        account_id (UUID):
        body (DeleteAccountsAccountIDSystemsSystemAccountUnassignment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAccountsAccountIDSystemsAccount | DeleteAccountsAccountIDSystemsResponse403 | DeleteAccountsAccountIDSystemsResponse404 | DeleteAccountsAccountIDSystemsResponse422 | DeleteAccountsAccountIDSystemsResponse500]
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
    body: DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
) -> (
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
    | None
):
    """Unassign a System from an Account

    Args:
        account_id (UUID):
        body (DeleteAccountsAccountIDSystemsSystemAccountUnassignment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAccountsAccountIDSystemsAccount | DeleteAccountsAccountIDSystemsResponse403 | DeleteAccountsAccountIDSystemsResponse404 | DeleteAccountsAccountIDSystemsResponse422 | DeleteAccountsAccountIDSystemsResponse500
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
    body: DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
) -> Response[
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
]:
    """Unassign a System from an Account

    Args:
        account_id (UUID):
        body (DeleteAccountsAccountIDSystemsSystemAccountUnassignment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAccountsAccountIDSystemsAccount | DeleteAccountsAccountIDSystemsResponse403 | DeleteAccountsAccountIDSystemsResponse404 | DeleteAccountsAccountIDSystemsResponse422 | DeleteAccountsAccountIDSystemsResponse500]
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
    body: DeleteAccountsAccountIDSystemsSystemAccountUnassignment,
) -> (
    DeleteAccountsAccountIDSystemsAccount
    | DeleteAccountsAccountIDSystemsResponse403
    | DeleteAccountsAccountIDSystemsResponse404
    | DeleteAccountsAccountIDSystemsResponse422
    | DeleteAccountsAccountIDSystemsResponse500
    | None
):
    """Unassign a System from an Account

    Args:
        account_id (UUID):
        body (DeleteAccountsAccountIDSystemsSystemAccountUnassignment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAccountsAccountIDSystemsAccount | DeleteAccountsAccountIDSystemsResponse403 | DeleteAccountsAccountIDSystemsResponse404 | DeleteAccountsAccountIDSystemsResponse422 | DeleteAccountsAccountIDSystemsResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
