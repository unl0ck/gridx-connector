from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item import (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item,
)
from ...models.get_accounts_account_id_users_user_id_notifications_rules_response_403 import (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403,
)
from ...models.get_accounts_account_id_users_user_id_notifications_rules_response_500 import (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/users/{user_id}/notifications/rules".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
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
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
]:
    """List all Rules

     Lists all rules for the user.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
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
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
    | None
):
    """List all Rules

     Lists all rules for the user.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
]:
    """List all Rules

     Lists all rules for the user.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
    | None
):
    """List all Rules

     Lists all rules for the user.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | GetAccountsAccountIDUsersUserIDNotificationsRulesResponse500 | list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
