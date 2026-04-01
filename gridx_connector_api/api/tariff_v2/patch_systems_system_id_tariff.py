from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_systems_system_id_tariff_body import PatchSystemsSystemIDTariffBody
from ...models.patch_systems_system_id_tariff_response_400 import PatchSystemsSystemIDTariffResponse400
from ...models.patch_systems_system_id_tariff_response_403 import PatchSystemsSystemIDTariffResponse403
from ...models.patch_systems_system_id_tariff_response_404 import PatchSystemsSystemIDTariffResponse404
from ...models.patch_systems_system_id_tariff_response_422 import PatchSystemsSystemIDTariffResponse422
from ...models.patch_systems_system_id_tariff_response_500 import PatchSystemsSystemIDTariffResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PatchSystemsSystemIDTariffBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/systems/{system_id}/tariff".format(
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
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemsSystemIDTariffResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchSystemsSystemIDTariffResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemsSystemIDTariffResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchSystemsSystemIDTariffResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchSystemsSystemIDTariffResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
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
    body: PatchSystemsSystemIDTariffBody,
) -> Response[
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
]:
    """Update the tariff v2 of a system

     Updates the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDTariffResponse400 | PatchSystemsSystemIDTariffResponse403 | PatchSystemsSystemIDTariffResponse404 | PatchSystemsSystemIDTariffResponse422 | PatchSystemsSystemIDTariffResponse500]
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
    body: PatchSystemsSystemIDTariffBody,
) -> (
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
    | None
):
    """Update the tariff v2 of a system

     Updates the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDTariffResponse400 | PatchSystemsSystemIDTariffResponse403 | PatchSystemsSystemIDTariffResponse404 | PatchSystemsSystemIDTariffResponse422 | PatchSystemsSystemIDTariffResponse500
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
    body: PatchSystemsSystemIDTariffBody,
) -> Response[
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
]:
    """Update the tariff v2 of a system

     Updates the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemsSystemIDTariffResponse400 | PatchSystemsSystemIDTariffResponse403 | PatchSystemsSystemIDTariffResponse404 | PatchSystemsSystemIDTariffResponse422 | PatchSystemsSystemIDTariffResponse500]
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
    body: PatchSystemsSystemIDTariffBody,
) -> (
    PatchSystemsSystemIDTariffResponse400
    | PatchSystemsSystemIDTariffResponse403
    | PatchSystemsSystemIDTariffResponse404
    | PatchSystemsSystemIDTariffResponse422
    | PatchSystemsSystemIDTariffResponse500
    | None
):
    """Update the tariff v2 of a system

     Updates the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PatchSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemsSystemIDTariffResponse400 | PatchSystemsSystemIDTariffResponse403 | PatchSystemsSystemIDTariffResponse404 | PatchSystemsSystemIDTariffResponse422 | PatchSystemsSystemIDTariffResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
