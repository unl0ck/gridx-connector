from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_body import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_201 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_400 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_403 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_404 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_422 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422,
)
from ...models.patch_spine_devices_device_id_powersequences_sequence_id_response_500 import (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    device_id: str,
    sequence_id: int,
    *,
    body: PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/spine/devices/{device_id}/powersequences/{sequence_id}".format(
            device_id=quote(str(device_id), safe=""),
            sequence_id=quote(str(sequence_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: str,
    sequence_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset = UNSET,
) -> Response[
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
]:
    """Change a specific power sequence for a specific device.

     A PATCH may be performed on startTime and endTime of an existing power sequence.
    If only one parameter is specified, the other is calculated from the accumulated duration of all
    power time slots for this sequence.
    A device binding is needed before changing the power sequence. If a binding doesn't exist, it is
    first created and then the power sequence is updated.

    Args:
        device_id (str):
        sequence_id (int):
        body (PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        sequence_id=sequence_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device_id: str,
    sequence_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset = UNSET,
) -> (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
    | None
):
    """Change a specific power sequence for a specific device.

     A PATCH may be performed on startTime and endTime of an existing power sequence.
    If only one parameter is specified, the other is calculated from the accumulated duration of all
    power time slots for this sequence.
    A device binding is needed before changing the power sequence. If a binding doesn't exist, it is
    first created and then the power sequence is updated.

    Args:
        device_id (str):
        sequence_id (int):
        body (PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
    """

    return sync_detailed(
        device_id=device_id,
        sequence_id=sequence_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    sequence_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset = UNSET,
) -> Response[
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
]:
    """Change a specific power sequence for a specific device.

     A PATCH may be performed on startTime and endTime of an existing power sequence.
    If only one parameter is specified, the other is calculated from the accumulated duration of all
    power time slots for this sequence.
    A device binding is needed before changing the power sequence. If a binding doesn't exist, it is
    first created and then the power sequence is updated.

    Args:
        device_id (str):
        sequence_id (int):
        body (PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        sequence_id=sequence_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id: str,
    sequence_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset = UNSET,
) -> (
    PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422
    | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
    | None
):
    """Change a specific power sequence for a specific device.

     A PATCH may be performed on startTime and endTime of an existing power sequence.
    If only one parameter is specified, the other is calculated from the accumulated duration of all
    power time slots for this sequence.
    A device binding is needed before changing the power sequence. If a binding doesn't exist, it is
    first created and then the power sequence is updated.

    Args:
        device_id (str):
        sequence_id (int):
        body (PatchSpineDevicesDeviceIDPowersequencesSequenceIDBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse201 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse400 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse403 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse404 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse422 | PatchSpineDevicesDeviceIDPowersequencesSequenceIDResponse500
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            sequence_id=sequence_id,
            client=client,
            body=body,
        )
    ).parsed
