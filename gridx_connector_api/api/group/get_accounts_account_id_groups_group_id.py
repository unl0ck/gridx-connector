from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_groups_group_id_response_200 import GetAccountsAccountIDGroupsGroupIDResponse200
from ...models.get_accounts_account_id_groups_group_id_response_403 import GetAccountsAccountIDGroupsGroupIDResponse403
from ...models.get_accounts_account_id_groups_group_id_response_422 import GetAccountsAccountIDGroupsGroupIDResponse422
from ...models.get_accounts_account_id_groups_group_id_response_500 import GetAccountsAccountIDGroupsGroupIDResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/groups/{group_id}".format(
            account_id=quote(str(account_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetAccountsAccountIDGroupsGroupIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDGroupsGroupIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAccountsAccountIDGroupsGroupIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDGroupsGroupIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
]:
    """Retrieve a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDGroupsGroupIDResponse200 | GetAccountsAccountIDGroupsGroupIDResponse403 | GetAccountsAccountIDGroupsGroupIDResponse422 | GetAccountsAccountIDGroupsGroupIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
    | None
):
    """Retrieve a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDGroupsGroupIDResponse200 | GetAccountsAccountIDGroupsGroupIDResponse403 | GetAccountsAccountIDGroupsGroupIDResponse422 | GetAccountsAccountIDGroupsGroupIDResponse500
    """

    return sync_detailed(
        account_id=account_id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
]:
    """Retrieve a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDGroupsGroupIDResponse200 | GetAccountsAccountIDGroupsGroupIDResponse403 | GetAccountsAccountIDGroupsGroupIDResponse422 | GetAccountsAccountIDGroupsGroupIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDGroupsGroupIDResponse200
    | GetAccountsAccountIDGroupsGroupIDResponse403
    | GetAccountsAccountIDGroupsGroupIDResponse422
    | GetAccountsAccountIDGroupsGroupIDResponse500
    | None
):
    """Retrieve a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDGroupsGroupIDResponse200 | GetAccountsAccountIDGroupsGroupIDResponse403 | GetAccountsAccountIDGroupsGroupIDResponse422 | GetAccountsAccountIDGroupsGroupIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            group_id=group_id,
            client=client,
        )
    ).parsed
