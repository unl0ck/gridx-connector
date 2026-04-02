from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_systems_system_id_tariff_prices_body import PostSystemsSystemIDTariffPricesBody
from ...models.post_systems_system_id_tariff_prices_response_201 import PostSystemsSystemIDTariffPricesResponse201
from ...models.post_systems_system_id_tariff_prices_response_400 import PostSystemsSystemIDTariffPricesResponse400
from ...models.post_systems_system_id_tariff_prices_response_422 import PostSystemsSystemIDTariffPricesResponse422
from ...models.post_systems_system_id_tariff_prices_response_500 import PostSystemsSystemIDTariffPricesResponse500
from ...models.post_systems_system_id_tariff_prices_response_502 import PostSystemsSystemIDTariffPricesResponse502
from ...types import Response


def _get_kwargs(
    system_id: UUID,
    *,
    body: PostSystemsSystemIDTariffPricesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systems/{system_id}/tariff/prices".format(
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
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
    | None
):
    if response.status_code == 201:
        response_201 = PostSystemsSystemIDTariffPricesResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostSystemsSystemIDTariffPricesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = PostSystemsSystemIDTariffPricesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostSystemsSystemIDTariffPricesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = PostSystemsSystemIDTariffPricesResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
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
    body: PostSystemsSystemIDTariffPricesBody,
) -> Response[
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
]:
    """Set tariff end prices of a system

     Sets the tariff end prices for **external tariffs**.

    The sent price periods have a few restrictions:
    - They must have a 15 minute resolution.
    - They must not have gaps for current and future prices (gaps in the past are allowed).

    The prices can be sent in all supported currencies and will be converted by the `GET /tariff/prices`
    endpoint accordingly.

    You don't have to send your prices in all the currencies you want to support.
    Internally they always will be converted to Euro, therefore sending the same price periods in
    different currencies will overwrite
    the previously sent price periods.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDTariffPricesResponse201 | PostSystemsSystemIDTariffPricesResponse400 | PostSystemsSystemIDTariffPricesResponse422 | PostSystemsSystemIDTariffPricesResponse500 | PostSystemsSystemIDTariffPricesResponse502]
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
    body: PostSystemsSystemIDTariffPricesBody,
) -> (
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
    | None
):
    """Set tariff end prices of a system

     Sets the tariff end prices for **external tariffs**.

    The sent price periods have a few restrictions:
    - They must have a 15 minute resolution.
    - They must not have gaps for current and future prices (gaps in the past are allowed).

    The prices can be sent in all supported currencies and will be converted by the `GET /tariff/prices`
    endpoint accordingly.

    You don't have to send your prices in all the currencies you want to support.
    Internally they always will be converted to Euro, therefore sending the same price periods in
    different currencies will overwrite
    the previously sent price periods.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDTariffPricesResponse201 | PostSystemsSystemIDTariffPricesResponse400 | PostSystemsSystemIDTariffPricesResponse422 | PostSystemsSystemIDTariffPricesResponse500 | PostSystemsSystemIDTariffPricesResponse502
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
    body: PostSystemsSystemIDTariffPricesBody,
) -> Response[
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
]:
    """Set tariff end prices of a system

     Sets the tariff end prices for **external tariffs**.

    The sent price periods have a few restrictions:
    - They must have a 15 minute resolution.
    - They must not have gaps for current and future prices (gaps in the past are allowed).

    The prices can be sent in all supported currencies and will be converted by the `GET /tariff/prices`
    endpoint accordingly.

    You don't have to send your prices in all the currencies you want to support.
    Internally they always will be converted to Euro, therefore sending the same price periods in
    different currencies will overwrite
    the previously sent price periods.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemsSystemIDTariffPricesResponse201 | PostSystemsSystemIDTariffPricesResponse400 | PostSystemsSystemIDTariffPricesResponse422 | PostSystemsSystemIDTariffPricesResponse500 | PostSystemsSystemIDTariffPricesResponse502]
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
    body: PostSystemsSystemIDTariffPricesBody,
) -> (
    PostSystemsSystemIDTariffPricesResponse201
    | PostSystemsSystemIDTariffPricesResponse400
    | PostSystemsSystemIDTariffPricesResponse422
    | PostSystemsSystemIDTariffPricesResponse500
    | PostSystemsSystemIDTariffPricesResponse502
    | None
):
    """Set tariff end prices of a system

     Sets the tariff end prices for **external tariffs**.

    The sent price periods have a few restrictions:
    - They must have a 15 minute resolution.
    - They must not have gaps for current and future prices (gaps in the past are allowed).

    The prices can be sent in all supported currencies and will be converted by the `GET /tariff/prices`
    endpoint accordingly.

    You don't have to send your prices in all the currencies you want to support.
    Internally they always will be converted to Euro, therefore sending the same price periods in
    different currencies will overwrite
    the previously sent price periods.

    Args:
        system_id (UUID):
        body (PostSystemsSystemIDTariffPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemsSystemIDTariffPricesResponse201 | PostSystemsSystemIDTariffPricesResponse400 | PostSystemsSystemIDTariffPricesResponse422 | PostSystemsSystemIDTariffPricesResponse500 | PostSystemsSystemIDTariffPricesResponse502
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
