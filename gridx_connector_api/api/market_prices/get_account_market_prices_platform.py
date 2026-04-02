from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_account_market_prices_platform_energy_market_data import (
    GetAccountMarketPricesPlatformEnergyMarketData,
)
from ...models.get_account_market_prices_platform_response_400 import GetAccountMarketPricesPlatformResponse400
from ...models.get_account_market_prices_platform_response_403 import GetAccountMarketPricesPlatformResponse403
from ...models.get_account_market_prices_platform_response_404 import GetAccountMarketPricesPlatformResponse404
from ...models.get_account_market_prices_platform_response_500 import GetAccountMarketPricesPlatformResponse500
from ...models.get_account_market_prices_platform_response_502 import GetAccountMarketPricesPlatformResponse502
from ...types import UNSET, Response, Unset


def _get_kwargs(
    platform: str,
    *,
    domain: str | Unset = UNSET,
    interval: str,
    timezone: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["domain"] = domain

    params["interval"] = interval

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/market-prices/{platform}".format(
            platform=quote(str(platform), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
    | None
):
    if response.status_code == 200:
        response_200 = GetAccountMarketPricesPlatformEnergyMarketData.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAccountMarketPricesPlatformResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GetAccountMarketPricesPlatformResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccountMarketPricesPlatformResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccountMarketPricesPlatformResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = GetAccountMarketPricesPlatformResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform: str,
    *,
    client: AuthenticatedClient,
    domain: str | Unset = UNSET,
    interval: str,
    timezone: str,
) -> Response[
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
]:
    """Retrieve energy market prices for the authenticated account

     List energy market prices for the given interval. Prices are fetched from an external energy market
    platform.
    For the given interval, the hourly prices of the second to last day and for the last day are
    returned in a 60M resolution.
    For all the other days in the interval, the average daily price is returned.
    For example, in order to get hourly prices for the current day and the day before, set the **end**
    of the interval to the current day.

    **Deprecated** - Use `/systems/{systemID}/tariff/prices` instead.

    Args:
        platform (str):
        domain (str | Unset):
        interval (str):
        timezone (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountMarketPricesPlatformEnergyMarketData | GetAccountMarketPricesPlatformResponse400 | GetAccountMarketPricesPlatformResponse403 | GetAccountMarketPricesPlatformResponse404 | GetAccountMarketPricesPlatformResponse500 | GetAccountMarketPricesPlatformResponse502]
    """

    kwargs = _get_kwargs(
        platform=platform,
        domain=domain,
        interval=interval,
        timezone=timezone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform: str,
    *,
    client: AuthenticatedClient,
    domain: str | Unset = UNSET,
    interval: str,
    timezone: str,
) -> (
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
    | None
):
    """Retrieve energy market prices for the authenticated account

     List energy market prices for the given interval. Prices are fetched from an external energy market
    platform.
    For the given interval, the hourly prices of the second to last day and for the last day are
    returned in a 60M resolution.
    For all the other days in the interval, the average daily price is returned.
    For example, in order to get hourly prices for the current day and the day before, set the **end**
    of the interval to the current day.

    **Deprecated** - Use `/systems/{systemID}/tariff/prices` instead.

    Args:
        platform (str):
        domain (str | Unset):
        interval (str):
        timezone (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountMarketPricesPlatformEnergyMarketData | GetAccountMarketPricesPlatformResponse400 | GetAccountMarketPricesPlatformResponse403 | GetAccountMarketPricesPlatformResponse404 | GetAccountMarketPricesPlatformResponse500 | GetAccountMarketPricesPlatformResponse502
    """

    return sync_detailed(
        platform=platform,
        client=client,
        domain=domain,
        interval=interval,
        timezone=timezone,
    ).parsed


async def asyncio_detailed(
    platform: str,
    *,
    client: AuthenticatedClient,
    domain: str | Unset = UNSET,
    interval: str,
    timezone: str,
) -> Response[
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
]:
    """Retrieve energy market prices for the authenticated account

     List energy market prices for the given interval. Prices are fetched from an external energy market
    platform.
    For the given interval, the hourly prices of the second to last day and for the last day are
    returned in a 60M resolution.
    For all the other days in the interval, the average daily price is returned.
    For example, in order to get hourly prices for the current day and the day before, set the **end**
    of the interval to the current day.

    **Deprecated** - Use `/systems/{systemID}/tariff/prices` instead.

    Args:
        platform (str):
        domain (str | Unset):
        interval (str):
        timezone (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountMarketPricesPlatformEnergyMarketData | GetAccountMarketPricesPlatformResponse400 | GetAccountMarketPricesPlatformResponse403 | GetAccountMarketPricesPlatformResponse404 | GetAccountMarketPricesPlatformResponse500 | GetAccountMarketPricesPlatformResponse502]
    """

    kwargs = _get_kwargs(
        platform=platform,
        domain=domain,
        interval=interval,
        timezone=timezone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform: str,
    *,
    client: AuthenticatedClient,
    domain: str | Unset = UNSET,
    interval: str,
    timezone: str,
) -> (
    GetAccountMarketPricesPlatformEnergyMarketData
    | GetAccountMarketPricesPlatformResponse400
    | GetAccountMarketPricesPlatformResponse403
    | GetAccountMarketPricesPlatformResponse404
    | GetAccountMarketPricesPlatformResponse500
    | GetAccountMarketPricesPlatformResponse502
    | None
):
    """Retrieve energy market prices for the authenticated account

     List energy market prices for the given interval. Prices are fetched from an external energy market
    platform.
    For the given interval, the hourly prices of the second to last day and for the last day are
    returned in a 60M resolution.
    For all the other days in the interval, the average daily price is returned.
    For example, in order to get hourly prices for the current day and the day before, set the **end**
    of the interval to the current day.

    **Deprecated** - Use `/systems/{systemID}/tariff/prices` instead.

    Args:
        platform (str):
        domain (str | Unset):
        interval (str):
        timezone (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountMarketPricesPlatformEnergyMarketData | GetAccountMarketPricesPlatformResponse400 | GetAccountMarketPricesPlatformResponse403 | GetAccountMarketPricesPlatformResponse404 | GetAccountMarketPricesPlatformResponse500 | GetAccountMarketPricesPlatformResponse502
    """

    return (
        await asyncio_detailed(
            platform=platform,
            client=client,
            domain=domain,
            interval=interval,
            timezone=timezone,
        )
    ).parsed
