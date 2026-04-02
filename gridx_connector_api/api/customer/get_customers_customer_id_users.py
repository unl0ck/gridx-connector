from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_customers_customer_id_users_response_200_item import GetCustomersCustomerIDUsersResponse200Item
from ...models.get_customers_customer_id_users_response_403 import GetCustomersCustomerIDUsersResponse403
from ...models.get_customers_customer_id_users_response_422 import GetCustomersCustomerIDUsersResponse422
from ...models.get_customers_customer_id_users_response_500 import GetCustomersCustomerIDUsersResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: UUID,
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customers/{customer_id}/users".format(
            customer_id=quote(str(customer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetCustomersCustomerIDUsersResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = GetCustomersCustomerIDUsersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetCustomersCustomerIDUsersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = GetCustomersCustomerIDUsersResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
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
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
]:
    """List Customer's users

     Get a list of all users that belong to this customer.

    Args:
        customer_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomersCustomerIDUsersResponse403 | GetCustomersCustomerIDUsersResponse422 | GetCustomersCustomerIDUsersResponse500 | list[GetCustomersCustomerIDUsersResponse200Item]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> (
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
    | None
):
    """List Customer's users

     Get a list of all users that belong to this customer.

    Args:
        customer_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomersCustomerIDUsersResponse403 | GetCustomersCustomerIDUsersResponse422 | GetCustomersCustomerIDUsersResponse500 | list[GetCustomersCustomerIDUsersResponse200Item]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
]:
    """List Customer's users

     Get a list of all users that belong to this customer.

    Args:
        customer_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomersCustomerIDUsersResponse403 | GetCustomersCustomerIDUsersResponse422 | GetCustomersCustomerIDUsersResponse500 | list[GetCustomersCustomerIDUsersResponse200Item]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
) -> (
    GetCustomersCustomerIDUsersResponse403
    | GetCustomersCustomerIDUsersResponse422
    | GetCustomersCustomerIDUsersResponse500
    | list[GetCustomersCustomerIDUsersResponse200Item]
    | None
):
    """List Customer's users

     Get a list of all users that belong to this customer.

    Args:
        customer_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        sort (str | Unset):
        order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomersCustomerIDUsersResponse403 | GetCustomersCustomerIDUsersResponse422 | GetCustomersCustomerIDUsersResponse500 | list[GetCustomersCustomerIDUsersResponse200Item]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            order=order,
        )
    ).parsed
