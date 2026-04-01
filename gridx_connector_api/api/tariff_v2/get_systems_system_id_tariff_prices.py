from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_systems_system_id_tariff_prices_response_200 import GetSystemsSystemIDTariffPricesResponse200
from ...models.get_systems_system_id_tariff_prices_response_403 import GetSystemsSystemIDTariffPricesResponse403
from ...models.get_systems_system_id_tariff_prices_response_404 import GetSystemsSystemIDTariffPricesResponse404
from ...models.get_systems_system_id_tariff_prices_response_500 import GetSystemsSystemIDTariffPricesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_id: UUID,
    *,
    interval: str,
    resolution: str | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["interval"] = interval

    params["resolution"] = resolution

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systems/{system_id}/tariff/prices".format(
            system_id=quote(str(system_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetSystemsSystemIDTariffPricesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = GetSystemsSystemIDTariffPricesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemsSystemIDTariffPricesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSystemsSystemIDTariffPricesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
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
    interval: str,
    resolution: str | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
]:
    """Retrieve the tariff end prices of a system

     Retrieves the end-price tariff for the system in the specified resolution (15-minute by default if
    not specified).
    The end-price is the price the customer is billed for (for market data tariffs for example after
    offset, VAT and provider fee are applied).

    Depending on the tariff settings, the tariff data might have been directly posted through the API,
    originate from market data
    or is extrapolated from static data.

    If the resolution of the underlying data doesn't correspond to the requested resolution the data
    will be up- or down-sampled.
    For example the market prices used by market data tariffs have a 1 hour resolution. If you request
    15min resolution you will
    get 4 equal periods per hour. If you request daily resolution, the average prices of 24 hourly
    periods will be returned per period.

    If there are missing price periods over the requested interval (which may happen for `EXTERNAL`
    tariffs), the end-price tariff will start after the last period gap, aligned with the requested
    resolution.
    That is, if the requested interval for a given day is from 00:00 to 12:00 and no prices were sent
    from at 02:15 to 03:45, the first period returned will be from 03:45 to 04:00 for a 15-min
    resolution or from 04:00 to 05:00 for an hourly resolution.

    Once calculated the prices won't change anymore for the requested period.
    Even if the tariff is reconfigured the returned price will stay the same.
    This is due to the fact that historical prices can not be changed anymore.
    Changes in the tariff will only have an effect in the future.

    The returned currency is determined by the currency of the underlying tariff if not specified
    otherwise.

    Args:
        system_id (UUID):
        interval (str):
        resolution (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTariffPricesResponse200 | GetSystemsSystemIDTariffPricesResponse403 | GetSystemsSystemIDTariffPricesResponse404 | GetSystemsSystemIDTariffPricesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
        resolution=resolution,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: str | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> (
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
    | None
):
    """Retrieve the tariff end prices of a system

     Retrieves the end-price tariff for the system in the specified resolution (15-minute by default if
    not specified).
    The end-price is the price the customer is billed for (for market data tariffs for example after
    offset, VAT and provider fee are applied).

    Depending on the tariff settings, the tariff data might have been directly posted through the API,
    originate from market data
    or is extrapolated from static data.

    If the resolution of the underlying data doesn't correspond to the requested resolution the data
    will be up- or down-sampled.
    For example the market prices used by market data tariffs have a 1 hour resolution. If you request
    15min resolution you will
    get 4 equal periods per hour. If you request daily resolution, the average prices of 24 hourly
    periods will be returned per period.

    If there are missing price periods over the requested interval (which may happen for `EXTERNAL`
    tariffs), the end-price tariff will start after the last period gap, aligned with the requested
    resolution.
    That is, if the requested interval for a given day is from 00:00 to 12:00 and no prices were sent
    from at 02:15 to 03:45, the first period returned will be from 03:45 to 04:00 for a 15-min
    resolution or from 04:00 to 05:00 for an hourly resolution.

    Once calculated the prices won't change anymore for the requested period.
    Even if the tariff is reconfigured the returned price will stay the same.
    This is due to the fact that historical prices can not be changed anymore.
    Changes in the tariff will only have an effect in the future.

    The returned currency is determined by the currency of the underlying tariff if not specified
    otherwise.

    Args:
        system_id (UUID):
        interval (str):
        resolution (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTariffPricesResponse200 | GetSystemsSystemIDTariffPricesResponse403 | GetSystemsSystemIDTariffPricesResponse404 | GetSystemsSystemIDTariffPricesResponse500
    """

    return sync_detailed(
        system_id=system_id,
        client=client,
        interval=interval,
        resolution=resolution,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: str | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
]:
    """Retrieve the tariff end prices of a system

     Retrieves the end-price tariff for the system in the specified resolution (15-minute by default if
    not specified).
    The end-price is the price the customer is billed for (for market data tariffs for example after
    offset, VAT and provider fee are applied).

    Depending on the tariff settings, the tariff data might have been directly posted through the API,
    originate from market data
    or is extrapolated from static data.

    If the resolution of the underlying data doesn't correspond to the requested resolution the data
    will be up- or down-sampled.
    For example the market prices used by market data tariffs have a 1 hour resolution. If you request
    15min resolution you will
    get 4 equal periods per hour. If you request daily resolution, the average prices of 24 hourly
    periods will be returned per period.

    If there are missing price periods over the requested interval (which may happen for `EXTERNAL`
    tariffs), the end-price tariff will start after the last period gap, aligned with the requested
    resolution.
    That is, if the requested interval for a given day is from 00:00 to 12:00 and no prices were sent
    from at 02:15 to 03:45, the first period returned will be from 03:45 to 04:00 for a 15-min
    resolution or from 04:00 to 05:00 for an hourly resolution.

    Once calculated the prices won't change anymore for the requested period.
    Even if the tariff is reconfigured the returned price will stay the same.
    This is due to the fact that historical prices can not be changed anymore.
    Changes in the tariff will only have an effect in the future.

    The returned currency is determined by the currency of the underlying tariff if not specified
    otherwise.

    Args:
        system_id (UUID):
        interval (str):
        resolution (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemsSystemIDTariffPricesResponse200 | GetSystemsSystemIDTariffPricesResponse403 | GetSystemsSystemIDTariffPricesResponse404 | GetSystemsSystemIDTariffPricesResponse500]
    """

    kwargs = _get_kwargs(
        system_id=system_id,
        interval=interval,
        resolution=resolution,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_id: UUID,
    *,
    client: AuthenticatedClient,
    interval: str,
    resolution: str | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> (
    GetSystemsSystemIDTariffPricesResponse200
    | GetSystemsSystemIDTariffPricesResponse403
    | GetSystemsSystemIDTariffPricesResponse404
    | GetSystemsSystemIDTariffPricesResponse500
    | None
):
    """Retrieve the tariff end prices of a system

     Retrieves the end-price tariff for the system in the specified resolution (15-minute by default if
    not specified).
    The end-price is the price the customer is billed for (for market data tariffs for example after
    offset, VAT and provider fee are applied).

    Depending on the tariff settings, the tariff data might have been directly posted through the API,
    originate from market data
    or is extrapolated from static data.

    If the resolution of the underlying data doesn't correspond to the requested resolution the data
    will be up- or down-sampled.
    For example the market prices used by market data tariffs have a 1 hour resolution. If you request
    15min resolution you will
    get 4 equal periods per hour. If you request daily resolution, the average prices of 24 hourly
    periods will be returned per period.

    If there are missing price periods over the requested interval (which may happen for `EXTERNAL`
    tariffs), the end-price tariff will start after the last period gap, aligned with the requested
    resolution.
    That is, if the requested interval for a given day is from 00:00 to 12:00 and no prices were sent
    from at 02:15 to 03:45, the first period returned will be from 03:45 to 04:00 for a 15-min
    resolution or from 04:00 to 05:00 for an hourly resolution.

    Once calculated the prices won't change anymore for the requested period.
    Even if the tariff is reconfigured the returned price will stay the same.
    This is due to the fact that historical prices can not be changed anymore.
    Changes in the tariff will only have an effect in the future.

    The returned currency is determined by the currency of the underlying tariff if not specified
    otherwise.

    Args:
        system_id (UUID):
        interval (str):
        resolution (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemsSystemIDTariffPricesResponse200 | GetSystemsSystemIDTariffPricesResponse403 | GetSystemsSystemIDTariffPricesResponse404 | GetSystemsSystemIDTariffPricesResponse500
    """

    return (
        await asyncio_detailed(
            system_id=system_id,
            client=client,
            interval=interval,
            resolution=resolution,
            currency=currency,
        )
    ).parsed
