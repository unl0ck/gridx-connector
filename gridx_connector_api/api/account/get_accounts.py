from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account import GetAccountsAccount
from ...models.get_accounts_kind import GetAccountsKind
from ...models.get_accounts_response_403 import GetAccountsResponse403
from ...models.get_accounts_response_422 import GetAccountsResponse422
from ...models.get_accounts_response_500 import GetAccountsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: GetAccountsKind | Unset = UNSET,
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
        "url": "/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAccountsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetAccountsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    kind: GetAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> Response[GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]]:
    """List all Accounts

     List accounts that are accessible to the authenticated user.

    Args:
        kind (GetAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]]
    """

    kwargs = _get_kwargs(
        kind=kind,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kind: GetAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount] | None:
    """List all Accounts

     List accounts that are accessible to the authenticated user.

    Args:
        kind (GetAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]
    """

    return sync_detailed(
        client=client,
        kind=kind,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: GetAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> Response[GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]]:
    """List all Accounts

     List accounts that are accessible to the authenticated user.

    Args:
        kind (GetAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]]
    """

    kwargs = _get_kwargs(
        kind=kind,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kind: GetAccountsKind | Unset = UNSET,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
) -> GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount] | None:
    """List all Accounts

     List accounts that are accessible to the authenticated user.

    Args:
        kind (GetAccountsKind | Unset):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsResponse403 | GetAccountsResponse422 | GetAccountsResponse500 | list[GetAccountsAccount]
    """

    return (
        await asyncio_detailed(
            client=client,
            kind=kind,
            per_page=per_page,
            page=page,
        )
    ).parsed
