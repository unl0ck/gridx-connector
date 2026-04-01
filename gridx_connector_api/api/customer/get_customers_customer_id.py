from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_customers_customer_id_customer_account import GetCustomersCustomerIDCustomerAccount
from ...models.get_customers_customer_id_response_400 import GetCustomersCustomerIDResponse400
from ...models.get_customers_customer_id_response_403 import GetCustomersCustomerIDResponse403
from ...models.get_customers_customer_id_response_404 import GetCustomersCustomerIDResponse404
from ...models.get_customers_customer_id_response_500 import GetCustomersCustomerIDResponse500
from ...types import Response


def _get_kwargs(
    customer_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customers/{customer_id}".format(
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetCustomersCustomerIDCustomerAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCustomersCustomerIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetCustomersCustomerIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCustomersCustomerIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetCustomersCustomerIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
]:
    """Get Customer

     Get a single customer given its account ID.

    Args:
        customer_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomersCustomerIDCustomerAccount | GetCustomersCustomerIDResponse400 | GetCustomersCustomerIDResponse403 | GetCustomersCustomerIDResponse404 | GetCustomersCustomerIDResponse500]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
    | None
):
    """Get Customer

     Get a single customer given its account ID.

    Args:
        customer_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomersCustomerIDCustomerAccount | GetCustomersCustomerIDResponse400 | GetCustomersCustomerIDResponse403 | GetCustomersCustomerIDResponse404 | GetCustomersCustomerIDResponse500
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
]:
    """Get Customer

     Get a single customer given its account ID.

    Args:
        customer_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomersCustomerIDCustomerAccount | GetCustomersCustomerIDResponse400 | GetCustomersCustomerIDResponse403 | GetCustomersCustomerIDResponse404 | GetCustomersCustomerIDResponse500]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetCustomersCustomerIDCustomerAccount
    | GetCustomersCustomerIDResponse400
    | GetCustomersCustomerIDResponse403
    | GetCustomersCustomerIDResponse404
    | GetCustomersCustomerIDResponse500
    | None
):
    """Get Customer

     Get a single customer given its account ID.

    Args:
        customer_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomersCustomerIDCustomerAccount | GetCustomersCustomerIDResponse400 | GetCustomersCustomerIDResponse403 | GetCustomersCustomerIDResponse404 | GetCustomersCustomerIDResponse500
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
        )
    ).parsed
