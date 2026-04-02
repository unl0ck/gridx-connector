from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_accounts_account_id_groups_body import PostAccountsAccountIDGroupsBody
from ...models.post_accounts_account_id_groups_policy_group import PostAccountsAccountIDGroupsPolicyGroup
from ...models.post_accounts_account_id_groups_response_403 import PostAccountsAccountIDGroupsResponse403
from ...models.post_accounts_account_id_groups_response_422 import PostAccountsAccountIDGroupsResponse422
from ...models.post_accounts_account_id_groups_response_500 import PostAccountsAccountIDGroupsResponse500
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    *,
    body: PostAccountsAccountIDGroupsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/groups".format(
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
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostAccountsAccountIDGroupsPolicyGroup.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PostAccountsAccountIDGroupsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostAccountsAccountIDGroupsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostAccountsAccountIDGroupsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
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
    body: PostAccountsAccountIDGroupsBody,
) -> Response[
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
]:
    """Create a Group

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDGroupsPolicyGroup | PostAccountsAccountIDGroupsResponse403 | PostAccountsAccountIDGroupsResponse422 | PostAccountsAccountIDGroupsResponse500]
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
    body: PostAccountsAccountIDGroupsBody,
) -> (
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
    | None
):
    """Create a Group

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDGroupsPolicyGroup | PostAccountsAccountIDGroupsResponse403 | PostAccountsAccountIDGroupsResponse422 | PostAccountsAccountIDGroupsResponse500
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
    body: PostAccountsAccountIDGroupsBody,
) -> Response[
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
]:
    """Create a Group

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountsAccountIDGroupsPolicyGroup | PostAccountsAccountIDGroupsResponse403 | PostAccountsAccountIDGroupsResponse422 | PostAccountsAccountIDGroupsResponse500]
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
    body: PostAccountsAccountIDGroupsBody,
) -> (
    PostAccountsAccountIDGroupsPolicyGroup
    | PostAccountsAccountIDGroupsResponse403
    | PostAccountsAccountIDGroupsResponse422
    | PostAccountsAccountIDGroupsResponse500
    | None
):
    """Create a Group

    Args:
        account_id (UUID):
        body (PostAccountsAccountIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountsAccountIDGroupsPolicyGroup | PostAccountsAccountIDGroupsResponse403 | PostAccountsAccountIDGroupsResponse422 | PostAccountsAccountIDGroupsResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
