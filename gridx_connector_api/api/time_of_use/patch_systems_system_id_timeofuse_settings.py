from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_systems_system_id_timeofuse_settings_body import PatchSystemsSystemIDTimeofuseSettingsBody
from ...models.patch_systems_system_id_timeofuse_settings_response_200 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse200,
)
from ...models.patch_systems_system_id_timeofuse_settings_response_400 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse400,
)
from ...models.patch_systems_system_id_timeofuse_settings_response_403 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse403,
)
from ...models.patch_systems_system_id_timeofuse_settings_response_404 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse404,
)
from ...models.patch_systems_system_id_timeofuse_settings_response_500 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse500,
)
from ...models.patch_systems_system_id_timeofuse_settings_response_502 import (
    PatchSystemsSystemIDTimeofuseSettingsResponse502,
)
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PatchSystemsSystemIDTimeofuseSettingsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}/timeofuse/settings".format(
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
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    if response.status_code == 200:
        response_200 = PatchSystemsSystemIDTimeofuseSettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchSystemsSystemIDTimeofuseSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchSystemsSystemIDTimeofuseSettingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemsSystemIDTimeofuseSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PatchSystemsSystemIDTimeofuseSettingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = PatchSystemsSystemIDTimeofuseSettingsResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
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
    body: PatchSystemsSystemIDTimeofuseSettingsBody,
) -> Response[
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
]:
    """Update time of use optimization settings for a system.

     Update time of use optimization settings for a system.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTimeofuseSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDTimeofuseSettingsResponse200 | PatchSystemsSystemIDTimeofuseSettingsResponse400 | PatchSystemsSystemIDTimeofuseSettingsResponse403 | PatchSystemsSystemIDTimeofuseSettingsResponse404 | PatchSystemsSystemIDTimeofuseSettingsResponse500 | PatchSystemsSystemIDTimeofuseSettingsResponse502]
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
    body: PatchSystemsSystemIDTimeofuseSettingsBody,
) -> (
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    """Update time of use optimization settings for a system.

     Update time of use optimization settings for a system.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTimeofuseSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDTimeofuseSettingsResponse200 | PatchSystemsSystemIDTimeofuseSettingsResponse400 | PatchSystemsSystemIDTimeofuseSettingsResponse403 | PatchSystemsSystemIDTimeofuseSettingsResponse404 | PatchSystemsSystemIDTimeofuseSettingsResponse500 | PatchSystemsSystemIDTimeofuseSettingsResponse502
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
    body: PatchSystemsSystemIDTimeofuseSettingsBody,
) -> Response[
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
]:
    """Update time of use optimization settings for a system.

     Update time of use optimization settings for a system.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTimeofuseSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDTimeofuseSettingsResponse200 | PatchSystemsSystemIDTimeofuseSettingsResponse400 | PatchSystemsSystemIDTimeofuseSettingsResponse403 | PatchSystemsSystemIDTimeofuseSettingsResponse404 | PatchSystemsSystemIDTimeofuseSettingsResponse500 | PatchSystemsSystemIDTimeofuseSettingsResponse502]
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
    body: PatchSystemsSystemIDTimeofuseSettingsBody,
) -> (
    PatchSystemsSystemIDTimeofuseSettingsResponse200
    | PatchSystemsSystemIDTimeofuseSettingsResponse400
    | PatchSystemsSystemIDTimeofuseSettingsResponse403
    | PatchSystemsSystemIDTimeofuseSettingsResponse404
    | PatchSystemsSystemIDTimeofuseSettingsResponse500
    | PatchSystemsSystemIDTimeofuseSettingsResponse502
    | None
):
    """Update time of use optimization settings for a system.

     Update time of use optimization settings for a system.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTimeofuseSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDTimeofuseSettingsResponse200 | PatchSystemsSystemIDTimeofuseSettingsResponse400 | PatchSystemsSystemIDTimeofuseSettingsResponse403 | PatchSystemsSystemIDTimeofuseSettingsResponse404 | PatchSystemsSystemIDTimeofuseSettingsResponse500 | PatchSystemsSystemIDTimeofuseSettingsResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
