from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_users_user_id_notifications_response_200_item import (
    GetAccountsAccountIDUsersUserIDNotificationsResponse200Item,
)
from ...models.get_accounts_account_id_users_user_id_notifications_response_403 import (
    GetAccountsAccountIDUsersUserIDNotificationsResponse403,
)
from ...models.get_accounts_account_id_users_user_id_notifications_response_500 import (
    GetAccountsAccountIDUsersUserIDNotificationsResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
    *,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    unread: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["unread"] = unread

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/users/{user_id}/notifications".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDUsersUserIDNotificationsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDUsersUserIDNotificationsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDUsersUserIDNotificationsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    unread: bool | Unset = UNSET,
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
]:
    """List all Notifications

     Lists all notification for a user.

    User ID may be explicitly specified as a path parameter,
    otherwise the authenticated user will be used.

    Args:
        account_id (UUID):
        user_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        unread (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsResponse403 | GetAccountsAccountIDUsersUserIDNotificationsResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        per_page=per_page,
        page=page,
        unread=unread,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    unread: bool | Unset = UNSET,
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
    | None
):
    """List all Notifications

     Lists all notification for a user.

    User ID may be explicitly specified as a path parameter,
    otherwise the authenticated user will be used.

    Args:
        account_id (UUID):
        user_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        unread (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsResponse403 | GetAccountsAccountIDUsersUserIDNotificationsResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
        per_page=per_page,
        page=page,
        unread=unread,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    unread: bool | Unset = UNSET,
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
]:
    """List all Notifications

     Lists all notification for a user.

    User ID may be explicitly specified as a path parameter,
    otherwise the authenticated user will be used.

    Args:
        account_id (UUID):
        user_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        unread (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsResponse403 | GetAccountsAccountIDUsersUserIDNotificationsResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        per_page=per_page,
        page=page,
        unread=unread,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    per_page: int | Unset = 20,
    page: int | Unset = 1,
    unread: bool | Unset = UNSET,
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
    | None
):
    """List all Notifications

     Lists all notification for a user.

    User ID may be explicitly specified as a path parameter,
    otherwise the authenticated user will be used.

    Args:
        account_id (UUID):
        user_id (UUID):
        per_page (int | Unset):  Default: 20.
        page (int | Unset):  Default: 1.
        unread (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsResponse403 | GetAccountsAccountIDUsersUserIDNotificationsResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsResponse200Item]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
            per_page=per_page,
            page=page,
            unread=unread,
        )
    ).parsed
