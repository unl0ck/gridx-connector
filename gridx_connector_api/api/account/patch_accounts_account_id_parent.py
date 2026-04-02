from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_accounts_account_id_parent_account import PatchAccountsAccountIDParentAccount
from ...models.patch_accounts_account_id_parent_body import PatchAccountsAccountIDParentBody
from ...models.patch_accounts_account_id_parent_response_400 import PatchAccountsAccountIDParentResponse400
from ...models.patch_accounts_account_id_parent_response_403 import PatchAccountsAccountIDParentResponse403
from ...models.patch_accounts_account_id_parent_response_500 import PatchAccountsAccountIDParentResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: PatchAccountsAccountIDParentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/accounts/{account_id}/parent".format(
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
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchAccountsAccountIDParentAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchAccountsAccountIDParentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchAccountsAccountIDParentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = PatchAccountsAccountIDParentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
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
    body: PatchAccountsAccountIDParentBody,
) -> Response[
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
]:
    r"""Move account to different parent.

     Moves a b2b account (and all its resources) into a target b2b account that is accessible to the
    authenticated user.
    A b2b account is an account with `kind=\"b2b\"`

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDParentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountsAccountIDParentAccount | PatchAccountsAccountIDParentResponse400 | PatchAccountsAccountIDParentResponse403 | PatchAccountsAccountIDParentResponse500]
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
    body: PatchAccountsAccountIDParentBody,
) -> (
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
    | None
):
    r"""Move account to different parent.

     Moves a b2b account (and all its resources) into a target b2b account that is accessible to the
    authenticated user.
    A b2b account is an account with `kind=\"b2b\"`

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDParentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountsAccountIDParentAccount | PatchAccountsAccountIDParentResponse400 | PatchAccountsAccountIDParentResponse403 | PatchAccountsAccountIDParentResponse500
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
    body: PatchAccountsAccountIDParentBody,
) -> Response[
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
]:
    r"""Move account to different parent.

     Moves a b2b account (and all its resources) into a target b2b account that is accessible to the
    authenticated user.
    A b2b account is an account with `kind=\"b2b\"`

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDParentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountsAccountIDParentAccount | PatchAccountsAccountIDParentResponse400 | PatchAccountsAccountIDParentResponse403 | PatchAccountsAccountIDParentResponse500]
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
    body: PatchAccountsAccountIDParentBody,
) -> (
    PatchAccountsAccountIDParentAccount
    | PatchAccountsAccountIDParentResponse400
    | PatchAccountsAccountIDParentResponse403
    | PatchAccountsAccountIDParentResponse500
    | None
):
    r"""Move account to different parent.

     Moves a b2b account (and all its resources) into a target b2b account that is accessible to the
    authenticated user.
    A b2b account is an account with `kind=\"b2b\"`

    Args:
        account_id (UUID):
        body (PatchAccountsAccountIDParentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountsAccountIDParentAccount | PatchAccountsAccountIDParentResponse400 | PatchAccountsAccountIDParentResponse403 | PatchAccountsAccountIDParentResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
