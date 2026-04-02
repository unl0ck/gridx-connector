from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_gateways_gateway_id_appliances_appliance_id_body import (
    PatchGatewaysGatewayIDAppliancesApplianceIDBody,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_response_400 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_response_403 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse403,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_response_404 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse404,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_response_422 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse422,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_response_500 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PatchGatewaysGatewayIDAppliancesApplianceIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchGatewaysGatewayIDAppliancesApplianceIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchGatewaysGatewayIDAppliancesApplianceIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchGatewaysGatewayIDAppliancesApplianceIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchGatewaysGatewayIDAppliancesApplianceIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDBody,
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Update an Appliance

     Updates the specific appliance by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDAppliancesApplianceIDResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDBody,
) -> (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Update an Appliance

     Updates the specific appliance by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDAppliancesApplianceIDResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDBody,
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
]:
    """Update an Appliance

     Updates the specific appliance by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDAppliancesApplianceIDResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDBody,
) -> (
    PatchGatewaysGatewayIDAppliancesApplianceIDResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
    | None
):
    """Update an Appliance

     Updates the specific appliance by setting the values of the body parameters.

    Any parameters not provided will be left unchanged.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDAppliancesApplianceIDResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            body=body,
        )
    ).parsed
