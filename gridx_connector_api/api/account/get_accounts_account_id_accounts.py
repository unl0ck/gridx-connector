from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_accounts_account import GetAccountsAccountIDAccountsAccount
from ...models.get_accounts_account_id_accounts_kind import GetAccountsAccountIDAccountsKind
from ...models.get_accounts_account_id_accounts_response_403 import GetAccountsAccountIDAccountsResponse403
from ...models.get_accounts_account_id_accounts_response_422 import GetAccountsAccountIDAccountsResponse422
from ...models.get_accounts_account_id_accounts_response_500 import GetAccountsAccountIDAccountsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    kind: GetAccountsAccountIDAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/accounts".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDAccountsAccount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDAccountsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAccountsAccountIDAccountsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDAccountsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
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
    kind: GetAccountsAccountIDAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> Response[
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
]:
    """List all nested Accounts

     List all child accounts of the given account that are accessible to the authenticated user.

    Args:
        account_id (UUID):
        kind (GetAccountsAccountIDAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDAccountsResponse403 | GetAccountsAccountIDAccountsResponse422 | GetAccountsAccountIDAccountsResponse500 | list[GetAccountsAccountIDAccountsAccount]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        kind=kind,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetAccountsAccountIDAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> (
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
    | None
):
    """List all nested Accounts

     List all child accounts of the given account that are accessible to the authenticated user.

    Args:
        account_id (UUID):
        kind (GetAccountsAccountIDAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDAccountsResponse403 | GetAccountsAccountIDAccountsResponse422 | GetAccountsAccountIDAccountsResponse500 | list[GetAccountsAccountIDAccountsAccount]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        kind=kind,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetAccountsAccountIDAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> Response[
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
]:
    """List all nested Accounts

     List all child accounts of the given account that are accessible to the authenticated user.

    Args:
        account_id (UUID):
        kind (GetAccountsAccountIDAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDAccountsResponse403 | GetAccountsAccountIDAccountsResponse422 | GetAccountsAccountIDAccountsResponse500 | list[GetAccountsAccountIDAccountsAccount]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        kind=kind,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetAccountsAccountIDAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> (
    GetAccountsAccountIDAccountsResponse403
    | GetAccountsAccountIDAccountsResponse422
    | GetAccountsAccountIDAccountsResponse500
    | list[GetAccountsAccountIDAccountsAccount]
    | None
):
    """List all nested Accounts

     List all child accounts of the given account that are accessible to the authenticated user.

    Args:
        account_id (UUID):
        kind (GetAccountsAccountIDAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDAccountsResponse403 | GetAccountsAccountIDAccountsResponse422 | GetAccountsAccountIDAccountsResponse500 | list[GetAccountsAccountIDAccountsAccount]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            kind=kind,
            per_page=per_page,
            page=page,
        )
    ).parsed
