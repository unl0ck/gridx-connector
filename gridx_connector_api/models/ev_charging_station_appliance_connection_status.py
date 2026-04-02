from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ev_charging_station_appliance_connection_status_status import (
    EVChargingStationApplianceConnectionStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EVChargingStationApplianceConnectionStatus")


@_attrs_define
class EVChargingStationApplianceConnectionStatus:
    """
    Attributes:
        status (EVChargingStationApplianceConnectionStatusStatus): Indicates the connection status of an appliance.

            The connection status of an appliance is determined by the gateway. The gateway regularly
            sends the connection status of all connected appliances.

            It is one of:
            - `AVAILABLE`: Appliance was reported as available by the gateway.
            - `UNAVAILABLE`: Appliance was reported as unavailable by the gateway.
            - `UNKNOWN`: The gateway didn't report a status for the appliance.

            In case the connection status of the gateway this appliance belongs to is `TEMPORARILY_UNAVAILABLE` or
            `UNAVAILABLE`
            the status is always `UNAVAILABLE`.
        contacted_at (datetime.datetime | Unset): No longer supported.

            Will be set approximately to a value matching the status field.
            If the appliance is `AVAILABLE`, it will be the current datetime.
            If the appliance is `UNAVAILABLE`, it will be a datetime 24 hours in the past.
    """

    status: EVChargingStationApplianceConnectionStatusStatus
    contacted_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        contacted_at: str | Unset = UNSET
        if not isinstance(self.contacted_at, Unset):
            contacted_at = self.contacted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if contacted_at is not UNSET:
            field_dict["contactedAt"] = contacted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = EVChargingStationApplianceConnectionStatusStatus(d.pop("status"))

        _contacted_at = d.pop("contactedAt", UNSET)
        contacted_at: datetime.datetime | Unset
        if isinstance(_contacted_at, Unset):
            contacted_at = UNSET
        else:
            contacted_at = isoparse(_contacted_at)

        ev_charging_station_appliance_connection_status = cls(
            status=status,
            contacted_at=contacted_at,
        )

        ev_charging_station_appliance_connection_status.additional_properties = d
        return ev_charging_station_appliance_connection_status

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
