from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_body import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_400 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_403 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_404 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_422 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422,
)
from ...models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_500 import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    body: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/ev/configuration".format(
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
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
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
    body: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Update an EV configuration

     Updates the specified appliance's EV charging station configuration by setting the body parameters.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
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
    body: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Update an EV configuration

     Updates the specified appliance's EV charging station configuration by setting the body parameters.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
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
    body: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> Response[
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Update an EV configuration

     Updates the specified appliance's EV charging station configuration by setting the body parameters.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
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
    body: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Update an EV configuration

     Updates the specified appliance's EV charging station configuration by setting the body parameters.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            body=body,
        )
    ).parsed
