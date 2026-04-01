from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_body import PostSystemsBody
from ...models.post_systems_response_403 import PostSystemsResponse403
from ...models.post_systems_response_422 import PostSystemsResponse422
from ...models.post_systems_response_500 import PostSystemsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostSystemsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systems",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500 | None:
    if response.status_code == 403:
        response_403 = PostSystemsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostSystemsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostSystemsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSystemsBody,
) -> Response[PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500]:
    """Create a System

     Creates a System.

    Args:
        body (PostSystemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500]
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
    body: PostSystemsBody,
) -> PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500 | None:
    """Create a System

     Creates a System.

    Args:
        body (PostSystemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSystemsBody,
) -> Response[PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500]:
    """Create a System

     Creates a System.

    Args:
        body (PostSystemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostSystemsBody,
) -> PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500 | None:
    """Create a System

     Creates a System.

    Args:
        body (PostSystemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsResponse403 | PostSystemsResponse422 | PostSystemsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
