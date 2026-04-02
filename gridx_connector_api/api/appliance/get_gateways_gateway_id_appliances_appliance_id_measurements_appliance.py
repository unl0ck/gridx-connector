from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heater_appliance import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_ev_charging_stations_measurement import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_meters_measurement import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_response_400 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_response_403 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_response_404 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_response_422 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_response_500 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500,
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
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/measurements/appliance".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> (
                GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
                | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
                | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
                | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
                | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_inverters_measurements = (
                        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements.from_dict(
                            data
                        )
                    )

                    return response_200_item_inverters_measurements
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_meters_measurement = (
                        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement.from_dict(data)
                    )

                    return response_200_item_meters_measurement
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_ev_charging_stations_measurement = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement.from_dict(
                        data
                    )

                    return response_200_item_ev_charging_stations_measurement
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_a_measurement_produced_by_a_heatpump_appliance = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance.from_dict(
                        data
                    )

                    return response_200_item_a_measurement_produced_by_a_heatpump_appliance
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_a_measurement_produced_by_a_heater_appliance = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance.from_dict(
                    data
                )

                return response_200_item_a_measurement_produced_by_a_heater_appliance

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403.from_dict(
            response.json()
        )

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404.from_dict(
            response.json()
        )

        return response_404

    if response.status_code == 422:
        response_422 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422.from_dict(
            response.json()
        )

        return response_422

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500.from_dict(
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
]:
    """List Appliance's Raw Measurements

     Lists raw measurements of an appliance over a period of time.

    The provided `interval` must not span more than 24 hours.

    The resolution cannot be controlled. The granularity at which we store
    measurements varies from appliance to appliance, firmware and
    configuration.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing raw measurements is only supported for appliances of type:
    * `INVERTER`
    * `METER`
    * `EVSTATION`
    * `HEAT_PUMP`

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement]]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
    | None
):
    """List Appliance's Raw Measurements

     Lists raw measurements of an appliance over a period of time.

    The provided `interval` must not span more than 24 hours.

    The resolution cannot be controlled. The granularity at which we store
    measurements varies from appliance to appliance, firmware and
    configuration.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing raw measurements is only supported for appliances of type:
    * `INVERTER`
    * `METER`
    * `EVSTATION`
    * `HEAT_PUMP`

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
]:
    """List Appliance's Raw Measurements

     Lists raw measurements of an appliance over a period of time.

    The provided `interval` must not span more than 24 hours.

    The resolution cannot be controlled. The granularity at which we store
    measurements varies from appliance to appliance, firmware and
    configuration.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing raw measurements is only supported for appliances of type:
    * `INVERTER`
    * `METER`
    * `EVSTATION`
    * `HEAT_PUMP`

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement]]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500
    | list[
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements
        | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement
    ]
    | None
):
    """List Appliance's Raw Measurements

     Lists raw measurements of an appliance over a period of time.

    The provided `interval` must not span more than 24 hours.

    The resolution cannot be controlled. The granularity at which we store
    measurements varies from appliance to appliance, firmware and
    configuration.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing raw measurements is only supported for appliances of type:
    * `INVERTER`
    * `METER`
    * `EVSTATION`
    * `HEAT_PUMP`

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeaterAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement]
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            interval=interval,
        )
    ).parsed
