from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_appliances_response_403 import GetGatewaysGatewayIDAppliancesResponse403
from ...models.get_gateways_gateway_id_appliances_response_404 import GetGatewaysGatewayIDAppliancesResponse404
from ...models.get_gateways_gateway_id_appliances_response_500 import GetGatewaysGatewayIDAppliancesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gateway_id: UUID,
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    list_all: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["listAll"] = list_all

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/appliances".format(
            gateway_id=quote(str(gateway_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
    | None
):
    if response.status_code == 403:
        response_403 = GetGatewaysGatewayIDAppliancesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDAppliancesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDAppliancesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    list_all: bool | Unset = False,
) -> Response[
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
]:
    """List Gateway's Appliances

     Lists appliances that belong to the given gateway.

    Children appliances, e.g. those of hybrid inverters, are not included by default.
    To include them, `listAll` parameter must be set to `true`.

    Args:
        gateway_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        list_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesResponse403 | GetGatewaysGatewayIDAppliancesResponse404 | GetGatewaysGatewayIDAppliancesResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        page=page,
        per_page=per_page,
        list_all=list_all,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    list_all: bool | Unset = False,
) -> (
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
    | None
):
    """List Gateway's Appliances

     Lists appliances that belong to the given gateway.

    Children appliances, e.g. those of hybrid inverters, are not included by default.
    To include them, `listAll` parameter must be set to `true`.

    Args:
        gateway_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        list_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesResponse403 | GetGatewaysGatewayIDAppliancesResponse404 | GetGatewaysGatewayIDAppliancesResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        client=client,
        page=page,
        per_page=per_page,
        list_all=list_all,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    list_all: bool | Unset = False,
) -> Response[
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
]:
    """List Gateway's Appliances

     Lists appliances that belong to the given gateway.

    Children appliances, e.g. those of hybrid inverters, are not included by default.
    To include them, `listAll` parameter must be set to `true`.

    Args:
        gateway_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        list_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDAppliancesResponse403 | GetGatewaysGatewayIDAppliancesResponse404 | GetGatewaysGatewayIDAppliancesResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        page=page,
        per_page=per_page,
        list_all=list_all,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    list_all: bool | Unset = False,
) -> (
    GetGatewaysGatewayIDAppliancesResponse403
    | GetGatewaysGatewayIDAppliancesResponse404
    | GetGatewaysGatewayIDAppliancesResponse500
    | None
):
    """List Gateway's Appliances

     Lists appliances that belong to the given gateway.

    Children appliances, e.g. those of hybrid inverters, are not included by default.
    To include them, `listAll` parameter must be set to `true`.

    Args:
        gateway_id (UUID):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        list_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDAppliancesResponse403 | GetGatewaysGatewayIDAppliancesResponse404 | GetGatewaysGatewayIDAppliancesResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            client=client,
            page=page,
            per_page=per_page,
            list_all=list_all,
        )
    ).parsed
