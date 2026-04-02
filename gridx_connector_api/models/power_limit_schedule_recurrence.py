from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.power_limit_schedule_recurrence_by_day_of_week_item import PowerLimitScheduleRecurrenceByDayOfWeekItem
from ..models.power_limit_schedule_recurrence_frequency import PowerLimitScheduleRecurrenceFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerLimitScheduleRecurrence")


@_attrs_define
class PowerLimitScheduleRecurrence:
    """Recurrence rules for this schedule.

    Inspired by [RFC5545](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) and supporting a small subset of it.

        Attributes:
            frequency (PowerLimitScheduleRecurrenceFrequency): Type of recurrence rule.
            by_day_of_week (list[PowerLimitScheduleRecurrenceByDayOfWeekItem] | Unset): Specifies a list of weekdays this
                rule should apply to.
                Only valid for `frequency=DAILY`.

                Omitting it is the same as selecting all days.
    """

    frequency: PowerLimitScheduleRecurrenceFrequency
    by_day_of_week: list[PowerLimitScheduleRecurrenceByDayOfWeekItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency.value

        by_day_of_week: list[str] | Unset = UNSET
        if not isinstance(self.by_day_of_week, Unset):
            by_day_of_week = []
            for by_day_of_week_item_data in self.by_day_of_week:
                by_day_of_week_item = by_day_of_week_item_data.value
                by_day_of_week.append(by_day_of_week_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
            }
        )
        if by_day_of_week is not UNSET:
            field_dict["byDayOfWeek"] = by_day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequency = PowerLimitScheduleRecurrenceFrequency(d.pop("frequency"))

        _by_day_of_week = d.pop("byDayOfWeek", UNSET)
        by_day_of_week: list[PowerLimitScheduleRecurrenceByDayOfWeekItem] | Unset = UNSET
        if _by_day_of_week is not UNSET:
            by_day_of_week = []
            for by_day_of_week_item_data in _by_day_of_week:
                by_day_of_week_item = PowerLimitScheduleRecurrenceByDayOfWeekItem(by_day_of_week_item_data)

                by_day_of_week.append(by_day_of_week_item)

        power_limit_schedule_recurrence = cls(
            frequency=frequency,
            by_day_of_week=by_day_of_week,
        )

        power_limit_schedule_recurrence.additional_properties = d
        return power_limit_schedule_recurrence

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
