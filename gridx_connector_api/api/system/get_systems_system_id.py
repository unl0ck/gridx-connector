from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_include_item import GetSystemsSystemIDIncludeItem
from ...models.get_systems_system_id_response_403 import GetSystemsSystemIDResponse403
from ...models.get_systems_system_id_response_404 import GetSystemsSystemIDResponse404
from ...models.get_systems_system_id_response_500 import GetSystemsSystemIDResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_id: UUID,
    *,
    include: list[GetSystemsSystemIDIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500 | None:
    if response.status_code == 403:
        response_403 = GetSystemsSystemIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500]:
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
    include: list[GetSystemsSystemIDIncludeItem] | Unset = UNSET,
) -> Response[GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500]:
    """Retrieve a System

     Retrieves the details of an existing system.

    Args:
        system_id (UUID):
        include (list[GetSystemsSystemIDIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    include: list[GetSystemsSystemIDIncludeItem] | Unset = UNSET,
) -> GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500 | None:
    """Retrieve a System

     Retrieves the details of an existing system.

    Args:
        system_id (UUID):
        include (list[GetSystemsSystemIDIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    include: list[GetSystemsSystemIDIncludeItem] | Unset = UNSET,
) -> Response[GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500]:
    """Retrieve a System

     Retrieves the details of an existing system.

    Args:
        system_id (UUID):
        include (list[GetSystemsSystemIDIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    include: list[GetSystemsSystemIDIncludeItem] | Unset = UNSET,
) -> GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500 | None:
    """Retrieve a System

     Retrieves the details of an existing system.

    Args:
        system_id (UUID):
        include (list[GetSystemsSystemIDIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDResponse403 | GetSystemsSystemIDResponse404 | GetSystemsSystemIDResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            include=include,
        )
    ).parsed
