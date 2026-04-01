from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_accounts_account_id_bidding_zone_body import PutAccountsAccountIDBiddingZoneBody
from ...models.put_accounts_account_id_bidding_zone_response_200 import PutAccountsAccountIDBiddingZoneResponse200
from ...models.put_accounts_account_id_bidding_zone_response_403 import PutAccountsAccountIDBiddingZoneResponse403
from ...models.put_accounts_account_id_bidding_zone_response_404 import PutAccountsAccountIDBiddingZoneResponse404
from ...models.put_accounts_account_id_bidding_zone_response_422 import PutAccountsAccountIDBiddingZoneResponse422
from ...models.put_accounts_account_id_bidding_zone_response_500 import PutAccountsAccountIDBiddingZoneResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: PutAccountsAccountIDBiddingZoneBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/{account_id}/bidding-zone".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.gridx.v2+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PutAccountsAccountIDBiddingZoneResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PutAccountsAccountIDBiddingZoneResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutAccountsAccountIDBiddingZoneResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PutAccountsAccountIDBiddingZoneResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PutAccountsAccountIDBiddingZoneResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
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
    body: PutAccountsAccountIDBiddingZoneBody,
) -> Response[
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
]:
    """Set bidding zone

     Set the electricity market bidding zone of the given accountID.

    Args:
        account_id (UUID):
        body (PutAccountsAccountIDBiddingZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAccountsAccountIDBiddingZoneResponse200 | PutAccountsAccountIDBiddingZoneResponse403 | PutAccountsAccountIDBiddingZoneResponse404 | PutAccountsAccountIDBiddingZoneResponse422 | PutAccountsAccountIDBiddingZoneResponse500]
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
    body: PutAccountsAccountIDBiddingZoneBody,
) -> (
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
    | None
):
    """Set bidding zone

     Set the electricity market bidding zone of the given accountID.

    Args:
        account_id (UUID):
        body (PutAccountsAccountIDBiddingZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAccountsAccountIDBiddingZoneResponse200 | PutAccountsAccountIDBiddingZoneResponse403 | PutAccountsAccountIDBiddingZoneResponse404 | PutAccountsAccountIDBiddingZoneResponse422 | PutAccountsAccountIDBiddingZoneResponse500
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
    body: PutAccountsAccountIDBiddingZoneBody,
) -> Response[
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
]:
    """Set bidding zone

     Set the electricity market bidding zone of the given accountID.

    Args:
        account_id (UUID):
        body (PutAccountsAccountIDBiddingZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAccountsAccountIDBiddingZoneResponse200 | PutAccountsAccountIDBiddingZoneResponse403 | PutAccountsAccountIDBiddingZoneResponse404 | PutAccountsAccountIDBiddingZoneResponse422 | PutAccountsAccountIDBiddingZoneResponse500]
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
    body: PutAccountsAccountIDBiddingZoneBody,
) -> (
    PutAccountsAccountIDBiddingZoneResponse200
    | PutAccountsAccountIDBiddingZoneResponse403
    | PutAccountsAccountIDBiddingZoneResponse404
    | PutAccountsAccountIDBiddingZoneResponse422
    | PutAccountsAccountIDBiddingZoneResponse500
    | None
):
    """Set bidding zone

     Set the electricity market bidding zone of the given accountID.

    Args:
        account_id (UUID):
        body (PutAccountsAccountIDBiddingZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAccountsAccountIDBiddingZoneResponse200 | PutAccountsAccountIDBiddingZoneResponse403 | PutAccountsAccountIDBiddingZoneResponse404 | PutAccountsAccountIDBiddingZoneResponse422 | PutAccountsAccountIDBiddingZoneResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
