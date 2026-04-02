from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_clusters_cluster_id_live_response_401 import GetClustersClusterIDLiveResponse401
from ...models.get_clusters_cluster_id_live_response_403 import GetClustersClusterIDLiveResponse403
from ...models.get_clusters_cluster_id_live_response_404 import GetClustersClusterIDLiveResponse404
from ...models.get_clusters_cluster_id_live_response_500 import GetClustersClusterIDLiveResponse500
from ...types import Response


def _get_kwargs(
    cluster_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clusters/{cluster_id}/live".format(
            cluster_id=quote(str(cluster_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
    | None
):
    if response.status_code == 401:
        response_401 = GetClustersClusterIDLiveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetClustersClusterIDLiveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetClustersClusterIDLiveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetClustersClusterIDLiveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
]:
    """Retrieve Cluster's Live Measurement.

     Retrieves a cluster's latest aggregated measurement.

    Args:
        cluster_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetClustersClusterIDLiveResponse401 | GetClustersClusterIDLiveResponse403 | GetClustersClusterIDLiveResponse404 | GetClustersClusterIDLiveResponse500]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
    | None
):
    """Retrieve Cluster's Live Measurement.

     Retrieves a cluster's latest aggregated measurement.

    Args:
        cluster_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetClustersClusterIDLiveResponse401 | GetClustersClusterIDLiveResponse403 | GetClustersClusterIDLiveResponse404 | GetClustersClusterIDLiveResponse500
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
]:
    """Retrieve Cluster's Live Measurement.

     Retrieves a cluster's latest aggregated measurement.

    Args:
        cluster_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetClustersClusterIDLiveResponse401 | GetClustersClusterIDLiveResponse403 | GetClustersClusterIDLiveResponse404 | GetClustersClusterIDLiveResponse500]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_id: UUID,
    *,
    client: AuthenticatedClient,
) -> (
    GetClustersClusterIDLiveResponse401
    | GetClustersClusterIDLiveResponse403
    | GetClustersClusterIDLiveResponse404
    | GetClustersClusterIDLiveResponse500
    | None
):
    """Retrieve Cluster's Live Measurement.

     Retrieves a cluster's latest aggregated measurement.

    Args:
        cluster_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetClustersClusterIDLiveResponse401 | GetClustersClusterIDLiveResponse403 | GetClustersClusterIDLiveResponse404 | GetClustersClusterIDLiveResponse500
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed
