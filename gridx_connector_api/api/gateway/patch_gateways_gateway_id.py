from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_gateways_gateway_id_body import PatchGatewaysGatewayIDBody
from ...models.patch_gateways_gateway_id_response_200 import PatchGatewaysGatewayIDResponse200
from ...models.patch_gateways_gateway_id_response_400 import PatchGatewaysGatewayIDResponse400
from ...models.patch_gateways_gateway_id_response_403 import PatchGatewaysGatewayIDResponse403
from ...models.patch_gateways_gateway_id_response_404 import PatchGatewaysGatewayIDResponse404
from ...models.patch_gateways_gateway_id_response_422 import PatchGatewaysGatewayIDResponse422
from ...models.patch_gateways_gateway_id_response_500 import PatchGatewaysGatewayIDResponse500
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    *,
    body: PatchGatewaysGatewayIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/gateways/{gateway_id}".format(
            gateway_id=quote(str(gateway_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchGatewaysGatewayIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchGatewaysGatewayIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchGatewaysGatewayIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchGatewaysGatewayIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchGatewaysGatewayIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchGatewaysGatewayIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDBody,
) -> Response[
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
]:
    """Update a Gateway

     Updates the specific gateway by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        body (PatchGatewaysGatewayIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDResponse200 | PatchGatewaysGatewayIDResponse400 | PatchGatewaysGatewayIDResponse403 | PatchGatewaysGatewayIDResponse404 | PatchGatewaysGatewayIDResponse422 | PatchGatewaysGatewayIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDBody,
) -> (
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
    | None
):
    """Update a Gateway

     Updates the specific gateway by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        body (PatchGatewaysGatewayIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDResponse200 | PatchGatewaysGatewayIDResponse400 | PatchGatewaysGatewayIDResponse403 | PatchGatewaysGatewayIDResponse404 | PatchGatewaysGatewayIDResponse422 | PatchGatewaysGatewayIDResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDBody,
) -> Response[
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
]:
    """Update a Gateway

     Updates the specific gateway by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        body (PatchGatewaysGatewayIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDResponse200 | PatchGatewaysGatewayIDResponse400 | PatchGatewaysGatewayIDResponse403 | PatchGatewaysGatewayIDResponse404 | PatchGatewaysGatewayIDResponse422 | PatchGatewaysGatewayIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDBody,
) -> (
    PatchGatewaysGatewayIDResponse200
    | PatchGatewaysGatewayIDResponse400
    | PatchGatewaysGatewayIDResponse403
    | PatchGatewaysGatewayIDResponse404
    | PatchGatewaysGatewayIDResponse422
    | PatchGatewaysGatewayIDResponse500
    | None
):
    """Update a Gateway

     Updates the specific gateway by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        body (PatchGatewaysGatewayIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDResponse200 | PatchGatewaysGatewayIDResponse400 | PatchGatewaysGatewayIDResponse403 | PatchGatewaysGatewayIDResponse404 | PatchGatewaysGatewayIDResponse422 | PatchGatewaysGatewayIDResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            client=client,
            body=body,
        )
    ).parsed
