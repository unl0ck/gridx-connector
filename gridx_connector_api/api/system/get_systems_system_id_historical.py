from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_historical_measurements import GetSystemsSystemIDHistoricalMeasurements
from ...models.get_systems_system_id_historical_resolution import GetSystemsSystemIDHistoricalResolution
from ...models.get_systems_system_id_historical_response_403 import GetSystemsSystemIDHistoricalResponse403
from ...models.get_systems_system_id_historical_response_404 import GetSystemsSystemIDHistoricalResponse404
from ...models.get_systems_system_id_historical_response_422 import GetSystemsSystemIDHistoricalResponse422
from ...models.get_systems_system_id_historical_response_500 import GetSystemsSystemIDHistoricalResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_id: UUID,
    *,
    interval: str,
    resolution: GetSystemsSystemIDHistoricalResolution | Unset = GetSystemsSystemIDHistoricalResolution.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    json_resolution: str | Unset = UNSET
    if not isinstance(resolution, Unset):
        json_resolution = resolution.value

    params["resolution"] = json_resolution

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/historical".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDHistoricalMeasurements.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDHistoricalResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDHistoricalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDHistoricalResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDHistoricalResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
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
    interval: str,
    resolution: GetSystemsSystemIDHistoricalResolution | Unset = GetSystemsSystemIDHistoricalResolution.VALUE_1,
) -> Response[
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
]:
    r"""Historical Measurements for Systems

     Lists aggregated measurements of a system over a period of time.

    System measurements are the result of incorporating measurements from
    all appliances that are part of a system. This allows computing e.g.
    overall consumption adding producers (e.g. PV) and subtracting consumers
    (e.g. EV charging stations). This aggregation is performed in various
    resolutions to suit different use cases. See the 'resolution' parameter
    for a list of options.

    Depending on the resolution parameter, the response contains either
    power or energy measurements (unless otherwise documented):
    - **power** (unit: W): `15m`, `1h`
    - **energy** (unit: Wh): `1d`, `1w`, `1M`, `1y`

    Measurements are \"aligned\" differently whether they contain energy or
    power measurements:
    - For power values the data point is written after the aggregated time
      span. For the interval 2018-04-01T00:00:00Z/2018-04-02T00:00:00Z
      with resolution 15m the first observation will be recorded at
      2018-04-01T00:15:00Z
    - For energy values the observation is stored at the beginning of
      the aggregated time span. For the interval
      2018-04-01T00:00:00Z/2018-04-05T00:00:00Z and resolution 1d the first
      observation will be recorded at 2018-04-01T00:00:00Z

    The `total` object of the response contains an aggregation of the
    individual data points over time and therefore is an energy value.
    The `total.measuredAt` field is an interval containing all data points
    in the requested interval.

    In order to reduce the duration of the endpoint, the gridX API imposes
    limitations on the interval for a given resolution:

    | Resolution | Limit                   |
    |------------|-------------------------|
    | 15m        | intervals up to 1 day   |
    | 1h         | intervals up to 1 week  |
    | 1d         | intervals up to 1 month |
    | 1w         | intervals up to 1 month |
    | 1M         | intervals up to 5 years |
    | 1y         | no limit                |

    Args:
        system_id (UUID):
        interval (str):
        resolution (GetSystemsSystemIDHistoricalResolution | Unset):  Default:
            GetSystemsSystemIDHistoricalResolution.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDHistoricalMeasurements | GetSystemsSystemIDHistoricalResponse403 | GetSystemsSystemIDHistoricalResponse404 | GetSystemsSystemIDHistoricalResponse422 | GetSystemsSystemIDHistoricalResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
        resolution=resolution,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: GetSystemsSystemIDHistoricalResolution | Unset = GetSystemsSystemIDHistoricalResolution.VALUE_1,
) -> (
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
    | None
):
    r"""Historical Measurements for Systems

     Lists aggregated measurements of a system over a period of time.

    System measurements are the result of incorporating measurements from
    all appliances that are part of a system. This allows computing e.g.
    overall consumption adding producers (e.g. PV) and subtracting consumers
    (e.g. EV charging stations). This aggregation is performed in various
    resolutions to suit different use cases. See the 'resolution' parameter
    for a list of options.

    Depending on the resolution parameter, the response contains either
    power or energy measurements (unless otherwise documented):
    - **power** (unit: W): `15m`, `1h`
    - **energy** (unit: Wh): `1d`, `1w`, `1M`, `1y`

    Measurements are \"aligned\" differently whether they contain energy or
    power measurements:
    - For power values the data point is written after the aggregated time
      span. For the interval 2018-04-01T00:00:00Z/2018-04-02T00:00:00Z
      with resolution 15m the first observation will be recorded at
      2018-04-01T00:15:00Z
    - For energy values the observation is stored at the beginning of
      the aggregated time span. For the interval
      2018-04-01T00:00:00Z/2018-04-05T00:00:00Z and resolution 1d the first
      observation will be recorded at 2018-04-01T00:00:00Z

    The `total` object of the response contains an aggregation of the
    individual data points over time and therefore is an energy value.
    The `total.measuredAt` field is an interval containing all data points
    in the requested interval.

    In order to reduce the duration of the endpoint, the gridX API imposes
    limitations on the interval for a given resolution:

    | Resolution | Limit                   |
    |------------|-------------------------|
    | 15m        | intervals up to 1 day   |
    | 1h         | intervals up to 1 week  |
    | 1d         | intervals up to 1 month |
    | 1w         | intervals up to 1 month |
    | 1M         | intervals up to 5 years |
    | 1y         | no limit                |

    Args:
        system_id (UUID):
        interval (str):
        resolution (GetSystemsSystemIDHistoricalResolution | Unset):  Default:
            GetSystemsSystemIDHistoricalResolution.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDHistoricalMeasurements | GetSystemsSystemIDHistoricalResponse403 | GetSystemsSystemIDHistoricalResponse404 | GetSystemsSystemIDHistoricalResponse422 | GetSystemsSystemIDHistoricalResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        interval=interval,
        resolution=resolution,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: GetSystemsSystemIDHistoricalResolution | Unset = GetSystemsSystemIDHistoricalResolution.VALUE_1,
) -> Response[
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
]:
    r"""Historical Measurements for Systems

     Lists aggregated measurements of a system over a period of time.

    System measurements are the result of incorporating measurements from
    all appliances that are part of a system. This allows computing e.g.
    overall consumption adding producers (e.g. PV) and subtracting consumers
    (e.g. EV charging stations). This aggregation is performed in various
    resolutions to suit different use cases. See the 'resolution' parameter
    for a list of options.

    Depending on the resolution parameter, the response contains either
    power or energy measurements (unless otherwise documented):
    - **power** (unit: W): `15m`, `1h`
    - **energy** (unit: Wh): `1d`, `1w`, `1M`, `1y`

    Measurements are \"aligned\" differently whether they contain energy or
    power measurements:
    - For power values the data point is written after the aggregated time
      span. For the interval 2018-04-01T00:00:00Z/2018-04-02T00:00:00Z
      with resolution 15m the first observation will be recorded at
      2018-04-01T00:15:00Z
    - For energy values the observation is stored at the beginning of
      the aggregated time span. For the interval
      2018-04-01T00:00:00Z/2018-04-05T00:00:00Z and resolution 1d the first
      observation will be recorded at 2018-04-01T00:00:00Z

    The `total` object of the response contains an aggregation of the
    individual data points over time and therefore is an energy value.
    The `total.measuredAt` field is an interval containing all data points
    in the requested interval.

    In order to reduce the duration of the endpoint, the gridX API imposes
    limitations on the interval for a given resolution:

    | Resolution | Limit                   |
    |------------|-------------------------|
    | 15m        | intervals up to 1 day   |
    | 1h         | intervals up to 1 week  |
    | 1d         | intervals up to 1 month |
    | 1w         | intervals up to 1 month |
    | 1M         | intervals up to 5 years |
    | 1y         | no limit                |

    Args:
        system_id (UUID):
        interval (str):
        resolution (GetSystemsSystemIDHistoricalResolution | Unset):  Default:
            GetSystemsSystemIDHistoricalResolution.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDHistoricalMeasurements | GetSystemsSystemIDHistoricalResponse403 | GetSystemsSystemIDHistoricalResponse404 | GetSystemsSystemIDHistoricalResponse422 | GetSystemsSystemIDHistoricalResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
        resolution=resolution,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: GetSystemsSystemIDHistoricalResolution | Unset = GetSystemsSystemIDHistoricalResolution.VALUE_1,
) -> (
    GetSystemsSystemIDHistoricalMeasurements
    | GetSystemsSystemIDHistoricalResponse403
    | GetSystemsSystemIDHistoricalResponse404
    | GetSystemsSystemIDHistoricalResponse422
    | GetSystemsSystemIDHistoricalResponse500
    | None
):
    r"""Historical Measurements for Systems

     Lists aggregated measurements of a system over a period of time.

    System measurements are the result of incorporating measurements from
    all appliances that are part of a system. This allows computing e.g.
    overall consumption adding producers (e.g. PV) and subtracting consumers
    (e.g. EV charging stations). This aggregation is performed in various
    resolutions to suit different use cases. See the 'resolution' parameter
    for a list of options.

    Depending on the resolution parameter, the response contains either
    power or energy measurements (unless otherwise documented):
    - **power** (unit: W): `15m`, `1h`
    - **energy** (unit: Wh): `1d`, `1w`, `1M`, `1y`

    Measurements are \"aligned\" differently whether they contain energy or
    power measurements:
    - For power values the data point is written after the aggregated time
      span. For the interval 2018-04-01T00:00:00Z/2018-04-02T00:00:00Z
      with resolution 15m the first observation will be recorded at
      2018-04-01T00:15:00Z
    - For energy values the observation is stored at the beginning of
      the aggregated time span. For the interval
      2018-04-01T00:00:00Z/2018-04-05T00:00:00Z and resolution 1d the first
      observation will be recorded at 2018-04-01T00:00:00Z

    The `total` object of the response contains an aggregation of the
    individual data points over time and therefore is an energy value.
    The `total.measuredAt` field is an interval containing all data points
    in the requested interval.

    In order to reduce the duration of the endpoint, the gridX API imposes
    limitations on the interval for a given resolution:

    | Resolution | Limit                   |
    |------------|-------------------------|
    | 15m        | intervals up to 1 day   |
    | 1h         | intervals up to 1 week  |
    | 1d         | intervals up to 1 month |
    | 1w         | intervals up to 1 month |
    | 1M         | intervals up to 5 years |
    | 1y         | no limit                |

    Args:
        system_id (UUID):
        interval (str):
        resolution (GetSystemsSystemIDHistoricalResolution | Unset):  Default:
            GetSystemsSystemIDHistoricalResolution.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDHistoricalMeasurements | GetSystemsSystemIDHistoricalResponse403 | GetSystemsSystemIDHistoricalResponse404 | GetSystemsSystemIDHistoricalResponse422 | GetSystemsSystemIDHistoricalResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
            resolution=resolution,
        )
    ).parsed
