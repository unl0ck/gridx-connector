from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.systems_ams_systems_item_gateway_status import SystemsAMSSystemsItemGatewayStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.systems_ams_systems_item_location import SystemsAMSSystemsItemLocation


T = TypeVar("T", bound="SystemsAMSSystemsItem")


@_attrs_define
class SystemsAMSSystemsItem:
    """A single System with or without a list of its assets.

    Attributes:
        name (str):  Example: Example System Name.
        gateway_sn (str):  Example: G243-050-000-000-436-P-X.
        location (SystemsAMSSystemsItemLocation): The Location where the System is located at. The first time it is
            created and on any subsequent updates, the
            coordinates are looked up and persisted, so that on subsequent retrievals, those fields should be present.
            However, a System is considered valid even without a location, so failure to retrieve the coordinates won't
            result in an error when creating or updating a system.
        id (UUID | Unset):  Example: 92a76811-d3ff-4ec2-9d4f-cd92c4e540ea.
        gateway_status (SystemsAMSSystemsItemGatewayStatus | Unset):
        heartbeat_expiry (datetime.datetime | Unset): Heartbeat Expiry is deprecated. It has been replaced by a `status`
            field and a `lastHeartbeatReceivedAt`
            field.
        last_heartbeat_received_at (datetime.datetime | None | Unset): At what time the last heartbeat was received from
            the gridBox (gateway) that is part of this system.
        registered_at (datetime.datetime | None | Unset): Indicates the time the system was first registered in gridX.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    name: str
    gateway_sn: str
    location: SystemsAMSSystemsItemLocation
    id: UUID | Unset = UNSET
    gateway_status: SystemsAMSSystemsItemGatewayStatus | Unset = UNSET
    heartbeat_expiry: datetime.datetime | Unset = UNSET
    last_heartbeat_received_at: datetime.datetime | None | Unset = UNSET
    registered_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        gateway_sn = self.gateway_sn

        location = self.location.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        gateway_status: str | Unset = UNSET
        if not isinstance(self.gateway_status, Unset):
            gateway_status = self.gateway_status.value

        heartbeat_expiry: str | Unset = UNSET
        if not isinstance(self.heartbeat_expiry, Unset):
            heartbeat_expiry = self.heartbeat_expiry.isoformat()

        last_heartbeat_received_at: None | str | Unset
        if isinstance(self.last_heartbeat_received_at, Unset):
            last_heartbeat_received_at = UNSET
        elif isinstance(self.last_heartbeat_received_at, datetime.datetime):
            last_heartbeat_received_at = self.last_heartbeat_received_at.isoformat()
        else:
            last_heartbeat_received_at = self.last_heartbeat_received_at

        registered_at: None | str | Unset
        if isinstance(self.registered_at, Unset):
            registered_at = UNSET
        elif isinstance(self.registered_at, datetime.datetime):
            registered_at = self.registered_at.isoformat()
        else:
            registered_at = self.registered_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "gatewaySN": gateway_sn,
                "location": location,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if gateway_status is not UNSET:
            field_dict["gatewayStatus"] = gateway_status
        if heartbeat_expiry is not UNSET:
            field_dict["heartbeatExpiry"] = heartbeat_expiry
        if last_heartbeat_received_at is not UNSET:
            field_dict["lastHeartbeatReceivedAt"] = last_heartbeat_received_at
        if registered_at is not UNSET:
            field_dict["registeredAt"] = registered_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.systems_ams_systems_item_location import SystemsAMSSystemsItemLocation

        d = dict(src_dict)
        name = d.pop("name")

        gateway_sn = d.pop("gatewaySN")

        location = SystemsAMSSystemsItemLocation.from_dict(d.pop("location"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _gateway_status = d.pop("gatewayStatus", UNSET)
        gateway_status: SystemsAMSSystemsItemGatewayStatus | Unset
        if isinstance(_gateway_status, Unset):
            gateway_status = UNSET
        else:
            gateway_status = SystemsAMSSystemsItemGatewayStatus(_gateway_status)

        _heartbeat_expiry = d.pop("heartbeatExpiry", UNSET)
        heartbeat_expiry: datetime.datetime | Unset
        if isinstance(_heartbeat_expiry, Unset):
            heartbeat_expiry = UNSET
        else:
            heartbeat_expiry = isoparse(_heartbeat_expiry)

        def _parse_last_heartbeat_received_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_heartbeat_received_at_type_0 = isoparse(data)

                return last_heartbeat_received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_heartbeat_received_at = _parse_last_heartbeat_received_at(d.pop("lastHeartbeatReceivedAt", UNSET))

        def _parse_registered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_at_type_0 = isoparse(data)

                return registered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        registered_at = _parse_registered_at(d.pop("registeredAt", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        systems_ams_systems_item = cls(
            name=name,
            gateway_sn=gateway_sn,
            location=location,
            id=id,
            gateway_status=gateway_status,
            heartbeat_expiry=heartbeat_expiry,
            last_heartbeat_received_at=last_heartbeat_received_at,
            registered_at=registered_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        systems_ams_systems_item.additional_properties = d
        return systems_ams_systems_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
