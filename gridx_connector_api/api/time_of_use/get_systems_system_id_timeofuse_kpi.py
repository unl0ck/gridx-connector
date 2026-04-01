from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_kpi_response_200 import GetSystemsSystemIDTimeofuseKpiResponse200
from ...models.get_systems_system_id_timeofuse_kpi_response_400 import GetSystemsSystemIDTimeofuseKpiResponse400
from ...models.get_systems_system_id_timeofuse_kpi_response_404 import GetSystemsSystemIDTimeofuseKpiResponse404
from ...models.get_systems_system_id_timeofuse_kpi_response_422 import GetSystemsSystemIDTimeofuseKpiResponse422
from ...models.get_systems_system_id_timeofuse_kpi_response_500 import GetSystemsSystemIDTimeofuseKpiResponse500
from ...models.get_systems_system_id_timeofuse_kpi_response_502 import GetSystemsSystemIDTimeofuseKpiResponse502
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
        "url": "/systems/{system_id}/timeofuse/kpi".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseKpiResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSystemsSystemIDTimeofuseKpiResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseKpiResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDTimeofuseKpiResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseKpiResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseKpiResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
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
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
]:
    """Get the historical KPIs of the Time-of-Use service.

     Provides Key Performance Indicators (KPIs) for system cost analysis under Time-of-Use (ToU) and
    Self-Sufficiency Optimization (SSO) models. Returns interval-based ToU and SSO costs to evaluate
    potential savings between the two scenarios.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseKpiResponse200 | GetSystemsSystemIDTimeofuseKpiResponse400 | GetSystemsSystemIDTimeofuseKpiResponse404 | GetSystemsSystemIDTimeofuseKpiResponse422 | GetSystemsSystemIDTimeofuseKpiResponse500 | GetSystemsSystemIDTimeofuseKpiResponse502]
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
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
    | None
):
    """Get the historical KPIs of the Time-of-Use service.

     Provides Key Performance Indicators (KPIs) for system cost analysis under Time-of-Use (ToU) and
    Self-Sufficiency Optimization (SSO) models. Returns interval-based ToU and SSO costs to evaluate
    potential savings between the two scenarios.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseKpiResponse200 | GetSystemsSystemIDTimeofuseKpiResponse400 | GetSystemsSystemIDTimeofuseKpiResponse404 | GetSystemsSystemIDTimeofuseKpiResponse422 | GetSystemsSystemIDTimeofuseKpiResponse500 | GetSystemsSystemIDTimeofuseKpiResponse502
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
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
]:
    """Get the historical KPIs of the Time-of-Use service.

     Provides Key Performance Indicators (KPIs) for system cost analysis under Time-of-Use (ToU) and
    Self-Sufficiency Optimization (SSO) models. Returns interval-based ToU and SSO costs to evaluate
    potential savings between the two scenarios.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseKpiResponse200 | GetSystemsSystemIDTimeofuseKpiResponse400 | GetSystemsSystemIDTimeofuseKpiResponse404 | GetSystemsSystemIDTimeofuseKpiResponse422 | GetSystemsSystemIDTimeofuseKpiResponse500 | GetSystemsSystemIDTimeofuseKpiResponse502]
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
    GetSystemsSystemIDTimeofuseKpiResponse200
    | GetSystemsSystemIDTimeofuseKpiResponse400
    | GetSystemsSystemIDTimeofuseKpiResponse404
    | GetSystemsSystemIDTimeofuseKpiResponse422
    | GetSystemsSystemIDTimeofuseKpiResponse500
    | GetSystemsSystemIDTimeofuseKpiResponse502
    | None
):
    """Get the historical KPIs of the Time-of-Use service.

     Provides Key Performance Indicators (KPIs) for system cost analysis under Time-of-Use (ToU) and
    Self-Sufficiency Optimization (SSO) models. Returns interval-based ToU and SSO costs to evaluate
    potential savings between the two scenarios.

    Args:
        system_id (UUID):
        interval (str | Unset):  Example: 2018-04-01T15:00:00Z/2018-04-25T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseKpiResponse200 | GetSystemsSystemIDTimeofuseKpiResponse400 | GetSystemsSystemIDTimeofuseKpiResponse404 | GetSystemsSystemIDTimeofuseKpiResponse422 | GetSystemsSystemIDTimeofuseKpiResponse500 | GetSystemsSystemIDTimeofuseKpiResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
        )
    ).parsed
