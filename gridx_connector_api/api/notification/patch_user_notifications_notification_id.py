from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_user_notifications_notification_id_body import PatchUserNotificationsNotificationIDBody
from ...models.patch_user_notifications_notification_id_notification import (
    PatchUserNotificationsNotificationIDNotification,
)
from ...models.patch_user_notifications_notification_id_response_400 import (
    PatchUserNotificationsNotificationIDResponse400,
)
from ...models.patch_user_notifications_notification_id_response_403 import (
    PatchUserNotificationsNotificationIDResponse403,
)
from ...models.patch_user_notifications_notification_id_response_404 import (
    PatchUserNotificationsNotificationIDResponse404,
)
from ...types import Response


def _get_kwargs(
    notification_id: UUID,
    *,
    body: PatchUserNotificationsNotificationIDBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/user/notifications/{notification_id}".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PatchUserNotificationsNotificationIDNotification.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchUserNotificationsNotificationIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchUserNotificationsNotificationIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchUserNotificationsNotificationIDResponse404.from_dict(response.json())

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
) -> Response[
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchUserNotificationsNotificationIDBody,
) -> Response[
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
]:
    """Update a Notification

     Updates a dashboard notification of the authenticated user.

    Args:
        notification_id (UUID):
        body (PatchUserNotificationsNotificationIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchUserNotificationsNotificationIDNotification | PatchUserNotificationsNotificationIDResponse400 | PatchUserNotificationsNotificationIDResponse403 | PatchUserNotificationsNotificationIDResponse404]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchUserNotificationsNotificationIDBody,
) -> (
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
    | None
):
    """Update a Notification

     Updates a dashboard notification of the authenticated user.

    Args:
        notification_id (UUID):
        body (PatchUserNotificationsNotificationIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchUserNotificationsNotificationIDNotification | PatchUserNotificationsNotificationIDResponse400 | PatchUserNotificationsNotificationIDResponse403 | PatchUserNotificationsNotificationIDResponse404
    """

    return sync_detailed(
        notification_id=notification_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchUserNotificationsNotificationIDBody,
) -> Response[
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
]:
    """Update a Notification

     Updates a dashboard notification of the authenticated user.

    Args:
        notification_id (UUID):
        body (PatchUserNotificationsNotificationIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchUserNotificationsNotificationIDNotification | PatchUserNotificationsNotificationIDResponse400 | PatchUserNotificationsNotificationIDResponse403 | PatchUserNotificationsNotificationIDResponse404]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchUserNotificationsNotificationIDBody,
) -> (
    Any
    | PatchUserNotificationsNotificationIDNotification
    | PatchUserNotificationsNotificationIDResponse400
    | PatchUserNotificationsNotificationIDResponse403
    | PatchUserNotificationsNotificationIDResponse404
    | None
):
    """Update a Notification

     Updates a dashboard notification of the authenticated user.

    Args:
        notification_id (UUID):
        body (PatchUserNotificationsNotificationIDBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchUserNotificationsNotificationIDNotification | PatchUserNotificationsNotificationIDResponse400 | PatchUserNotificationsNotificationIDResponse403 | PatchUserNotificationsNotificationIDResponse404
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
            body=body,
        )
    ).parsed
