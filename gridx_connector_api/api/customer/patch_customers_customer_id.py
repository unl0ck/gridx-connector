from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_customers_customer_id_body import PatchCustomersCustomerIDBody
from ...models.patch_customers_customer_id_customer_account import PatchCustomersCustomerIDCustomerAccount
from ...models.patch_customers_customer_id_response_400 import PatchCustomersCustomerIDResponse400
from ...models.patch_customers_customer_id_response_403 import PatchCustomersCustomerIDResponse403
from ...models.patch_customers_customer_id_response_422 import PatchCustomersCustomerIDResponse422
from ...models.patch_customers_customer_id_response_500 import PatchCustomersCustomerIDResponse500
from ...types import Response


def _get_kwargs(
    customer_id: UUID,
    *,
    body: PatchCustomersCustomerIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/customers/{customer_id}".format(
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchCustomersCustomerIDCustomerAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchCustomersCustomerIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchCustomersCustomerIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PatchCustomersCustomerIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchCustomersCustomerIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
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
    body: PatchCustomersCustomerIDBody,
) -> Response[
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
]:
    """Edit a single customer

    Args:
        customer_id (UUID):
        body (PatchCustomersCustomerIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCustomersCustomerIDCustomerAccount | PatchCustomersCustomerIDResponse400 | PatchCustomersCustomerIDResponse403 | PatchCustomersCustomerIDResponse422 | PatchCustomersCustomerIDResponse500]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchCustomersCustomerIDBody,
) -> (
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
    | None
):
    """Edit a single customer

    Args:
        customer_id (UUID):
        body (PatchCustomersCustomerIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCustomersCustomerIDCustomerAccount | PatchCustomersCustomerIDResponse400 | PatchCustomersCustomerIDResponse403 | PatchCustomersCustomerIDResponse422 | PatchCustomersCustomerIDResponse500
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchCustomersCustomerIDBody,
) -> Response[
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
]:
    """Edit a single customer

    Args:
        customer_id (UUID):
        body (PatchCustomersCustomerIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCustomersCustomerIDCustomerAccount | PatchCustomersCustomerIDResponse400 | PatchCustomersCustomerIDResponse403 | PatchCustomersCustomerIDResponse422 | PatchCustomersCustomerIDResponse500]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchCustomersCustomerIDBody,
) -> (
    PatchCustomersCustomerIDCustomerAccount
    | PatchCustomersCustomerIDResponse400
    | PatchCustomersCustomerIDResponse403
    | PatchCustomersCustomerIDResponse422
    | PatchCustomersCustomerIDResponse500
    | None
):
    """Edit a single customer

    Args:
        customer_id (UUID):
        body (PatchCustomersCustomerIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCustomersCustomerIDCustomerAccount | PatchCustomersCustomerIDResponse400 | PatchCustomersCustomerIDResponse403 | PatchCustomersCustomerIDResponse422 | PatchCustomersCustomerIDResponse500
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            body=body,
        )
    ).parsed
