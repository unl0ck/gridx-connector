from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_systems_system_id_power_limit_schedules_schedule_id_response_200_status import (
    GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Status,
)

if TYPE_CHECKING:
    from ..models.get_systems_system_id_power_limit_schedules_schedule_id_response_200_recurrence import (
        GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Recurrence,
    )
    from ..models.get_systems_system_id_power_limit_schedules_schedule_id_response_200_timeframes_item import (
        GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200TimeframesItem,
    )


T = TypeVar("T", bound="GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200")


@_attrs_define
class GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200:
    """
    Attributes:
        title (str): Name of this schedule. Must be unique for this system.
        from_ (datetime.datetime): From when the schedule applies (inclusive).
        to (datetime.datetime): Until when the schedule applies (exclusive).
        timezone (str): Fully qualified identifier of the timezone ([IANA timezone database
            identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) this schedule should be applied in.
            Used to determine time of day of the timeframes.
        timeframes (list[GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200TimeframesItem]): List of timeframes
            containing which import limit should be applied at which time of the day.

            They must not overlap in this schedule and also not with timeframes of other schedules of this system.
        recurrence (GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Recurrence): Recurrence rules for this
            schedule.

            Inspired by [RFC5545](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) and supporting a small subset of
            it.
        id (UUID): Unique ID of this schedule.
        status (GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Status): Status of the schedule.

            - `ACTIVE`: A timeframe of this schedule is currently being applied.
            - `OUTDATED`: No more timeframes from this schedule will be applied.
            - `UPCOMING`: A timeframe of this schedule will be applied in the future.
        created_at (datetime.datetime): When the Power Limit Schedule was created.
        updated_at (datetime.datetime): When the Power Limit Schedule was last updated.
    """

    title: str
    from_: datetime.datetime
    to: datetime.datetime
    timezone: str
    timeframes: list[GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200TimeframesItem]
    recurrence: GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Recurrence
    id: UUID
    status: GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Status
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        timezone = self.timezone

        timeframes = []
        for timeframes_item_data in self.timeframes:
            timeframes_item = timeframes_item_data.to_dict()
            timeframes.append(timeframes_item)

        recurrence = self.recurrence.to_dict()

        id = str(self.id)

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "from": from_,
                "to": to,
                "timezone": timezone,
                "timeframes": timeframes,
                "recurrence": recurrence,
                "id": id,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_power_limit_schedules_schedule_id_response_200_recurrence import (
            GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Recurrence,
        )
        from ..models.get_systems_system_id_power_limit_schedules_schedule_id_response_200_timeframes_item import (
            GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200TimeframesItem,
        )

        d = dict(src_dict)
        title = d.pop("title")

        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        timezone = d.pop("timezone")

        timeframes = []
        _timeframes = d.pop("timeframes")
        for timeframes_item_data in _timeframes:
            timeframes_item = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200TimeframesItem.from_dict(
                timeframes_item_data
            )

            timeframes.append(timeframes_item)

        recurrence = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Recurrence.from_dict(d.pop("recurrence"))

        id = UUID(d.pop("id"))

        status = GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Status(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        get_systems_system_id_power_limit_schedules_schedule_id_response_200 = cls(
            title=title,
            from_=from_,
            to=to,
            timezone=timezone,
            timeframes=timeframes,
            recurrence=recurrence,
            id=id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_systems_system_id_power_limit_schedules_schedule_id_response_200.additional_properties = d
        return get_systems_system_id_power_limit_schedules_schedule_id_response_200

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
