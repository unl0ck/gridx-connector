from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_accounts_account_id_scanconfiguration_body import PostAccountsAccountIDScanconfigurationBody
from ...models.post_accounts_account_id_scanconfiguration_response_422 import (
    PostAccountsAccountIDScanconfigurationResponse422,
)
from ...models.post_accounts_account_id_scanconfiguration_response_500 import (
    PostAccountsAccountIDScanconfigurationResponse500,
)
from ...models.post_accounts_account_id_scanconfiguration_scan_configuration import (
    PostAccountsAccountIDScanconfigurationScanConfiguration,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: PostAccountsAccountIDScanconfigurationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/scanconfiguration".format(
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
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    if response.status_code == 201:
        response_201 = PostAccountsAccountIDScanconfigurationScanConfiguration.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = PostAccountsAccountIDScanconfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostAccountsAccountIDScanconfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
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
    body: PostAccountsAccountIDScanconfigurationBody,
) -> Response[
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
]:
    """Create a Scan Configuration

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDScanconfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDScanconfigurationResponse422 | PostAccountsAccountIDScanconfigurationResponse500 | PostAccountsAccountIDScanconfigurationScanConfiguration]
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
    body: PostAccountsAccountIDScanconfigurationBody,
) -> (
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    """Create a Scan Configuration

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDScanconfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDScanconfigurationResponse422 | PostAccountsAccountIDScanconfigurationResponse500 | PostAccountsAccountIDScanconfigurationScanConfiguration
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
    body: PostAccountsAccountIDScanconfigurationBody,
) -> Response[
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
]:
    """Create a Scan Configuration

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDScanconfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDScanconfigurationResponse422 | PostAccountsAccountIDScanconfigurationResponse500 | PostAccountsAccountIDScanconfigurationScanConfiguration]
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
    body: PostAccountsAccountIDScanconfigurationBody,
) -> (
    PostAccountsAccountIDScanconfigurationResponse422
    | PostAccountsAccountIDScanconfigurationResponse500
    | PostAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    """Create a Scan Configuration

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDScanconfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDScanconfigurationResponse422 | PostAccountsAccountIDScanconfigurationResponse500 | PostAccountsAccountIDScanconfigurationScanConfiguration
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
