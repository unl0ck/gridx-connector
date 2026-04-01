from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_system_id_gateways_body import PostSystemsSystemIDGatewaysBody
from ...models.post_systems_system_id_gateways_response_201 import PostSystemsSystemIDGatewaysResponse201
from ...models.post_systems_system_id_gateways_response_403 import PostSystemsSystemIDGatewaysResponse403
from ...models.post_systems_system_id_gateways_response_404 import PostSystemsSystemIDGatewaysResponse404
from ...models.post_systems_system_id_gateways_response_422 import PostSystemsSystemIDGatewaysResponse422
from ...models.post_systems_system_id_gateways_response_500 import PostSystemsSystemIDGatewaysResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PostSystemsSystemIDGatewaysBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systems/{system_id}/gateways".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostSystemsSystemIDGatewaysResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = PostSystemsSystemIDGatewaysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemsSystemIDGatewaysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostSystemsSystemIDGatewaysResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostSystemsSystemIDGatewaysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDGatewaysBody,
) -> Response[
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
]:
    """Create a System's Gateway

     Creates a gateway.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDGatewaysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDGatewaysResponse201 | PostSystemsSystemIDGatewaysResponse403 | PostSystemsSystemIDGatewaysResponse404 | PostSystemsSystemIDGatewaysResponse422 | PostSystemsSystemIDGatewaysResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDGatewaysBody,
) -> (
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
    | None
):
    """Create a System's Gateway

     Creates a gateway.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDGatewaysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDGatewaysResponse201 | PostSystemsSystemIDGatewaysResponse403 | PostSystemsSystemIDGatewaysResponse404 | PostSystemsSystemIDGatewaysResponse422 | PostSystemsSystemIDGatewaysResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDGatewaysBody,
) -> Response[
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
]:
    """Create a System's Gateway

     Creates a gateway.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDGatewaysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDGatewaysResponse201 | PostSystemsSystemIDGatewaysResponse403 | PostSystemsSystemIDGatewaysResponse404 | PostSystemsSystemIDGatewaysResponse422 | PostSystemsSystemIDGatewaysResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDGatewaysBody,
) -> (
    PostSystemsSystemIDGatewaysResponse201
    | PostSystemsSystemIDGatewaysResponse403
    | PostSystemsSystemIDGatewaysResponse404
    | PostSystemsSystemIDGatewaysResponse422
    | PostSystemsSystemIDGatewaysResponse500
    | None
):
    """Create a System's Gateway

     Creates a gateway.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDGatewaysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDGatewaysResponse201 | PostSystemsSystemIDGatewaysResponse403 | PostSystemsSystemIDGatewaysResponse404 | PostSystemsSystemIDGatewaysResponse422 | PostSystemsSystemIDGatewaysResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
