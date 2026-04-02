from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_status_current_response_200 import (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200,
)
from ...models.get_systems_system_id_timeofuse_status_current_response_404 import (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse404,
)
from ...models.get_systems_system_id_timeofuse_status_current_response_422 import (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse422,
)
from ...models.get_systems_system_id_timeofuse_status_current_response_500 import (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse500,
)
from ...models.get_systems_system_id_timeofuse_status_current_response_502 import (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse502,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/timeofuse/status/current".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseStatusCurrentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseStatusCurrentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSystemsSystemIDTimeofuseStatusCurrentResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseStatusCurrentResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseStatusCurrentResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
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
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
]:
    """Get the last known status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status for
    associated with a system with `systemID`.

    This endpoint provides the last known, or current, status of the Time-of-Use runs.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseStatusCurrentResponse200 | GetSystemsSystemIDTimeofuseStatusCurrentResponse404 | GetSystemsSystemIDTimeofuseStatusCurrentResponse422 | GetSystemsSystemIDTimeofuseStatusCurrentResponse500 | GetSystemsSystemIDTimeofuseStatusCurrentResponse502]
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
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
    | None
):
    """Get the last known status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status for
    associated with a system with `systemID`.

    This endpoint provides the last known, or current, status of the Time-of-Use runs.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseStatusCurrentResponse200 | GetSystemsSystemIDTimeofuseStatusCurrentResponse404 | GetSystemsSystemIDTimeofuseStatusCurrentResponse422 | GetSystemsSystemIDTimeofuseStatusCurrentResponse500 | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
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
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
]:
    """Get the last known status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status for
    associated with a system with `systemID`.

    This endpoint provides the last known, or current, status of the Time-of-Use runs.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseStatusCurrentResponse200 | GetSystemsSystemIDTimeofuseStatusCurrentResponse404 | GetSystemsSystemIDTimeofuseStatusCurrentResponse422 | GetSystemsSystemIDTimeofuseStatusCurrentResponse500 | GetSystemsSystemIDTimeofuseStatusCurrentResponse502]
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
    GetSystemsSystemIDTimeofuseStatusCurrentResponse200
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse404
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse422
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse500
    | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
    | None
):
    """Get the last known status of the Time-of-Use service.

     The Time-of-Use (ToU) optimization runs on a given resolution of 15 minutes.
    For each time segment, i.e. `[10:00, 10:15]` it publishes an operational status for
    associated with a system with `systemID`.

    This endpoint provides the last known, or current, status of the Time-of-Use runs.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseStatusCurrentResponse200 | GetSystemsSystemIDTimeofuseStatusCurrentResponse404 | GetSystemsSystemIDTimeofuseStatusCurrentResponse422 | GetSystemsSystemIDTimeofuseStatusCurrentResponse500 | GetSystemsSystemIDTimeofuseStatusCurrentResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
