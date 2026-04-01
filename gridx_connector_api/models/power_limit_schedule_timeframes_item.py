from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PowerLimitScheduleTimeframesItem")


@_attrs_define
class PowerLimitScheduleTimeframesItem:
    """
    Attributes:
        from_ (str): Time of day from when the limit of this timeframe should be applied (inclusive).
             Example: 00:00.
        to (str): Time of day until when the limit of this timeframe should be applied (exclusive).
             Example: 14:00.
        max_power (int): Max import power in Watt to apply to the grid meter during this timeframe. Example: 100000.
    """

    from_: str
    to: str
    max_power: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        max_power = self.max_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "maxPower": max_power,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        max_power = d.pop("maxPower")

        power_limit_schedule_timeframes_item = cls(
            from_=from_,
            to=to,
            max_power=max_power,
        )

        power_limit_schedule_timeframes_item.additional_properties = d
        return power_limit_schedule_timeframes_item

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
