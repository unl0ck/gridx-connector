from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_system_id_tariff_body import PostSystemsSystemIDTariffBody
from ...models.post_systems_system_id_tariff_response_400 import PostSystemsSystemIDTariffResponse400
from ...models.post_systems_system_id_tariff_response_403 import PostSystemsSystemIDTariffResponse403
from ...models.post_systems_system_id_tariff_response_404 import PostSystemsSystemIDTariffResponse404
from ...models.post_systems_system_id_tariff_response_409 import PostSystemsSystemIDTariffResponse409
from ...models.post_systems_system_id_tariff_response_422 import PostSystemsSystemIDTariffResponse422
from ...models.post_systems_system_id_tariff_response_500 import PostSystemsSystemIDTariffResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PostSystemsSystemIDTariffBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
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
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemsSystemIDTariffResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PostSystemsSystemIDTariffResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemsSystemIDTariffResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = PostSystemsSystemIDTariffResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = PostSystemsSystemIDTariffResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostSystemsSystemIDTariffResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
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
    body: PostSystemsSystemIDTariffBody,
) -> Response[
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
]:
    """Set the tariff v2 of a system

     Sets the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDTariffResponse400 | PostSystemsSystemIDTariffResponse403 | PostSystemsSystemIDTariffResponse404 | PostSystemsSystemIDTariffResponse409 | PostSystemsSystemIDTariffResponse422 | PostSystemsSystemIDTariffResponse500]
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
    body: PostSystemsSystemIDTariffBody,
) -> (
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
    | None
):
    """Set the tariff v2 of a system

     Sets the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDTariffResponse400 | PostSystemsSystemIDTariffResponse403 | PostSystemsSystemIDTariffResponse404 | PostSystemsSystemIDTariffResponse409 | PostSystemsSystemIDTariffResponse422 | PostSystemsSystemIDTariffResponse500
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
    body: PostSystemsSystemIDTariffBody,
) -> Response[
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
]:
    """Set the tariff v2 of a system

     Sets the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDTariffResponse400 | PostSystemsSystemIDTariffResponse403 | PostSystemsSystemIDTariffResponse404 | PostSystemsSystemIDTariffResponse409 | PostSystemsSystemIDTariffResponse422 | PostSystemsSystemIDTariffResponse500]
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
    body: PostSystemsSystemIDTariffBody,
) -> (
    PostSystemsSystemIDTariffResponse400
    | PostSystemsSystemIDTariffResponse403
    | PostSystemsSystemIDTariffResponse404
    | PostSystemsSystemIDTariffResponse409
    | PostSystemsSystemIDTariffResponse422
    | PostSystemsSystemIDTariffResponse500
    | None
):
    """Set the tariff v2 of a system

     Sets the tariff v2 of the system.

    See the response bodies description which fields have to be set for which
    `feedinType`/`offtakeType`.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDTariffResponse400 | PostSystemsSystemIDTariffResponse403 | PostSystemsSystemIDTariffResponse404 | PostSystemsSystemIDTariffResponse409 | PostSystemsSystemIDTariffResponse422 | PostSystemsSystemIDTariffResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
