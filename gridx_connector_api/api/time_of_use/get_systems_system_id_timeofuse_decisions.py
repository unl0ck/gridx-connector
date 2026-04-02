from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_decisions_response_200 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse200,
)
from ...models.get_systems_system_id_timeofuse_decisions_response_400 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse400,
)
from ...models.get_systems_system_id_timeofuse_decisions_response_403 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse403,
)
from ...models.get_systems_system_id_timeofuse_decisions_response_404 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse404,
)
from ...models.get_systems_system_id_timeofuse_decisions_response_500 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse500,
)
from ...models.get_systems_system_id_timeofuse_decisions_response_502 import (
    GetSystemsSystemIDTimeofuseDecisionsResponse502,
)
from ...types import UNSET, Response


def _get_kwargs(
    system_id: UUID,
    *,
    interval: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/timeofuse/decisions".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseDecisionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSystemsSystemIDTimeofuseDecisionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDTimeofuseDecisionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseDecisionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseDecisionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseDecisionsResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
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
) -> Response[
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
]:
    """Get time of use optimization decisions of a system.

     Get optimization decisions and associated metrics for a system with `system_id`,
    within given time interval. Note that decisions may not always cover the complete time interval.
    Only decisions with `start_at` in the past are returned.
    The maximum time interval that can be requested is 48 hours.

    Args:
        system_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseDecisionsResponse200 | GetSystemsSystemIDTimeofuseDecisionsResponse400 | GetSystemsSystemIDTimeofuseDecisionsResponse403 | GetSystemsSystemIDTimeofuseDecisionsResponse404 | GetSystemsSystemIDTimeofuseDecisionsResponse500 | GetSystemsSystemIDTimeofuseDecisionsResponse502]
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
    interval: str,
) -> (
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
    | None
):
    """Get time of use optimization decisions of a system.

     Get optimization decisions and associated metrics for a system with `system_id`,
    within given time interval. Note that decisions may not always cover the complete time interval.
    Only decisions with `start_at` in the past are returned.
    The maximum time interval that can be requested is 48 hours.

    Args:
        system_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseDecisionsResponse200 | GetSystemsSystemIDTimeofuseDecisionsResponse400 | GetSystemsSystemIDTimeofuseDecisionsResponse403 | GetSystemsSystemIDTimeofuseDecisionsResponse404 | GetSystemsSystemIDTimeofuseDecisionsResponse500 | GetSystemsSystemIDTimeofuseDecisionsResponse502
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
    interval: str,
) -> Response[
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
]:
    """Get time of use optimization decisions of a system.

     Get optimization decisions and associated metrics for a system with `system_id`,
    within given time interval. Note that decisions may not always cover the complete time interval.
    Only decisions with `start_at` in the past are returned.
    The maximum time interval that can be requested is 48 hours.

    Args:
        system_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTimeofuseDecisionsResponse200 | GetSystemsSystemIDTimeofuseDecisionsResponse400 | GetSystemsSystemIDTimeofuseDecisionsResponse403 | GetSystemsSystemIDTimeofuseDecisionsResponse404 | GetSystemsSystemIDTimeofuseDecisionsResponse500 | GetSystemsSystemIDTimeofuseDecisionsResponse502]
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
    interval: str,
) -> (
    GetSystemsSystemIDTimeofuseDecisionsResponse200
    | GetSystemsSystemIDTimeofuseDecisionsResponse400
    | GetSystemsSystemIDTimeofuseDecisionsResponse403
    | GetSystemsSystemIDTimeofuseDecisionsResponse404
    | GetSystemsSystemIDTimeofuseDecisionsResponse500
    | GetSystemsSystemIDTimeofuseDecisionsResponse502
    | None
):
    """Get time of use optimization decisions of a system.

     Get optimization decisions and associated metrics for a system with `system_id`,
    within given time interval. Note that decisions may not always cover the complete time interval.
    Only decisions with `start_at` in the past are returned.
    The maximum time interval that can be requested is 48 hours.

    Args:
        system_id (UUID):
        interval (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTimeofuseDecisionsResponse200 | GetSystemsSystemIDTimeofuseDecisionsResponse400 | GetSystemsSystemIDTimeofuseDecisionsResponse403 | GetSystemsSystemIDTimeofuseDecisionsResponse404 | GetSystemsSystemIDTimeofuseDecisionsResponse500 | GetSystemsSystemIDTimeofuseDecisionsResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
        )
    ).parsed
