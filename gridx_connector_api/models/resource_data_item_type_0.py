from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.resource_data_item_type_0_state import ResourceDataItemType0State
from ..models.resource_data_item_type_0_value_source import ResourceDataItemType0ValueSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_data_item_type_0_power_time_slots_item import ResourceDataItemType0PowerTimeSlotsItem


T = TypeVar("T", bound="ResourceDataItemType0")


@_attrs_define
class ResourceDataItemType0:
    """
    Attributes:
        earliest_start_time (datetime.datetime): See EEBUS FSWG-022. Example: 2021-06-24T06:20:00Z.
        latest_end_time (datetime.datetime): See EEBUS FSWG-023. Example: 2021-06-24T19:00:00Z.
        power_time_slots (list[ResourceDataItemType0PowerTimeSlotsItem]): List of power time slots for a power sequence.
            See EEBUS FSWG-060.
        sequence_id (int | Unset): Identifier of power sequence, must be unique in path. Example: 1.
        state (ResourceDataItemType0State | Unset): EEBUS FSWG-025. See section 3.2.1.2.2.1.1.4 Example: scheduled.
        active_slot_number (int | Unset): The currently active powerTimeSlot, if state is inactive, schedule, completed
            or invalid, activeSlotNumber is 0.
        sequence_remote_controllable (bool | Unset):
        start_time (datetime.datetime | Unset): See EEBUS FSWG-04. Example: 2021-06-24T12:00:00Z.
        end_time (datetime.datetime | Unset): Must be greater than "alternatives. powerSequence. schedule. startTime"
            Example: 2021-06-24T13:40:00Z.
        is_pausable (bool | Unset): If the sequence can be paused by the CEM, this element SHALL be present and set to
            true. Otherwise it SHALL be omitted or set to false (default value).
            For more details, see EEBUS FSWG-026S.
             Default: False.
        is_stoppable (bool | Unset): If the sequence can be stopped by the CEM, this element SHALL be present and set to
            true. Otherwise it SHALL be omitted or set to false (default value).
            For more details, see EEBUS FSWG-027.
             Default: False.
        value_source (ResourceDataItemType0ValueSource | Unset): If not set, the source of forecasted values is
            undefined.
        task_identifier (int | Unset): Identifier of the task.
    """

    earliest_start_time: datetime.datetime
    latest_end_time: datetime.datetime
    power_time_slots: list[ResourceDataItemType0PowerTimeSlotsItem]
    sequence_id: int | Unset = UNSET
    state: ResourceDataItemType0State | Unset = UNSET
    active_slot_number: int | Unset = UNSET
    sequence_remote_controllable: bool | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    is_pausable: bool | Unset = False
    is_stoppable: bool | Unset = False
    value_source: ResourceDataItemType0ValueSource | Unset = UNSET
    task_identifier: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        earliest_start_time = self.earliest_start_time.isoformat()

        latest_end_time = self.latest_end_time.isoformat()

        power_time_slots = []
        for power_time_slots_item_data in self.power_time_slots:
            power_time_slots_item = power_time_slots_item_data.to_dict()
            power_time_slots.append(power_time_slots_item)

        sequence_id = self.sequence_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        active_slot_number = self.active_slot_number

        sequence_remote_controllable = self.sequence_remote_controllable

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        is_pausable = self.is_pausable

        is_stoppable = self.is_stoppable

        value_source: str | Unset = UNSET
        if not isinstance(self.value_source, Unset):
            value_source = self.value_source.value

        task_identifier = self.task_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "earliestStartTime": earliest_start_time,
                "latestEndTime": latest_end_time,
                "powerTimeSlots": power_time_slots,
            }
        )
        if sequence_id is not UNSET:
            field_dict["sequenceId"] = sequence_id
        if state is not UNSET:
            field_dict["state"] = state
        if active_slot_number is not UNSET:
            field_dict["activeSlotNumber"] = active_slot_number
        if sequence_remote_controllable is not UNSET:
            field_dict["sequenceRemoteControllable"] = sequence_remote_controllable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if is_pausable is not UNSET:
            field_dict["isPausable"] = is_pausable
        if is_stoppable is not UNSET:
            field_dict["isStoppable"] = is_stoppable
        if value_source is not UNSET:
            field_dict["valueSource"] = value_source
        if task_identifier is not UNSET:
            field_dict["taskIdentifier"] = task_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_data_item_type_0_power_time_slots_item import ResourceDataItemType0PowerTimeSlotsItem

        d = dict(src_dict)
        earliest_start_time = isoparse(d.pop("earliestStartTime"))

        latest_end_time = isoparse(d.pop("latestEndTime"))

        power_time_slots = []
        _power_time_slots = d.pop("powerTimeSlots")
        for power_time_slots_item_data in _power_time_slots:
            power_time_slots_item = ResourceDataItemType0PowerTimeSlotsItem.from_dict(power_time_slots_item_data)

            power_time_slots.append(power_time_slots_item)

        sequence_id = d.pop("sequenceId", UNSET)

        _state = d.pop("state", UNSET)
        state: ResourceDataItemType0State | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ResourceDataItemType0State(_state)

        active_slot_number = d.pop("activeSlotNumber", UNSET)

        sequence_remote_controllable = d.pop("sequenceRemoteControllable", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        is_pausable = d.pop("isPausable", UNSET)

        is_stoppable = d.pop("isStoppable", UNSET)

        _value_source = d.pop("valueSource", UNSET)
        value_source: ResourceDataItemType0ValueSource | Unset
        if isinstance(_value_source, Unset):
            value_source = UNSET
        else:
            value_source = ResourceDataItemType0ValueSource(_value_source)

        task_identifier = d.pop("taskIdentifier", UNSET)

        resource_data_item_type_0 = cls(
            earliest_start_time=earliest_start_time,
            latest_end_time=latest_end_time,
            power_time_slots=power_time_slots,
            sequence_id=sequence_id,
            state=state,
            active_slot_number=active_slot_number,
            sequence_remote_controllable=sequence_remote_controllable,
            start_time=start_time,
            end_time=end_time,
            is_pausable=is_pausable,
            is_stoppable=is_stoppable,
            value_source=value_source,
            task_identifier=task_identifier,
        )

        resource_data_item_type_0.additional_properties = d
        return resource_data_item_type_0

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
