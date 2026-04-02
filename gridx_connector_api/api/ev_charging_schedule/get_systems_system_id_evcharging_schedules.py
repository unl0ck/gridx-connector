from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_evcharging_schedules_response_200_item import (
    GetSystemsSystemIDEvchargingSchedulesResponse200Item,
)
from ...models.get_systems_system_id_evcharging_schedules_response_403 import (
    GetSystemsSystemIDEvchargingSchedulesResponse403,
)
from ...models.get_systems_system_id_evcharging_schedules_response_404 import (
    GetSystemsSystemIDEvchargingSchedulesResponse404,
)
from ...models.get_systems_system_id_evcharging_schedules_response_422 import (
    GetSystemsSystemIDEvchargingSchedulesResponse422,
)
from ...models.get_systems_system_id_evcharging_schedules_response_500 import (
    GetSystemsSystemIDEvchargingSchedulesResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/evcharging-schedules".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetSystemsSystemIDEvchargingSchedulesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDEvchargingSchedulesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDEvchargingSchedulesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDEvchargingSchedulesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDEvchargingSchedulesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
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
) -> Response[
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
]:
    """List a System's EV charging schedules.

     Lists EV charging schedules that belong to the specified system.

    It only contains the currently active schedules and schedules to be active in the
    next 24 hours.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvchargingSchedulesResponse403 | GetSystemsSystemIDEvchargingSchedulesResponse404 | GetSystemsSystemIDEvchargingSchedulesResponse422 | GetSystemsSystemIDEvchargingSchedulesResponse500 | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
    | None
):
    """List a System's EV charging schedules.

     Lists EV charging schedules that belong to the specified system.

    It only contains the currently active schedules and schedules to be active in the
    next 24 hours.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvchargingSchedulesResponse403 | GetSystemsSystemIDEvchargingSchedulesResponse404 | GetSystemsSystemIDEvchargingSchedulesResponse422 | GetSystemsSystemIDEvchargingSchedulesResponse500 | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
]:
    """List a System's EV charging schedules.

     Lists EV charging schedules that belong to the specified system.

    It only contains the currently active schedules and schedules to be active in the
    next 24 hours.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDEvchargingSchedulesResponse403 | GetSystemsSystemIDEvchargingSchedulesResponse404 | GetSystemsSystemIDEvchargingSchedulesResponse422 | GetSystemsSystemIDEvchargingSchedulesResponse500 | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetSystemsSystemIDEvchargingSchedulesResponse403
    | GetSystemsSystemIDEvchargingSchedulesResponse404
    | GetSystemsSystemIDEvchargingSchedulesResponse422
    | GetSystemsSystemIDEvchargingSchedulesResponse500
    | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
    | None
):
    """List a System's EV charging schedules.

     Lists EV charging schedules that belong to the specified system.

    It only contains the currently active schedules and schedules to be active in the
    next 24 hours.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDEvchargingSchedulesResponse403 | GetSystemsSystemIDEvchargingSchedulesResponse404 | GetSystemsSystemIDEvchargingSchedulesResponse422 | GetSystemsSystemIDEvchargingSchedulesResponse500 | list[GetSystemsSystemIDEvchargingSchedulesResponse200Item]
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
