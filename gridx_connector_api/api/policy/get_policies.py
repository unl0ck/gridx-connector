from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_policies_policy_document import GetPoliciesPolicyDocument
from ...models.get_policies_response_500 import GetPoliciesResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPoliciesResponse500 | list[GetPoliciesPolicyDocument] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetPoliciesPolicyDocument.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 500:
        response_500 = GetPoliciesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]]:
    """List Policy Documents

     Lists all ever created policy documents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetPoliciesResponse500 | list[GetPoliciesPolicyDocument] | None:
    """List Policy Documents

     Lists all ever created policy documents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]]:
    """List Policy Documents

     Lists all ever created policy documents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetPoliciesResponse500 | list[GetPoliciesPolicyDocument] | None:
    """List Policy Documents

     Lists all ever created policy documents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPoliciesResponse500 | list[GetPoliciesPolicyDocument]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
