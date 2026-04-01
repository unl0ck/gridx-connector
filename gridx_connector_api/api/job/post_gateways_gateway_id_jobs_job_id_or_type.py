from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_gateways_gateway_id_jobs_job_id_or_type_response_201 import (
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201,
)
from ...models.post_gateways_gateway_id_jobs_job_id_or_type_response_400 import (
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse400,
)
from ...models.post_gateways_gateway_id_jobs_job_id_or_type_response_500 import (
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse500,
)
from ...types import Response


def _get_kwargs(
    gateway_id: UUID,
    job_id_or_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/gateways/{gateway_id}/jobs/{job_id_or_type}".format(
            gateway_id=quote(str(gateway_id), safe=""),
            job_id_or_type=quote(str(job_id_or_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostGatewaysGatewayIDJobsJobIDOrTypeResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostGatewaysGatewayIDJobsJobIDOrTypeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = PostGatewaysGatewayIDJobsJobIDOrTypeResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
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
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
]:
    """Create a job with a given type

     Creates a job with the given type for the given gateway, only if a job with that type doesn't
    already exist.
    In this case, the path parameter should be a job type. Please note that the job type is case-
    sensitive (The job type path paramter is lower case opposed to the enum value returned in the body).

      * `scan`: Once this job is triggered, the gridBox will look for connected appliances and update
    the list accordingly.

      * `reset`: This type of job resets gridBox to default and removes it from previously configured
    system.

      * `restart`: Once this job is triggered, the gridBox will restart.

    *Job execution is asynchronous and does not guarantee immediate execution.*

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGatewaysGatewayIDJobsJobIDOrTypeResponse201 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500]
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
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    """Create a job with a given type

     Creates a job with the given type for the given gateway, only if a job with that type doesn't
    already exist.
    In this case, the path parameter should be a job type. Please note that the job type is case-
    sensitive (The job type path paramter is lower case opposed to the enum value returned in the body).

      * `scan`: Once this job is triggered, the gridBox will look for connected appliances and update
    the list accordingly.

      * `reset`: This type of job resets gridBox to default and removes it from previously configured
    system.

      * `restart`: Once this job is triggered, the gridBox will restart.

    *Job execution is asynchronous and does not guarantee immediate execution.*

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGatewaysGatewayIDJobsJobIDOrTypeResponse201 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
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
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
]:
    """Create a job with a given type

     Creates a job with the given type for the given gateway, only if a job with that type doesn't
    already exist.
    In this case, the path parameter should be a job type. Please note that the job type is case-
    sensitive (The job type path paramter is lower case opposed to the enum value returned in the body).

      * `scan`: Once this job is triggered, the gridBox will look for connected appliances and update
    the list accordingly.

      * `reset`: This type of job resets gridBox to default and removes it from previously configured
    system.

      * `restart`: Once this job is triggered, the gridBox will restart.

    *Job execution is asynchronous and does not guarantee immediate execution.*

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGatewaysGatewayIDJobsJobIDOrTypeResponse201 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500]
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
    PostGatewaysGatewayIDJobsJobIDOrTypeResponse201
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400
    | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
    | None
):
    """Create a job with a given type

     Creates a job with the given type for the given gateway, only if a job with that type doesn't
    already exist.
    In this case, the path parameter should be a job type. Please note that the job type is case-
    sensitive (The job type path paramter is lower case opposed to the enum value returned in the body).

      * `scan`: Once this job is triggered, the gridBox will look for connected appliances and update
    the list accordingly.

      * `reset`: This type of job resets gridBox to default and removes it from previously configured
    system.

      * `restart`: Once this job is triggered, the gridBox will restart.

    *Job execution is asynchronous and does not guarantee immediate execution.*

    Args:
        gateway_id (UUID):
        job_id_or_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGatewaysGatewayIDJobsJobIDOrTypeResponse201 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse400 | PostGatewaysGatewayIDJobsJobIDOrTypeResponse500
    """

    return (
        await asyncio_detailed(
            gateway_id=gateway_id,
            job_id_or_type=job_id_or_type,
            client=client,
        )
    ).parsed
