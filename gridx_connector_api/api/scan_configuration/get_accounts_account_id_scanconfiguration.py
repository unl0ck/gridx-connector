from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_scanconfiguration_response_404 import (
    GetAccountsAccountIDScanconfigurationResponse404,
)
from ...models.get_accounts_account_id_scanconfiguration_response_422 import (
    GetAccountsAccountIDScanconfigurationResponse422,
)
from ...models.get_accounts_account_id_scanconfiguration_response_500 import (
    GetAccountsAccountIDScanconfigurationResponse500,
)
from ...models.get_accounts_account_id_scanconfiguration_scan_configuration import (
    GetAccountsAccountIDScanconfigurationScanConfiguration,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/scanconfiguration".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    if response.status_code == 200:
        response_200 = GetAccountsAccountIDScanconfigurationScanConfiguration.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetAccountsAccountIDScanconfigurationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetAccountsAccountIDScanconfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDScanconfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
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
) -> Response[
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
]:
    """Retrieve Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDScanconfigurationResponse404 | GetAccountsAccountIDScanconfigurationResponse422 | GetAccountsAccountIDScanconfigurationResponse500 | GetAccountsAccountIDScanconfigurationScanConfiguration]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    """Retrieve Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDScanconfigurationResponse404 | GetAccountsAccountIDScanconfigurationResponse422 | GetAccountsAccountIDScanconfigurationResponse500 | GetAccountsAccountIDScanconfigurationScanConfiguration
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
]:
    """Retrieve Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDScanconfigurationResponse404 | GetAccountsAccountIDScanconfigurationResponse422 | GetAccountsAccountIDScanconfigurationResponse500 | GetAccountsAccountIDScanconfigurationScanConfiguration]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDScanconfigurationResponse404
    | GetAccountsAccountIDScanconfigurationResponse422
    | GetAccountsAccountIDScanconfigurationResponse500
    | GetAccountsAccountIDScanconfigurationScanConfiguration
    | None
):
    """Retrieve Scan Configuration

    Args:
        account_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDScanconfigurationResponse404 | GetAccountsAccountIDScanconfigurationResponse422 | GetAccountsAccountIDScanconfigurationResponse500 | GetAccountsAccountIDScanconfigurationScanConfiguration
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
