from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_policies_body import PostPoliciesBody
from ...models.post_policies_policy_document import PostPoliciesPolicyDocument
from ...models.post_policies_response_400 import PostPoliciesResponse400
from ...models.post_policies_response_422 import PostPoliciesResponse422
from ...models.post_policies_response_500 import PostPoliciesResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostPoliciesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500 | None:
    if response.status_code == 201:
        response_201 = PostPoliciesPolicyDocument.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostPoliciesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = PostPoliciesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostPoliciesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostPoliciesBody,
) -> Response[PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500]:
    """Create Policy Document

     Creates a new policy document.

    Args:
        body (PostPoliciesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500]
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
    body: PostPoliciesBody,
) -> PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500 | None:
    """Create Policy Document

     Creates a new policy document.

    Args:
        body (PostPoliciesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostPoliciesBody,
) -> Response[PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500]:
    """Create Policy Document

     Creates a new policy document.

    Args:
        body (PostPoliciesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostPoliciesBody,
) -> PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500 | None:
    """Create Policy Document

     Creates a new policy document.

    Args:
        body (PostPoliciesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPoliciesPolicyDocument | PostPoliciesResponse400 | PostPoliciesResponse422 | PostPoliciesResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
