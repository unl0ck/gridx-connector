from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_system_id_evcharging_schedules_body import PostSystemsSystemIDEvchargingSchedulesBody
from ...models.post_systems_system_id_evcharging_schedules_ev_charging_schedule import (
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule,
)
from ...models.post_systems_system_id_evcharging_schedules_response_400 import (
    PostSystemsSystemIDEvchargingSchedulesResponse400,
)
from ...models.post_systems_system_id_evcharging_schedules_response_403 import (
    PostSystemsSystemIDEvchargingSchedulesResponse403,
)
from ...models.post_systems_system_id_evcharging_schedules_response_404 import (
    PostSystemsSystemIDEvchargingSchedulesResponse404,
)
from ...models.post_systems_system_id_evcharging_schedules_response_422 import (
    PostSystemsSystemIDEvchargingSchedulesResponse422,
)
from ...models.post_systems_system_id_evcharging_schedules_response_500 import (
    PostSystemsSystemIDEvchargingSchedulesResponse500,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PostSystemsSystemIDEvchargingSchedulesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systems/{system_id}/evcharging-schedules".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostSystemsSystemIDEvchargingSchedulesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PostSystemsSystemIDEvchargingSchedulesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemsSystemIDEvchargingSchedulesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostSystemsSystemIDEvchargingSchedulesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostSystemsSystemIDEvchargingSchedulesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
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
    body: PostSystemsSystemIDEvchargingSchedulesBody,
) -> Response[
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
]:
    """Create an EV charging schedule

     Creates a system's EV charging schedule.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvchargingSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule | PostSystemsSystemIDEvchargingSchedulesResponse400 | PostSystemsSystemIDEvchargingSchedulesResponse403 | PostSystemsSystemIDEvchargingSchedulesResponse404 | PostSystemsSystemIDEvchargingSchedulesResponse422 | PostSystemsSystemIDEvchargingSchedulesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvchargingSchedulesBody,
) -> (
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
    | None
):
    """Create an EV charging schedule

     Creates a system's EV charging schedule.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvchargingSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule | PostSystemsSystemIDEvchargingSchedulesResponse400 | PostSystemsSystemIDEvchargingSchedulesResponse403 | PostSystemsSystemIDEvchargingSchedulesResponse404 | PostSystemsSystemIDEvchargingSchedulesResponse422 | PostSystemsSystemIDEvchargingSchedulesResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvchargingSchedulesBody,
) -> Response[
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
]:
    """Create an EV charging schedule

     Creates a system's EV charging schedule.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvchargingSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule | PostSystemsSystemIDEvchargingSchedulesResponse400 | PostSystemsSystemIDEvchargingSchedulesResponse403 | PostSystemsSystemIDEvchargingSchedulesResponse404 | PostSystemsSystemIDEvchargingSchedulesResponse422 | PostSystemsSystemIDEvchargingSchedulesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostSystemsSystemIDEvchargingSchedulesBody,
) -> (
    PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule
    | PostSystemsSystemIDEvchargingSchedulesResponse400
    | PostSystemsSystemIDEvchargingSchedulesResponse403
    | PostSystemsSystemIDEvchargingSchedulesResponse404
    | PostSystemsSystemIDEvchargingSchedulesResponse422
    | PostSystemsSystemIDEvchargingSchedulesResponse500
    | None
):
    """Create an EV charging schedule

     Creates a system's EV charging schedule.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDEvchargingSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule | PostSystemsSystemIDEvchargingSchedulesResponse400 | PostSystemsSystemIDEvchargingSchedulesResponse403 | PostSystemsSystemIDEvchargingSchedulesResponse404 | PostSystemsSystemIDEvchargingSchedulesResponse422 | PostSystemsSystemIDEvchargingSchedulesResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
