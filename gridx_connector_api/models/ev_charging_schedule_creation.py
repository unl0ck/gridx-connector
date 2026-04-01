from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EVChargingScheduleCreation")


@_attrs_define
class EVChargingScheduleCreation:
    """
    Attributes:
        from_ (datetime.datetime): Specifies when the schedule should start in RFC3339 format.
             Example: 2021-11-04T00:00:00Z.
        to (datetime.datetime): Specifies when the schedule should end in RFC3339 format.
             Example: 2021-11-04T00:30:00Z.
        limit (int): The maximum amount of power in Watts that will be used for scheduling charging in the interval
            [from, to].
             Example: 75000.
    """

    from_: datetime.datetime
    to: datetime.datetime
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        limit = d.pop("limit")

        ev_charging_schedule_creation = cls(
            from_=from_,
            to=to,
            limit=limit,
        )

        ev_charging_schedule_creation.additional_properties = d
        return ev_charging_schedule_creation

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
