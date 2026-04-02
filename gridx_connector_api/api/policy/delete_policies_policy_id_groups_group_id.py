from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_policies_policy_id_groups_group_id_response_400 import (
    DeletePoliciesPolicyIDGroupsGroupIDResponse400,
)
from ...models.delete_policies_policy_id_groups_group_id_response_422 import (
    DeletePoliciesPolicyIDGroupsGroupIDResponse422,
)
from ...models.delete_policies_policy_id_groups_group_id_response_500 import (
    DeletePoliciesPolicyIDGroupsGroupIDResponse500,
)
from ...types import Response


def _get_kwargs(
    policy_id: UUID,
    group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/policies/{policy_id}/groups/{group_id}".format(
            policy_id=quote(str(policy_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeletePoliciesPolicyIDGroupsGroupIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = DeletePoliciesPolicyIDGroupsGroupIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = DeletePoliciesPolicyIDGroupsGroupIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
]:
    """Unassign Policy Document from Group

    Args:
        policy_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePoliciesPolicyIDGroupsGroupIDResponse400 | DeletePoliciesPolicyIDGroupsGroupIDResponse422 | DeletePoliciesPolicyIDGroupsGroupIDResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
    | None
):
    """Unassign Policy Document from Group

    Args:
        policy_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePoliciesPolicyIDGroupsGroupIDResponse400 | DeletePoliciesPolicyIDGroupsGroupIDResponse422 | DeletePoliciesPolicyIDGroupsGroupIDResponse500
    """

    return sync_detailed(
        policy_id=policy_id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
]:
    """Unassign Policy Document from Group

    Args:
        policy_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePoliciesPolicyIDGroupsGroupIDResponse400 | DeletePoliciesPolicyIDGroupsGroupIDResponse422 | DeletePoliciesPolicyIDGroupsGroupIDResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | DeletePoliciesPolicyIDGroupsGroupIDResponse400
    | DeletePoliciesPolicyIDGroupsGroupIDResponse422
    | DeletePoliciesPolicyIDGroupsGroupIDResponse500
    | None
):
    """Unassign Policy Document from Group

    Args:
        policy_id (UUID):
        group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePoliciesPolicyIDGroupsGroupIDResponse400 | DeletePoliciesPolicyIDGroupsGroupIDResponse422 | DeletePoliciesPolicyIDGroupsGroupIDResponse500
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            group_id=group_id,
            client=client,
        )
    ).parsed
