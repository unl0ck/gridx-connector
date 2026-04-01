from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_accounts_account_id_users_user_id_notifications_rules_rule_id_body import (
    PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
)
from ...models.put_accounts_account_id_users_user_id_notifications_rules_rule_id_response_403 import (
    PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403,
)
from ...models.put_accounts_account_id_users_user_id_notifications_rules_rule_id_response_500 import (
    PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
    rule_id: UUID,
    *,
    body: PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/{account_id}/users/{user_id}/notifications/rules/{rule_id}".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
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
    rule_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
) -> Response[
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
]:
    """Update a Rule

     Updates a rule specified by its ID.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        rule_id (UUID):
        body (PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403 | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        rule_id=rule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    user_id: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
) -> (
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
    | None
):
    """Update a Rule

     Updates a rule specified by its ID.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        rule_id (UUID):
        body (PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403 | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        rule_id=rule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
) -> Response[
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
]:
    """Update a Rule

     Updates a rule specified by its ID.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        rule_id (UUID):
        body (PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403 | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        rule_id=rule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody,
) -> (
    Any
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403
    | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
    | None
):
    """Update a Rule

     Updates a rule specified by its ID.

    The user and account may be specified explicitly via path parameters or implicitly via the
    authentication context. Explicitly specified values take precedence.

    Args:
        account_id (UUID):
        user_id (UUID):
        rule_id (UUID):
        body (PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse403 | PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            rule_id=rule_id,
            client=client,
            body=body,
        )
    ).parsed
