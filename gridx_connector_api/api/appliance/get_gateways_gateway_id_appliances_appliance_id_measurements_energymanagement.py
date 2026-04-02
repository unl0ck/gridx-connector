from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_energymanagement_energy_management_measurement import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_energymanagement_response_403 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_energymanagement_response_404 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_energymanagement_response_422 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_energymanagement_response_500 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500,
)
from ...types import UNSET, Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    interval: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/measurements/energymanagement".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
    | None
):
    if response.status_code == 200:
        response_200 = (
            GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403.from_dict(
            response.json()
        )

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404.from_dict(
            response.json()
        )

        return response_404

    if response.status_code == 422:
        response_422 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422.from_dict(
            response.json()
        )

        return response_422

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500.from_dict(
            response.json()
        )

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
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
    interval: str,
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
]:
    """List Appliance's Energy Management Measurements

     Lists energy management measurements of an appliance over a period of time.
    Data points returned are emitted directly by the Energy Management
    System (EMS), therefore the resolution cannot be controlled. The
    granularity at which we store measurements depends on the EMS mode and
    configuration.
    The provided `interval` must not span more than 24 hours.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        interval=interval,
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
    interval: str,
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
    | None
):
    """List Appliance's Energy Management Measurements

     Lists energy management measurements of an appliance over a period of time.
    Data points returned are emitted directly by the Energy Management
    System (EMS), therefore the resolution cannot be controlled. The
    granularity at which we store measurements depends on the EMS mode and
    configuration.
    The provided `interval` must not span more than 24 hours.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        client=client,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
]:
    """List Appliance's Energy Management Measurements

     Lists energy management measurements of an appliance over a period of time.
    Data points returned are emitted directly by the Energy Management
    System (EMS), therefore the resolution cannot be controlled. The
    granularity at which we store measurements depends on the EMS mode and
    configuration.
    The provided `interval` must not span more than 24 hours.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        interval=interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
    | None
):
    """List Appliance's Energy Management Measurements

     Lists energy management measurements of an appliance over a period of time.
    Data points returned are emitted directly by the Energy Management
    System (EMS), therefore the resolution cannot be controlled. The
    granularity at which we store measurements depends on the EMS mode and
    configuration.
    The provided `interval` must not span more than 24 hours.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementEnergyManagementMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsEnergymanagementResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            interval=interval,
        )
    ).parsed
