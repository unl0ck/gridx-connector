from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_accounts_account_id_users_user_id_notifications_rules_body import (
    PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
)
from ...models.post_accounts_account_id_users_user_id_notifications_rules_response_201 import (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201,
)
from ...models.post_accounts_account_id_users_user_id_notifications_rules_response_403 import (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403,
)
from ...models.post_accounts_account_id_users_user_id_notifications_rules_response_500 import (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
    *,
    body: PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/users/{user_id}/notifications/rules".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
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
    body: PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
) -> Response[
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
]:
    """Create a Rule

     Creates a new rule.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        body (PostAccountsAccountIDUsersUserIDNotificationsRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        body=body,
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
    body: PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
) -> (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | None
):
    """Create a Rule

     Creates a new rule.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        body (PostAccountsAccountIDUsersUserIDNotificationsRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
) -> Response[
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
]:
    """Create a Rule

     Creates a new rule.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        body (PostAccountsAccountIDUsersUserIDNotificationsRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostAccountsAccountIDUsersUserIDNotificationsRulesBody,
) -> (
    PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403
    | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    | None
):
    """Create a Rule

     Creates a new rule.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        body (PostAccountsAccountIDUsersUserIDNotificationsRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse403 | PostAccountsAccountIDUsersUserIDNotificationsRulesResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
