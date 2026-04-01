from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_200_item import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_400 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_403 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_404 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_422 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422,
)
from ...models.get_gateways_gateway_id_appliances_appliance_id_measurements_response_500 import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500,
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
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/measurements".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
]:
    r"""List Appliance's Combined Measurements

     Lists combinations of appliance measurements and energy management
    measurements.

    This endpoints adds a \"convenience\" method for fetching raw measurements
    and energy management measurements together, by combining them into a
    single measurement object.

    It is usually used to inspect the EMS behavior in correspondence to raw
    values reported by the appliance.

    The requested `interval` must not span more than 24 hours.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing combined measurements is only supported for appliances of type:
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
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
    | None
):
    r"""List Appliance's Combined Measurements

     Lists combinations of appliance measurements and energy management
    measurements.

    This endpoints adds a \"convenience\" method for fetching raw measurements
    and energy management measurements together, by combining them into a
    single measurement object.

    It is usually used to inspect the EMS behavior in correspondence to raw
    values reported by the appliance.

    The requested `interval` must not span more than 24 hours.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing combined measurements is only supported for appliances of type:
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
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
]:
    r"""List Appliance's Combined Measurements

     Lists combinations of appliance measurements and energy management
    measurements.

    This endpoints adds a \"convenience\" method for fetching raw measurements
    and energy management measurements together, by combining them into a
    single measurement object.

    It is usually used to inspect the EMS behavior in correspondence to raw
    values reported by the appliance.

    The requested `interval` must not span more than 24 hours.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing combined measurements is only supported for appliances of type:
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
        Response[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]]
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
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422
    | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500
    | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
    | None
):
    r"""List Appliance's Combined Measurements

     Lists combinations of appliance measurements and energy management
    measurements.

    This endpoints adds a \"convenience\" method for fetching raw measurements
    and energy management measurements together, by combining them into a
    single measurement object.

    It is usually used to inspect the EMS behavior in correspondence to raw
    values reported by the appliance.

    The requested `interval` must not span more than 24 hours.

    To retrieve raw measurements of hybrid inverters, use the appliance IDs
    of the children (battery or PV) appliances.

    Listing combined measurements is only supported for appliances of type:
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
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse400 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse403 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse404 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse422 | GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse500 | list[GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsResponse200Item]
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            interval=interval,
        )
    ).parsed
