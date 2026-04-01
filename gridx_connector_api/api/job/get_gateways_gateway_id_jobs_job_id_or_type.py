from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gateways_gateway_id_jobs_job_id_or_type_response_200 import (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200,
)
from ...models.get_gateways_gateway_id_jobs_job_id_or_type_response_400 import (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse400,
)
from ...models.get_gateways_gateway_id_jobs_job_id_or_type_response_404 import (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse404,
)
from ...models.get_gateways_gateway_id_jobs_job_id_or_type_response_500 import (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    job_id_or_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateways/{gateway_id}/jobs/{job_id_or_type}".format(
            gateway_id=quote(str(gateway_id), safe=""),
            job_id_or_type=quote(str(job_id_or_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetGatewaysGatewayIDJobsJobIDOrTypeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewaysGatewayIDJobsJobIDOrTypeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetGatewaysGatewayIDJobsJobIDOrTypeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewaysGatewayIDJobsJobIDOrTypeResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gateway_id: UUID,
    job_id_or_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
]:
    """Get a Job

     Gets a particular job that belongs to the given gateway. In this case, the path parameter should be
    a job ID.

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDJobsJobIDOrTypeResponse200 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        job_id_or_type=job_id_or_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gateway_id: UUID,
    job_id_or_type: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    """Get a Job

     Gets a particular job that belongs to the given gateway. In this case, the path parameter should be
    a job ID.

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDJobsJobIDOrTypeResponse200 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
    """

    return sync_detailed(
        gateway_id=gateway_id,
        job_id_or_type=job_id_or_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    gateway_id: UUID,
    job_id_or_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
]:
    """Get a Job

     Gets a particular job that belongs to the given gateway. In this case, the path parameter should be
    a job ID.

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGatewaysGatewayIDJobsJobIDOrTypeResponse200 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500]
    """

    kwargs = _get_kwargs(
        gateway_id=gateway_id,
        job_id_or_type=job_id_or_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gateway_id: UUID,
    job_id_or_type: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetGatewaysGatewayIDJobsJobIDOrTypeResponse200
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404
    | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    """Get a Job

     Gets a particular job that belongs to the given gateway. In this case, the path parameter should be
    a job ID.

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGatewaysGatewayIDJobsJobIDOrTypeResponse200 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse400 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse404 | GetGatewaysGatewayIDJobsJobIDOrTypeResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            job_id_or_type=job_id_or_type,
            client=client,
        )
    ).parsed
