from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_accounts_account_id_users_user_id_response_400 import (
    DeleteAccountsAccountIDUsersUserIDResponse400,
)
from ...models.delete_accounts_account_id_users_user_id_response_403 import (
    DeleteAccountsAccountIDUsersUserIDResponse403,
)
from ...models.delete_accounts_account_id_users_user_id_response_500 import (
    DeleteAccountsAccountIDUsersUserIDResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    user_id: UUID,
    *,
    delete_auth0: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["delete-auth0"] = delete_auth0

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{account_id}/users/{user_id}".format(
            account_id=quote(str(account_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteAccountsAccountIDUsersUserIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = DeleteAccountsAccountIDUsersUserIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DeleteAccountsAccountIDUsersUserIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
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
    delete_auth0: bool | Unset = True,
) -> Response[
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
]:
    """Delete User

     Delete a user given its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        delete_auth0 (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountsAccountIDUsersUserIDResponse400 | DeleteAccountsAccountIDUsersUserIDResponse403 | DeleteAccountsAccountIDUsersUserIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        delete_auth0=delete_auth0,
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
    delete_auth0: bool | Unset = True,
) -> (
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
    | None
):
    """Delete User

     Delete a user given its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        delete_auth0 (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountsAccountIDUsersUserIDResponse400 | DeleteAccountsAccountIDUsersUserIDResponse403 | DeleteAccountsAccountIDUsersUserIDResponse500
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
        delete_auth0=delete_auth0,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    delete_auth0: bool | Unset = True,
) -> Response[
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
]:
    """Delete User

     Delete a user given its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        delete_auth0 (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountsAccountIDUsersUserIDResponse400 | DeleteAccountsAccountIDUsersUserIDResponse403 | DeleteAccountsAccountIDUsersUserIDResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        delete_auth0=delete_auth0,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    delete_auth0: bool | Unset = True,
) -> (
    Any
    | DeleteAccountsAccountIDUsersUserIDResponse400
    | DeleteAccountsAccountIDUsersUserIDResponse403
    | DeleteAccountsAccountIDUsersUserIDResponse500
    | None
):
    """Delete User

     Delete a user given its ID.

    Args:
        account_id (UUID):
        user_id (UUID):
        delete_auth0 (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountsAccountIDUsersUserIDResponse400 | DeleteAccountsAccountIDUsersUserIDResponse403 | DeleteAccountsAccountIDUsersUserIDResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
            delete_auth0=delete_auth0,
        )
    ).parsed
