from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule")


@_attrs_define
class PostSystemsSystemIDEvchargingSchedulesEVChargingSchedule:
    """
    Attributes:
        from_ (datetime.datetime): Specifies when the schedule should start in RFC3339 format.
             Example: 2021-11-04T00:00:00Z.
        to (datetime.datetime): Specifies when the schedule should end in RFC3339 format.
             Example: 2021-11-04T00:30:00Z.
        limit (int): The maximum amount of power in Watts that will be used for scheduling charging in the interval
            [from, to].
             Example: 75000.
        id (UUID):  Example: ec4d0c89-a604-49ac-82f0-427f9cb42204.
        updated_at (datetime.datetime | Unset): Specifies when the schedule was updated the last time.
    """

    from_: datetime.datetime
    to: datetime.datetime
    limit: int
    id: UUID
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        limit = self.limit

        id = str(self.id)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "limit": limit,
                "id": id,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        limit = d.pop("limit")

        id = UUID(d.pop("id"))

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        post_systems_system_id_evcharging_schedules_ev_charging_schedule = cls(
            from_=from_,
            to=to,
            limit=limit,
            id=id,
            updated_at=updated_at,
        )

        post_systems_system_id_evcharging_schedules_ev_charging_schedule.additional_properties = d
        return post_systems_system_id_evcharging_schedules_ev_charging_schedule

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
