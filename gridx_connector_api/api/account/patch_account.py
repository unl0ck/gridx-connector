from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_account_account import PatchAccountAccount
from ...models.patch_account_body import PatchAccountBody
from ...models.patch_account_response_403 import PatchAccountResponse403
from ...models.patch_account_response_404 import PatchAccountResponse404
from ...models.patch_account_response_422 import PatchAccountResponse422
from ...models.patch_account_response_500 import PatchAccountResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PatchAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/account",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchAccountAccount.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PatchAccountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchAccountResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchAccountResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchAccountResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchAccountBody,
) -> Response[
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
]:
    """Update the authenticated Account

     Update the user data of the authenticated account.

    Args:
        body (PatchAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountAccount | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PatchAccountBody,
) -> (
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
    | None
):
    """Update the authenticated Account

     Update the user data of the authenticated account.

    Args:
        body (PatchAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountAccount | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchAccountBody,
) -> Response[
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
]:
    """Update the authenticated Account

     Update the user data of the authenticated account.

    Args:
        body (PatchAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountAccount | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PatchAccountBody,
) -> (
    PatchAccountAccount
    | PatchAccountResponse403
    | PatchAccountResponse404
    | PatchAccountResponse422
    | PatchAccountResponse500
    | None
):
    """Update the authenticated Account

     Update the user data of the authenticated account.

    Args:
        body (PatchAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountAccount | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
