from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_account_tokens_token_id_body import PatchAccountTokensTokenIDBody
from ...models.patch_account_tokens_token_id_organizational_api_token import (
    PatchAccountTokensTokenIDOrganizationalAPIToken,
)
from ...types import Response


def _get_kwargs(
    token_id: UUID,
    *,
    body: PatchAccountTokensTokenIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/account/tokens/{token_id}".format(
            token_id=quote(str(token_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchAccountTokensTokenIDOrganizationalAPIToken | None:
    if response.status_code == 200:
        response_200 = PatchAccountTokensTokenIDOrganizationalAPIToken.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchAccountTokensTokenIDOrganizationalAPIToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountTokensTokenIDBody,
) -> Response[Any | PatchAccountTokensTokenIDOrganizationalAPIToken]:
    """Partially update an organizational API token

     Partially update the organizational API token of the currently authenticated account.

    Args:
        token_id (UUID):
        body (PatchAccountTokensTokenIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAccountTokensTokenIDOrganizationalAPIToken]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountTokensTokenIDBody,
) -> Any | PatchAccountTokensTokenIDOrganizationalAPIToken | None:
    """Partially update an organizational API token

     Partially update the organizational API token of the currently authenticated account.

    Args:
        token_id (UUID):
        body (PatchAccountTokensTokenIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAccountTokensTokenIDOrganizationalAPIToken
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountTokensTokenIDBody,
) -> Response[Any | PatchAccountTokensTokenIDOrganizationalAPIToken]:
    """Partially update an organizational API token

     Partially update the organizational API token of the currently authenticated account.

    Args:
        token_id (UUID):
        body (PatchAccountTokensTokenIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAccountTokensTokenIDOrganizationalAPIToken]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAccountTokensTokenIDBody,
) -> Any | PatchAccountTokensTokenIDOrganizationalAPIToken | None:
    """Partially update an organizational API token

     Partially update the organizational API token of the currently authenticated account.

    Args:
        token_id (UUID):
        body (PatchAccountTokensTokenIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAccountTokensTokenIDOrganizationalAPIToken
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            body=body,
        )
    ).parsed
