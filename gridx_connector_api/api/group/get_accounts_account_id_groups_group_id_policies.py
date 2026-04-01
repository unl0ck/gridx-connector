from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accounts_account_id_groups_group_id_policies_policy_document import (
    GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument,
)
from ...models.get_accounts_account_id_groups_group_id_policies_response_403 import (
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403,
)
from ...models.get_accounts_account_id_groups_group_id_policies_response_500 import (
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse500,
)
from ...types import Response


def _get_kwargs(
    account_id: UUID,
    group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/groups/{group_id}/policies".format(
            account_id=quote(str(account_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetAccountsAccountIDGroupsGroupIDPoliciesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetAccountsAccountIDGroupsGroupIDPoliciesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
]:
    """Get Policy Documents in a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDGroupsGroupIDPoliciesResponse403 | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500 | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
    | None
):
    """Get Policy Documents in a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDGroupsGroupIDPoliciesResponse403 | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500 | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
    """

    return sync_detailed(
        account_id=account_id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
]:
    """Get Policy Documents in a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountsAccountIDGroupsGroupIDPoliciesResponse403 | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500 | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetAccountsAccountIDGroupsGroupIDPoliciesResponse403
    | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500
    | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
    | None
):
    """Get Policy Documents in a Group

    Args:
        account_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountsAccountIDGroupsGroupIDPoliciesResponse403 | GetAccountsAccountIDGroupsGroupIDPoliciesResponse500 | list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            group_id=group_id,
            client=client,
        )
    ).parsed
