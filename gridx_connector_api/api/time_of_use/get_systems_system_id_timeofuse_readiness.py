from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_readiness_response_200 import (
    GetSystemsSystemIDTimeofuseReadinessResponse200,
)
from ...models.get_systems_system_id_timeofuse_readiness_response_403 import (
    GetSystemsSystemIDTimeofuseReadinessResponse403,
)
from ...models.get_systems_system_id_timeofuse_readiness_response_404 import (
    GetSystemsSystemIDTimeofuseReadinessResponse404,
)
from ...models.get_systems_system_id_timeofuse_readiness_response_500 import (
    GetSystemsSystemIDTimeofuseReadinessResponse500,
)
from ...models.get_systems_system_id_timeofuse_readiness_response_502 import (
    GetSystemsSystemIDTimeofuseReadinessResponse502,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/timeofuse/readiness".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseReadinessResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDTimeofuseReadinessResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseReadinessResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseReadinessResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseReadinessResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
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
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
]:
    r"""Evaluate whether the system is ready for enabling Time-of-Use.

     A series of operational prerequisites are required before enabling Time-of-Use (ToU) for a system.
    The checks are done in order to evaluate the system's \"readiness\" for ToU.
    In principal, checks pertaining to appliances used, price data used, as well as some system metadata
    are performed.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseReadinessResponse200 | GetSystemsSystemIDTimeofuseReadinessResponse403 | GetSystemsSystemIDTimeofuseReadinessResponse404 | GetSystemsSystemIDTimeofuseReadinessResponse500 | GetSystemsSystemIDTimeofuseReadinessResponse502]
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
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
    | None
):
    r"""Evaluate whether the system is ready for enabling Time-of-Use.

     A series of operational prerequisites are required before enabling Time-of-Use (ToU) for a system.
    The checks are done in order to evaluate the system's \"readiness\" for ToU.
    In principal, checks pertaining to appliances used, price data used, as well as some system metadata
    are performed.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseReadinessResponse200 | GetSystemsSystemIDTimeofuseReadinessResponse403 | GetSystemsSystemIDTimeofuseReadinessResponse404 | GetSystemsSystemIDTimeofuseReadinessResponse500 | GetSystemsSystemIDTimeofuseReadinessResponse502
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
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
]:
    r"""Evaluate whether the system is ready for enabling Time-of-Use.

     A series of operational prerequisites are required before enabling Time-of-Use (ToU) for a system.
    The checks are done in order to evaluate the system's \"readiness\" for ToU.
    In principal, checks pertaining to appliances used, price data used, as well as some system metadata
    are performed.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseReadinessResponse200 | GetSystemsSystemIDTimeofuseReadinessResponse403 | GetSystemsSystemIDTimeofuseReadinessResponse404 | GetSystemsSystemIDTimeofuseReadinessResponse500 | GetSystemsSystemIDTimeofuseReadinessResponse502]
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
    GetSystemsSystemIDTimeofuseReadinessResponse200
    | GetSystemsSystemIDTimeofuseReadinessResponse403
    | GetSystemsSystemIDTimeofuseReadinessResponse404
    | GetSystemsSystemIDTimeofuseReadinessResponse500
    | GetSystemsSystemIDTimeofuseReadinessResponse502
    | None
):
    r"""Evaluate whether the system is ready for enabling Time-of-Use.

     A series of operational prerequisites are required before enabling Time-of-Use (ToU) for a system.
    The checks are done in order to evaluate the system's \"readiness\" for ToU.
    In principal, checks pertaining to appliances used, price data used, as well as some system metadata
    are performed.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseReadinessResponse200 | GetSystemsSystemIDTimeofuseReadinessResponse403 | GetSystemsSystemIDTimeofuseReadinessResponse404 | GetSystemsSystemIDTimeofuseReadinessResponse500 | GetSystemsSystemIDTimeofuseReadinessResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
