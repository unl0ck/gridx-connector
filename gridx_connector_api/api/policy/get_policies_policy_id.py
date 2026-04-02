from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_policies_policy_id_policy_document import GetPoliciesPolicyIDPolicyDocument
from ...models.get_policies_policy_id_response_404 import GetPoliciesPolicyIDResponse404
from ...models.get_policies_policy_id_response_422 import GetPoliciesPolicyIDResponse422
from ...models.get_policies_policy_id_response_500 import GetPoliciesPolicyIDResponse500
from ...types import Response


def _get_kwargs(
    policy_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetPoliciesPolicyIDPolicyDocument.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetPoliciesPolicyIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetPoliciesPolicyIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetPoliciesPolicyIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
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
) -> Response[
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
]:
    """Get Policy Document

     Gets policy document based on its ID.

    Args:
        policy_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPoliciesPolicyIDPolicyDocument | GetPoliciesPolicyIDResponse404 | GetPoliciesPolicyIDResponse422 | GetPoliciesPolicyIDResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
    | None
):
    """Get Policy Document

     Gets policy document based on its ID.

    Args:
        policy_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPoliciesPolicyIDPolicyDocument | GetPoliciesPolicyIDResponse404 | GetPoliciesPolicyIDResponse422 | GetPoliciesPolicyIDResponse500
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
]:
    """Get Policy Document

     Gets policy document based on its ID.

    Args:
        policy_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPoliciesPolicyIDPolicyDocument | GetPoliciesPolicyIDResponse404 | GetPoliciesPolicyIDResponse422 | GetPoliciesPolicyIDResponse500]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetPoliciesPolicyIDPolicyDocument
    | GetPoliciesPolicyIDResponse404
    | GetPoliciesPolicyIDResponse422
    | GetPoliciesPolicyIDResponse500
    | None
):
    """Get Policy Document

     Gets policy document based on its ID.

    Args:
        policy_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPoliciesPolicyIDPolicyDocument | GetPoliciesPolicyIDResponse404 | GetPoliciesPolicyIDResponse422 | GetPoliciesPolicyIDResponse500
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
        )
    ).parsed
