from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_timeofuse_settings_response_200 import (
    GetSystemsSystemIDTimeofuseSettingsResponse200,
)
from ...models.get_systems_system_id_timeofuse_settings_response_403 import (
    GetSystemsSystemIDTimeofuseSettingsResponse403,
)
from ...models.get_systems_system_id_timeofuse_settings_response_404 import (
    GetSystemsSystemIDTimeofuseSettingsResponse404,
)
from ...models.get_systems_system_id_timeofuse_settings_response_500 import (
    GetSystemsSystemIDTimeofuseSettingsResponse500,
)
from ...models.get_systems_system_id_timeofuse_settings_response_502 import (
    GetSystemsSystemIDTimeofuseSettingsResponse502,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/timeofuse/settings".format(
            system_id=quote(str(system_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTimeofuseSettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDTimeofuseSettingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTimeofuseSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTimeofuseSettingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetSystemsSystemIDTimeofuseSettingsResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
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
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
]:
    """Get time of use optimization settings of a system.

     Get time of use optimization settings of a system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemsSystemIDTimeofuseSettingsResponse200 | GetSystemsSystemIDTimeofuseSettingsResponse403 | GetSystemsSystemIDTimeofuseSettingsResponse404 | GetSystemsSystemIDTimeofuseSettingsResponse500 | GetSystemsSystemIDTimeofuseSettingsResponse502]
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
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    """Get time of use optimization settings of a system.

     Get time of use optimization settings of a system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemsSystemIDTimeofuseSettingsResponse200 | GetSystemsSystemIDTimeofuseSettingsResponse403 | GetSystemsSystemIDTimeofuseSettingsResponse404 | GetSystemsSystemIDTimeofuseSettingsResponse500 | GetSystemsSystemIDTimeofuseSettingsResponse502
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
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
]:
    """Get time of use optimization settings of a system.

     Get time of use optimization settings of a system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemsSystemIDTimeofuseSettingsResponse200 | GetSystemsSystemIDTimeofuseSettingsResponse403 | GetSystemsSystemIDTimeofuseSettingsResponse404 | GetSystemsSystemIDTimeofuseSettingsResponse500 | GetSystemsSystemIDTimeofuseSettingsResponse502]
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
    Any
    | GetSystemsSystemIDTimeofuseSettingsResponse200
    | GetSystemsSystemIDTimeofuseSettingsResponse403
    | GetSystemsSystemIDTimeofuseSettingsResponse404
    | GetSystemsSystemIDTimeofuseSettingsResponse500
    | GetSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    """Get time of use optimization settings of a system.

     Get time of use optimization settings of a system.

    Args:
        system_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemsSystemIDTimeofuseSettingsResponse200 | GetSystemsSystemIDTimeofuseSettingsResponse403 | GetSystemsSystemIDTimeofuseSettingsResponse404 | GetSystemsSystemIDTimeofuseSettingsResponse500 | GetSystemsSystemIDTimeofuseSettingsResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
        )
    ).parsed
