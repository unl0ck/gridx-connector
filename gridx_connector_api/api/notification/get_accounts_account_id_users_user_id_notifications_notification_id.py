from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_users_user_id_notifications_notification_id_response_200 import (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200,
)
from ...models.get_accounts_account_id_users_user_id_notifications_notification_id_response_403 import (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403,
)
from ...models.get_accounts_account_id_users_user_id_notifications_notification_id_response_500 import (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
    notification_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/users/{user_id}/notifications/{notification_id}".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
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
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
]:
    """Retrieve a Notification

     Returns a notification by its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        notification_id=notification_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    user_id: UUID,
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
    | None
):
    """Retrieve a Notification

     Returns a notification by its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        notification_id=notification_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
]:
    """Retrieve a Notification

     Returns a notification by its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        notification_id=notification_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
    | None
):
    """Retrieve a Notification

     Returns a notification by its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse200 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse403 | GetAccountsAccountIDUsersUserIDNotificationsNotificationIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            notification_id=notification_id,
            client=client,
        )
    ).parsed
