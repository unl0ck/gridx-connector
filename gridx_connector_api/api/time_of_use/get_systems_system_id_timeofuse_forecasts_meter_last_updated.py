from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_200 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200,
)
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_400 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400,
)
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_404 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404,
)
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_422 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422,
)
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_500 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500,
)
from ...models.get_systems_system_id_timeofuse_forecasts_meter_last_updated_response_502 import (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_id: UUID,
    *,
    interval: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/timeofuse/forecasts/meter/last-updated".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
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
    interval: str | Unset = UNSET,
) -> Response[
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
]:
    """Get the last updated timestamp for the Time-of-Use forecasts for the grid connection point.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes a series of forecasts for
    the grid connection point associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the forecasts are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[00:00:00 today, 00:00:00 in two days]`.
    The maximum size of this interval is 48h.

    This endpoint returns the last timestamp RFC3339 format when the forecasts **in the selected time
    window**
    were updated.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str | Unset = UNSET,
) -> (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
    | None
):
    """Get the last updated timestamp for the Time-of-Use forecasts for the grid connection point.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes a series of forecasts for
    the grid connection point associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the forecasts are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[00:00:00 today, 00:00:00 in two days]`.
    The maximum size of this interval is 48h.

    This endpoint returns the last timestamp RFC3339 format when the forecasts **in the selected time
    window**
    were updated.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str | Unset = UNSET,
) -> Response[
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
]:
    """Get the last updated timestamp for the Time-of-Use forecasts for the grid connection point.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes a series of forecasts for
    the grid connection point associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the forecasts are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[00:00:00 today, 00:00:00 in two days]`.
    The maximum size of this interval is 48h.

    This endpoint returns the last timestamp RFC3339 format when the forecasts **in the selected time
    window**
    were updated.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str | Unset = UNSET,
) -> (
    GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500
    | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
    | None
):
    """Get the last updated timestamp for the Time-of-Use forecasts for the grid connection point.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes a series of forecasts for
    the grid connection point associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the forecasts are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[00:00:00 today, 00:00:00 in two days]`.
    The maximum size of this interval is 48h.

    This endpoint returns the last timestamp RFC3339 format when the forecasts **in the selected time
    window**
    were updated.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse200 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse400 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse404 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse422 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse500 | GetSystemsSystemIDTimeofuseForecastsMeterLastUpdatedResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
        )
    ).parsed
