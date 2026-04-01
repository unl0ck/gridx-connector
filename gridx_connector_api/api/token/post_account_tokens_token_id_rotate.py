from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_account_tokens_token_id_rotate_lifetime import PostAccountTokensTokenIDRotateLifetime
from ...models.post_account_tokens_token_id_rotate_organizational_api_token_with_secret import (
    PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret,
)
from ...models.post_account_tokens_token_id_rotate_response_403 import PostAccountTokensTokenIDRotateResponse403
from ...models.post_account_tokens_token_id_rotate_response_422 import PostAccountTokensTokenIDRotateResponse422
from ...models.post_account_tokens_token_id_rotate_response_500 import PostAccountTokensTokenIDRotateResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: UUID,
    *,
    lifetime: PostAccountTokensTokenIDRotateLifetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lifetime: str | Unset = UNSET
    if not isinstance(lifetime, Unset):
        json_lifetime = lifetime.value

    params["lifetime"] = json_lifetime

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/tokens/{token_id}/rotate".format(
            token_id=quote(str(token_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = PostAccountTokensTokenIDRotateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = PostAccountTokensTokenIDRotateResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostAccountTokensTokenIDRotateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
]:
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
    lifetime: PostAccountTokensTokenIDRotateLifetime | Unset = UNSET,
) -> Response[
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
]:
    """Rotate an existing organizational API token

     Rotates a non-expired organizational API token for the given token ID by creating and returning a
    new token
    with the same properties as the original one, specified by the `tokenID` path parameter.
    The new token's expiry date is based on the original one extended by the value specified in the
    `lifetime` query parameter.
    The original token's permissions are copied verbatim.

    Args:
        token_id (UUID):
        lifetime (PostAccountTokensTokenIDRotateLifetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret | PostAccountTokensTokenIDRotateResponse403 | PostAccountTokensTokenIDRotateResponse422 | PostAccountTokensTokenIDRotateResponse500]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        lifetime=lifetime,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    lifetime: PostAccountTokensTokenIDRotateLifetime | Unset = UNSET,
) -> (
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
    | None
):
    """Rotate an existing organizational API token

     Rotates a non-expired organizational API token for the given token ID by creating and returning a
    new token
    with the same properties as the original one, specified by the `tokenID` path parameter.
    The new token's expiry date is based on the original one extended by the value specified in the
    `lifetime` query parameter.
    The original token's permissions are copied verbatim.

    Args:
        token_id (UUID):
        lifetime (PostAccountTokensTokenIDRotateLifetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret | PostAccountTokensTokenIDRotateResponse403 | PostAccountTokensTokenIDRotateResponse422 | PostAccountTokensTokenIDRotateResponse500
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        lifetime=lifetime,
    ).parsed


async def asyncio_detailed(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    lifetime: PostAccountTokensTokenIDRotateLifetime | Unset = UNSET,
) -> Response[
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
]:
    """Rotate an existing organizational API token

     Rotates a non-expired organizational API token for the given token ID by creating and returning a
    new token
    with the same properties as the original one, specified by the `tokenID` path parameter.
    The new token's expiry date is based on the original one extended by the value specified in the
    `lifetime` query parameter.
    The original token's permissions are copied verbatim.

    Args:
        token_id (UUID):
        lifetime (PostAccountTokensTokenIDRotateLifetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret | PostAccountTokensTokenIDRotateResponse403 | PostAccountTokensTokenIDRotateResponse422 | PostAccountTokensTokenIDRotateResponse500]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        lifetime=lifetime,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: UUID,
    *,
    client: AuthenticatedClient,
    lifetime: PostAccountTokensTokenIDRotateLifetime | Unset = UNSET,
) -> (
    Any
    | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret
    | PostAccountTokensTokenIDRotateResponse403
    | PostAccountTokensTokenIDRotateResponse422
    | PostAccountTokensTokenIDRotateResponse500
    | None
):
    """Rotate an existing organizational API token

     Rotates a non-expired organizational API token for the given token ID by creating and returning a
    new token
    with the same properties as the original one, specified by the `tokenID` path parameter.
    The new token's expiry date is based on the original one extended by the value specified in the
    `lifetime` query parameter.
    The original token's permissions are copied verbatim.

    Args:
        token_id (UUID):
        lifetime (PostAccountTokensTokenIDRotateLifetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAccountTokensTokenIDRotateOrganizationalAPITokenWithSecret | PostAccountTokensTokenIDRotateResponse403 | PostAccountTokensTokenIDRotateResponse422 | PostAccountTokensTokenIDRotateResponse500
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            lifetime=lifetime,
        )
    ).parsed
