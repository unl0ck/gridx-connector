from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_power_limit_schedules_schedule_id_response_200 import (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200,
)
from ...models.get_systems_system_id_power_limit_schedules_schedule_id_response_403 import (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403,
)
from ...models.get_systems_system_id_power_limit_schedules_schedule_id_response_404 import (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404,
)
from ...models.get_systems_system_id_power_limit_schedules_schedule_id_response_500 import (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    schedule_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/power-limit-schedules/{schedule_id}".format(
            system_id=quote(str(system_id), safe=""),
            schedule_id=quote(str(schedule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
]:
    """Retrieve a power limit schedule

     Retrieves the details of an existing power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        schedule_id=schedule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    """Retrieve a power limit schedule

     Retrieves the details of an existing power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    """

    return sync_detailed(
        system_id=system_id,
        schedule_id=schedule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
]:
    """Retrieve a power limit schedule

     Retrieves the details of an existing power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        schedule_id=schedule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    """Retrieve a power limit schedule

     Retrieves the details of an existing power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            schedule_id=schedule_id,
            client=client,
        )
    ).parsed
