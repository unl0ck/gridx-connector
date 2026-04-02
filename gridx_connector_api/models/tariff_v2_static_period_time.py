from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TariffV2StaticPeriodTime")


@_attrs_define
class TariffV2StaticPeriodTime:
    """Contains the information when a static period of a TariffV2 starts or ends.
    Described by the weekday and the seconds of this day.

        Attributes:
            weekday (int): The weekdays index (Sunday=0, ...)
            seconds_of_day (int): The second of the weekday until the period is valid/which the period is valid from
    """

    weekday: int
    seconds_of_day: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekday = self.weekday

        seconds_of_day = self.seconds_of_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekday": weekday,
                "secondsOfDay": seconds_of_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weekday = d.pop("weekday")

        seconds_of_day = d.pop("secondsOfDay")

        tariff_v2_static_period_time = cls(
            weekday=weekday,
            seconds_of_day=seconds_of_day,
        )

        tariff_v2_static_period_time.additional_properties = d
        return tariff_v2_static_period_time

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
