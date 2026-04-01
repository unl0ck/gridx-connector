from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_body import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
)
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_response_200 import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200,
)
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_response_400 import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400,
)
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_response_403 import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403,
)
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_response_404 import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404,
)
from ...models.patch_systems_system_id_power_limit_schedules_schedule_id_response_500 import (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    schedule_id: UUID,
    *,
    body: PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}/power-limit-schedules/{schedule_id}".format(
            system_id=quote(str(system_id), safe=""),
            schedule_id=quote(str(schedule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
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
    body: PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
) -> Response[
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
]:
    """Update a power limit schedule

     Updates the specified power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):
        body (PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        schedule_id=schedule_id,
        body=body,
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
    body: PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
) -> (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    """Update a power limit schedule

     Updates the specified power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):
        body (PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    """

    return sync_detailed(
        system_id=system_id,
        schedule_id=schedule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
) -> Response[
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
]:
    """Update a power limit schedule

     Updates the specified power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):
        body (PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        schedule_id=schedule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    schedule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody,
) -> (
    PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404
    | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    | None
):
    """Update a power limit schedule

     Updates the specified power limit schedule.

    Args:
        system_id (UUID):
        schedule_id (UUID):
        body (PatchSystemsSystemIDPowerLimitSchedulesScheduleIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse400 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse403 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse404 | PatchSystemsSystemIDPowerLimitSchedulesScheduleIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            schedule_id=schedule_id,
            client=client,
            body=body,
        )
    ).parsed
