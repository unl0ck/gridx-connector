from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_functionalities_functionality_id_response_200 import (
    GetProductFunctionalitiesFunctionalityIDResponse200,
)
from ...models.get_product_functionalities_functionality_id_response_404 import (
    GetProductFunctionalitiesFunctionalityIDResponse404,
)
from ...models.get_product_functionalities_functionality_id_response_422 import (
    GetProductFunctionalitiesFunctionalityIDResponse422,
)
from ...models.get_product_functionalities_functionality_id_response_500 import (
    GetProductFunctionalitiesFunctionalityIDResponse500,
)
from ...types import Response


def _get_kwargs(
    functionality_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product-functionalities/{functionality_id}".format(
            functionality_id=quote(str(functionality_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetProductFunctionalitiesFunctionalityIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetProductFunctionalitiesFunctionalityIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetProductFunctionalitiesFunctionalityIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetProductFunctionalitiesFunctionalityIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    functionality_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
]:
    """Get a Product Functionality

     Lists all product functionalities.

    Args:
        functionality_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductFunctionalitiesFunctionalityIDResponse200 | GetProductFunctionalitiesFunctionalityIDResponse404 | GetProductFunctionalitiesFunctionalityIDResponse422 | GetProductFunctionalitiesFunctionalityIDResponse500]
    """

    kwargs = _get_kwargs(
        functionality_id=functionality_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    functionality_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
    | None
):
    """Get a Product Functionality

     Lists all product functionalities.

    Args:
        functionality_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductFunctionalitiesFunctionalityIDResponse200 | GetProductFunctionalitiesFunctionalityIDResponse404 | GetProductFunctionalitiesFunctionalityIDResponse422 | GetProductFunctionalitiesFunctionalityIDResponse500
    """

    return sync_detailed(
        functionality_id=functionality_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    functionality_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
]:
    """Get a Product Functionality

     Lists all product functionalities.

    Args:
        functionality_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductFunctionalitiesFunctionalityIDResponse200 | GetProductFunctionalitiesFunctionalityIDResponse404 | GetProductFunctionalitiesFunctionalityIDResponse422 | GetProductFunctionalitiesFunctionalityIDResponse500]
    """

    kwargs = _get_kwargs(
        functionality_id=functionality_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    functionality_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetProductFunctionalitiesFunctionalityIDResponse200
    | GetProductFunctionalitiesFunctionalityIDResponse404
    | GetProductFunctionalitiesFunctionalityIDResponse422
    | GetProductFunctionalitiesFunctionalityIDResponse500
    | None
):
    """Get a Product Functionality

     Lists all product functionalities.

    Args:
        functionality_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductFunctionalitiesFunctionalityIDResponse200 | GetProductFunctionalitiesFunctionalityIDResponse404 | GetProductFunctionalitiesFunctionalityIDResponse422 | GetProductFunctionalitiesFunctionalityIDResponse500
    """

    return (
        await asyncio_detailed(
            functionality_id=functionality_id,
            client=client,
        )
    ).parsed
