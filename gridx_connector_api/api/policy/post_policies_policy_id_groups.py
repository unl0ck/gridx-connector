from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_policies_policy_id_groups_body import PostPoliciesPolicyIDGroupsBody
from ...models.post_policies_policy_id_groups_response_400 import PostPoliciesPolicyIDGroupsResponse400
from ...models.post_policies_policy_id_groups_response_422 import PostPoliciesPolicyIDGroupsResponse422
from ...models.post_policies_policy_id_groups_response_500 import PostPoliciesPolicyIDGroupsResponse500
from ...types import Response


def _get_kwargs(
    policy_id: UUID,
    *,
    body: PostPoliciesPolicyIDGroupsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/{policy_id}/groups".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = PostPoliciesPolicyIDGroupsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = PostPoliciesPolicyIDGroupsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostPoliciesPolicyIDGroupsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostPoliciesPolicyIDGroupsBody,
) -> Response[
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
]:
    """Assign Policy Document to Group

    Args:
        policy_id (UUID):
        body (PostPoliciesPolicyIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPoliciesPolicyIDGroupsResponse400 | PostPoliciesPolicyIDGroupsResponse422 | PostPoliciesPolicyIDGroupsResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostPoliciesPolicyIDGroupsBody,
) -> (
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
    | None
):
    """Assign Policy Document to Group

    Args:
        policy_id (UUID):
        body (PostPoliciesPolicyIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPoliciesPolicyIDGroupsResponse400 | PostPoliciesPolicyIDGroupsResponse422 | PostPoliciesPolicyIDGroupsResponse500
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostPoliciesPolicyIDGroupsBody,
) -> Response[
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
]:
    """Assign Policy Document to Group

    Args:
        policy_id (UUID):
        body (PostPoliciesPolicyIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPoliciesPolicyIDGroupsResponse400 | PostPoliciesPolicyIDGroupsResponse422 | PostPoliciesPolicyIDGroupsResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostPoliciesPolicyIDGroupsBody,
) -> (
    Any
    | PostPoliciesPolicyIDGroupsResponse400
    | PostPoliciesPolicyIDGroupsResponse422
    | PostPoliciesPolicyIDGroupsResponse500
    | None
):
    """Assign Policy Document to Group

    Args:
        policy_id (UUID):
        body (PostPoliciesPolicyIDGroupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPoliciesPolicyIDGroupsResponse400 | PostPoliciesPolicyIDGroupsResponse422 | PostPoliciesPolicyIDGroupsResponse500
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            body=body,
        )
    ).parsed
