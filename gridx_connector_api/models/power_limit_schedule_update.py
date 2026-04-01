from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.power_limit_schedule_update_recurrence import PowerLimitScheduleUpdateRecurrence
    from ..models.power_limit_schedule_update_timeframes_item import PowerLimitScheduleUpdateTimeframesItem


T = TypeVar("T", bound="PowerLimitScheduleUpdate")


@_attrs_define
class PowerLimitScheduleUpdate:
    """
    Attributes:
        title (str | Unset): Name of this schedule. Must be unique for this system.
        from_ (datetime.datetime | Unset): From when the schedule applies (inclusive).
        to (datetime.datetime | Unset): Until when the schedule applies (exclusive).
        timezone (str | Unset): Fully qualified identifier of the timezone ([IANA timezone database
            identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) this schedule should be applied in.
            Used to determine time of day of the timeframes.
        timeframes (list[PowerLimitScheduleUpdateTimeframesItem] | Unset): List of timeframes containing which import
            limit should be applied at which time of the day.

            They must not overlap in this schedule and also not with timeframes of other schedules of this system.
        recurrence (PowerLimitScheduleUpdateRecurrence | Unset): Recurrence rules for this schedule.

            Inspired by [RFC5545](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) and supporting a small subset of
            it.
    """

    title: str | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    timezone: str | Unset = UNSET
    timeframes: list[PowerLimitScheduleUpdateTimeframesItem] | Unset = UNSET
    recurrence: PowerLimitScheduleUpdateRecurrence | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        timezone = self.timezone

        timeframes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeframes, Unset):
            timeframes = []
            for timeframes_item_data in self.timeframes:
                timeframes_item = timeframes_item_data.to_dict()
                timeframes.append(timeframes_item)

        recurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.power_limit_schedule_update_recurrence import PowerLimitScheduleUpdateRecurrence
        from ..models.power_limit_schedule_update_timeframes_item import PowerLimitScheduleUpdateTimeframesItem

        d = dict(src_dict)
        title = d.pop("title", UNSET)

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

        timezone = d.pop("timezone", UNSET)

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: list[PowerLimitScheduleUpdateTimeframesItem] | Unset = UNSET
        if _timeframes is not UNSET:
            timeframes = []
            for timeframes_item_data in _timeframes:
                timeframes_item = PowerLimitScheduleUpdateTimeframesItem.from_dict(timeframes_item_data)

                timeframes.append(timeframes_item)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: PowerLimitScheduleUpdateRecurrence | Unset
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = PowerLimitScheduleUpdateRecurrence.from_dict(_recurrence)

        power_limit_schedule_update = cls(
            title=title,
            from_=from_,
            to=to,
            timezone=timezone,
            timeframes=timeframes,
            recurrence=recurrence,
        )

        power_limit_schedule_update.additional_properties = d
        return power_limit_schedule_update

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
