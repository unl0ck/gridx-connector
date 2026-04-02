from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_system_tag_body import SetSystemTagBody
from ...models.set_system_tag_response_200 import SetSystemTagResponse200
from ...models.set_system_tag_response_201 import SetSystemTagResponse201
from ...models.set_system_tag_response_400 import SetSystemTagResponse400
from ...models.set_system_tag_response_403 import SetSystemTagResponse403
from ...models.set_system_tag_response_404 import SetSystemTagResponse404
from ...models.set_system_tag_response_500 import SetSystemTagResponse500
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    tag_name: str,
    *,
    body: SetSystemTagBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/systems/{system_id}/tags/{tag_name}".format(
            system_id=quote(str(system_id), safe=""),
            tag_name=quote(str(tag_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
    | None
):
    if response.status_code == 200:
        response_200 = SetSystemTagResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SetSystemTagResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = SetSystemTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SetSystemTagResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetSystemTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = SetSystemTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    body: SetSystemTagBody,
) -> Response[
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
]:
    """Create or update a tag for a system

     Creates or updates a tag for a specific system. If the tag doesn't exist, it will be created,
    and the status code `201 Created` will be returned.
    If the tag exists, its value will be updated and the status code `200 OK` will be returned
    (even if the new value is the same as the previous one).

    Args:
        system_id (UUID):
        tag_name (str):
        body (SetSystemTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetSystemTagResponse200 | SetSystemTagResponse201 | SetSystemTagResponse400 | SetSystemTagResponse403 | SetSystemTagResponse404 | SetSystemTagResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        tag_name=tag_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    body: SetSystemTagBody,
) -> (
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
    | None
):
    """Create or update a tag for a system

     Creates or updates a tag for a specific system. If the tag doesn't exist, it will be created,
    and the status code `201 Created` will be returned.
    If the tag exists, its value will be updated and the status code `200 OK` will be returned
    (even if the new value is the same as the previous one).

    Args:
        system_id (UUID):
        tag_name (str):
        body (SetSystemTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetSystemTagResponse200 | SetSystemTagResponse201 | SetSystemTagResponse400 | SetSystemTagResponse403 | SetSystemTagResponse404 | SetSystemTagResponse500
    """

    return sync_detailed(
        system_id=system_id,
        tag_name=tag_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    body: SetSystemTagBody,
) -> Response[
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
]:
    """Create or update a tag for a system

     Creates or updates a tag for a specific system. If the tag doesn't exist, it will be created,
    and the status code `201 Created` will be returned.
    If the tag exists, its value will be updated and the status code `200 OK` will be returned
    (even if the new value is the same as the previous one).

    Args:
        system_id (UUID):
        tag_name (str):
        body (SetSystemTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetSystemTagResponse200 | SetSystemTagResponse201 | SetSystemTagResponse400 | SetSystemTagResponse403 | SetSystemTagResponse404 | SetSystemTagResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        tag_name=tag_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    body: SetSystemTagBody,
) -> (
    SetSystemTagResponse200
    | SetSystemTagResponse201
    | SetSystemTagResponse400
    | SetSystemTagResponse403
    | SetSystemTagResponse404
    | SetSystemTagResponse500
    | None
):
    """Create or update a tag for a system

     Creates or updates a tag for a specific system. If the tag doesn't exist, it will be created,
    and the status code `201 Created` will be returned.
    If the tag exists, its value will be updated and the status code `200 OK` will be returned
    (even if the new value is the same as the previous one).

    Args:
        system_id (UUID):
        tag_name (str):
        body (SetSystemTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetSystemTagResponse200 | SetSystemTagResponse201 | SetSystemTagResponse400 | SetSystemTagResponse403 | SetSystemTagResponse404 | SetSystemTagResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            tag_name=tag_name,
            client=client,
            body=body,
        )
    ).parsed
