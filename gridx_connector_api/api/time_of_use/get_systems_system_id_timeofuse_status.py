from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_status_response_200 import GetSystemsSystemIDTimeofuseStatusResponse200
from ...models.get_systems_system_id_timeofuse_status_response_400 import GetSystemsSystemIDTimeofuseStatusResponse400
from ...models.get_systems_system_id_timeofuse_status_response_404 import GetSystemsSystemIDTimeofuseStatusResponse404
from ...models.get_systems_system_id_timeofuse_status_response_422 import GetSystemsSystemIDTimeofuseStatusResponse422
from ...models.get_systems_system_id_timeofuse_status_response_500 import GetSystemsSystemIDTimeofuseStatusResponse500
from ...models.get_systems_system_id_timeofuse_status_response_502 import GetSystemsSystemIDTimeofuseStatusResponse502
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
        "url": "/systems/{system_id}/timeofuse/status".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSystemsSystemIDTimeofuseStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseStatusResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDTimeofuseStatusResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseStatusResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseStatusResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
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
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
]:
    """Get the historical status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status
    associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the status data are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[now - 48h, now]`.
    The maximum size of this interval is 48h.
    Please note that the statuses might not cover the whole time window.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseStatusResponse200 | GetSystemsSystemIDTimeofuseStatusResponse400 | GetSystemsSystemIDTimeofuseStatusResponse404 | GetSystemsSystemIDTimeofuseStatusResponse422 | GetSystemsSystemIDTimeofuseStatusResponse500 | GetSystemsSystemIDTimeofuseStatusResponse502]
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
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
    | None
):
    """Get the historical status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status
    associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the status data are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[now - 48h, now]`.
    The maximum size of this interval is 48h.
    Please note that the statuses might not cover the whole time window.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseStatusResponse200 | GetSystemsSystemIDTimeofuseStatusResponse400 | GetSystemsSystemIDTimeofuseStatusResponse404 | GetSystemsSystemIDTimeofuseStatusResponse422 | GetSystemsSystemIDTimeofuseStatusResponse500 | GetSystemsSystemIDTimeofuseStatusResponse502
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
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
]:
    """Get the historical status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status
    associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the status data are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[now - 48h, now]`.
    The maximum size of this interval is 48h.
    Please note that the statuses might not cover the whole time window.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseStatusResponse200 | GetSystemsSystemIDTimeofuseStatusResponse400 | GetSystemsSystemIDTimeofuseStatusResponse404 | GetSystemsSystemIDTimeofuseStatusResponse422 | GetSystemsSystemIDTimeofuseStatusResponse500 | GetSystemsSystemIDTimeofuseStatusResponse502]
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
    GetSystemsSystemIDTimeofuseStatusResponse200
    | GetSystemsSystemIDTimeofuseStatusResponse400
    | GetSystemsSystemIDTimeofuseStatusResponse404
    | GetSystemsSystemIDTimeofuseStatusResponse422
    | GetSystemsSystemIDTimeofuseStatusResponse500
    | GetSystemsSystemIDTimeofuseStatusResponse502
    | None
):
    """Get the historical status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status
    associated with a system with `systemID`.

    This endpoint requires to specify a time window called `interval` for which the status data are
    returned.
    For example `[2021-01-01T02:07:14Z, 2021-01-02T02:07:14Z]`.
    If no interval is provided it is assumed to be `[now - 48h, now]`.
    The maximum size of this interval is 48h.
    Please note that the statuses might not cover the whole time window.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseStatusResponse200 | GetSystemsSystemIDTimeofuseStatusResponse400 | GetSystemsSystemIDTimeofuseStatusResponse404 | GetSystemsSystemIDTimeofuseStatusResponse422 | GetSystemsSystemIDTimeofuseStatusResponse500 | GetSystemsSystemIDTimeofuseStatusResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
        )
    ).parsed
