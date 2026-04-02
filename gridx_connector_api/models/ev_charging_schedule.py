from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EVChargingSchedule")


@_attrs_define
class EVChargingSchedule:
    """An Electric Vehicle charging schedule represents an interval in which
    the electric vehicle is supposed to charge at a defined limit.

        Attributes:
            from_ (datetime.datetime | Unset): Specifies when the schedule should start in RFC3339 format.
                 Example: 2021-11-04T00:00:00Z.
            to (datetime.datetime | Unset): Specifies when the schedule should end in RFC3339 format.
                 Example: 2021-11-04T00:30:00Z.
            limit (int | Unset): The maximum amount of power in Watts that will be used for scheduling charging in the
                interval [from, to].
                 Example: 75000.
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        limit = d.pop("limit", UNSET)

        ev_charging_schedule = cls(
            from_=from_,
            to=to,
            limit=limit,
        )

        ev_charging_schedule.additional_properties = d
        return ev_charging_schedule

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
