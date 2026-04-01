from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.connection_status_status import ConnectionStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionStatus")


@_attrs_define
class ConnectionStatus:
    """
    Attributes:
        status (ConnectionStatusStatus): Indicates the connection status. Is one of:
              * `AVAILABLE`: Gateway/Appliance has sent data in the last two minutes
              * `TEMPORARILY_UNAVAILABLE`: Gateway/Appliance has not sent data in the last two minutes
              * `UNAVAILABLE`: Gateway/Appliance has not sent data in the last 24 hours
        contacted_at (datetime.datetime | Unset): When the gateway/appliance has last contacted the gridX cloud.
    """

    status: ConnectionStatusStatus
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
        status = ConnectionStatusStatus(d.pop("status"))

        _contacted_at = d.pop("contactedAt", UNSET)
        contacted_at: datetime.datetime | Unset
        if isinstance(_contacted_at, Unset):
            contacted_at = UNSET
        else:
            contacted_at = isoparse(_contacted_at)

        connection_status = cls(
            status=status,
            contacted_at=contacted_at,
        )

        connection_status.additional_properties = d
        return connection_status

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
