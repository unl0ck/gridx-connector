from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_accounts_account import PostAccountsAccount
from ...models.post_accounts_body import PostAccountsBody
from ...models.post_accounts_response_403 import PostAccountsResponse403
from ...models.post_accounts_response_422 import PostAccountsResponse422
from ...models.post_accounts_response_500 import PostAccountsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostAccountsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountsAccount.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = PostAccountsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostAccountsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostAccountsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAccountsBody,
) -> Response[PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500]:
    """Create an Account

     Create a new account for the authenticated user. The child account will inherit the authenticated
    accounts information.

    Args:
        body (PostAccountsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500]
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
    body: PostAccountsBody,
) -> PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500 | None:
    """Create an Account

     Create a new account for the authenticated user. The child account will inherit the authenticated
    accounts information.

    Args:
        body (PostAccountsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAccountsBody,
) -> Response[PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500]:
    """Create an Account

     Create a new account for the authenticated user. The child account will inherit the authenticated
    accounts information.

    Args:
        body (PostAccountsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostAccountsBody,
) -> PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500 | None:
    """Create an Account

     Create a new account for the authenticated user. The child account will inherit the authenticated
    accounts information.

    Args:
        body (PostAccountsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccount | PostAccountsResponse403 | PostAccountsResponse422 | PostAccountsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
