from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_body import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_201 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_400 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_403 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_404 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_422 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422,
)
from ...models.post_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_500 import (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    body: PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/gateways/{gateway_id}/appliances/{appliance_id}/ev/configuration".format(
            gateway_id=quote(str(gateway_id), safe=""),
            appliance_id=quote(str(appliance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> Response[
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Create an EV Configuration

     Creates an EV charging station's configuration if no configuration is present.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Create an EV Configuration

     Creates an EV charging station's configuration if no configuration is present.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> Response[
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
]:
    """Create an EV Configuration

     Creates an EV charging station's configuration if no configuration is present.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        appliance_id=appliance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    appliance_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody,
) -> (
    PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422
    | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    | None
):
    """Create an EV Configuration

     Creates an EV charging station's configuration if no configuration is present.

    Args:
        gateway_id (UUID):
        appliance_id (UUID):
        body (PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse201 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse400 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse403 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse404 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse422 | PostGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            appliance_id=appliance_id,
            client=client,
            body=body,
        )
    ).parsed
