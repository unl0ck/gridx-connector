from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.power_sequence_update_state import PowerSequenceUpdateState
from ..models.power_sequence_update_value_source import PowerSequenceUpdateValueSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.power_sequence_update_power_time_slots_item import PowerSequenceUpdatePowerTimeSlotsItem


T = TypeVar("T", bound="PowerSequenceUpdate")


@_attrs_define
class PowerSequenceUpdate:
    """
    Attributes:
        sequence_id (int | Unset): Identifier of power sequence, must be unique in path. Example: 1.
        state (PowerSequenceUpdateState | Unset): EEBUS FSWG-025. See section 3.2.1.2.2.1.1.4 Example: scheduled.
        active_slot_number (int | Unset): The currently active powerTimeSlot, if state is inactive, schedule, completed
            or invalid, activeSlotNumber is 0.
        sequence_remote_controllable (bool | Unset):
        start_time (datetime.datetime | Unset): See EEBUS FSWG-04. Example: 2021-06-24T12:00:00Z.
        end_time (datetime.datetime | Unset): Must be greater than "alternatives. powerSequence. schedule. startTime"
            Example: 2021-06-24T13:40:00Z.
        earliest_start_time (datetime.datetime | Unset): See EEBUS FSWG-022. Example: 2021-06-24T06:20:00Z.
        latest_end_time (datetime.datetime | Unset): See EEBUS FSWG-023. Example: 2021-06-24T19:00:00Z.
        is_pausable (bool | Unset): If the sequence can be paused by the CEM, this element SHALL be present and set to
            true. Otherwise it SHALL be omitted or set to false (default value).
            For more details, see EEBUS FSWG-026S.
             Default: False.
        is_stoppable (bool | Unset): If the sequence can be stopped by the CEM, this element SHALL be present and set to
            true. Otherwise it SHALL be omitted or set to false (default value).
            For more details, see EEBUS FSWG-027.
             Default: False.
        value_source (PowerSequenceUpdateValueSource | Unset): If not set, the source of forecasted values is undefined.
        task_identifier (int | Unset): Identifier of the task.
        power_time_slots (list[PowerSequenceUpdatePowerTimeSlotsItem] | Unset): List of power time slots for a power
            sequence. See EEBUS FSWG-060.
    """

    sequence_id: int | Unset = UNSET
    state: PowerSequenceUpdateState | Unset = UNSET
    active_slot_number: int | Unset = UNSET
    sequence_remote_controllable: bool | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    earliest_start_time: datetime.datetime | Unset = UNSET
    latest_end_time: datetime.datetime | Unset = UNSET
    is_pausable: bool | Unset = False
    is_stoppable: bool | Unset = False
    value_source: PowerSequenceUpdateValueSource | Unset = UNSET
    task_identifier: int | Unset = UNSET
    power_time_slots: list[PowerSequenceUpdatePowerTimeSlotsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        earliest_start_time: str | Unset = UNSET
        if not isinstance(self.earliest_start_time, Unset):
            earliest_start_time = self.earliest_start_time.isoformat()

        latest_end_time: str | Unset = UNSET
        if not isinstance(self.latest_end_time, Unset):
            latest_end_time = self.latest_end_time.isoformat()

        is_pausable = self.is_pausable

        is_stoppable = self.is_stoppable

        value_source: str | Unset = UNSET
        if not isinstance(self.value_source, Unset):
            value_source = self.value_source.value

        task_identifier = self.task_identifier

        power_time_slots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.power_time_slots, Unset):
            power_time_slots = []
            for power_time_slots_item_data in self.power_time_slots:
                power_time_slots_item = power_time_slots_item_data.to_dict()
                power_time_slots.append(power_time_slots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if earliest_start_time is not UNSET:
            field_dict["earliestStartTime"] = earliest_start_time
        if latest_end_time is not UNSET:
            field_dict["latestEndTime"] = latest_end_time
        if is_pausable is not UNSET:
            field_dict["isPausable"] = is_pausable
        if is_stoppable is not UNSET:
            field_dict["isStoppable"] = is_stoppable
        if value_source is not UNSET:
            field_dict["valueSource"] = value_source
        if task_identifier is not UNSET:
            field_dict["taskIdentifier"] = task_identifier
        if power_time_slots is not UNSET:
            field_dict["powerTimeSlots"] = power_time_slots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.power_sequence_update_power_time_slots_item import PowerSequenceUpdatePowerTimeSlotsItem

        d = dict(src_dict)
        sequence_id = d.pop("sequenceId", UNSET)

        _state = d.pop("state", UNSET)
        state: PowerSequenceUpdateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PowerSequenceUpdateState(_state)

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

        _earliest_start_time = d.pop("earliestStartTime", UNSET)
        earliest_start_time: datetime.datetime | Unset
        if isinstance(_earliest_start_time, Unset):
            earliest_start_time = UNSET
        else:
            earliest_start_time = isoparse(_earliest_start_time)

        _latest_end_time = d.pop("latestEndTime", UNSET)
        latest_end_time: datetime.datetime | Unset
        if isinstance(_latest_end_time, Unset):
            latest_end_time = UNSET
        else:
            latest_end_time = isoparse(_latest_end_time)

        is_pausable = d.pop("isPausable", UNSET)

        is_stoppable = d.pop("isStoppable", UNSET)

        _value_source = d.pop("valueSource", UNSET)
        value_source: PowerSequenceUpdateValueSource | Unset
        if isinstance(_value_source, Unset):
            value_source = UNSET
        else:
            value_source = PowerSequenceUpdateValueSource(_value_source)

        task_identifier = d.pop("taskIdentifier", UNSET)

        _power_time_slots = d.pop("powerTimeSlots", UNSET)
        power_time_slots: list[PowerSequenceUpdatePowerTimeSlotsItem] | Unset = UNSET
        if _power_time_slots is not UNSET:
            power_time_slots = []
            for power_time_slots_item_data in _power_time_slots:
                power_time_slots_item = PowerSequenceUpdatePowerTimeSlotsItem.from_dict(power_time_slots_item_data)

                power_time_slots.append(power_time_slots_item)

        power_sequence_update = cls(
            sequence_id=sequence_id,
            state=state,
            active_slot_number=active_slot_number,
            sequence_remote_controllable=sequence_remote_controllable,
            start_time=start_time,
            end_time=end_time,
            earliest_start_time=earliest_start_time,
            latest_end_time=latest_end_time,
            is_pausable=is_pausable,
            is_stoppable=is_stoppable,
            value_source=value_source,
            task_identifier=task_identifier,
            power_time_slots=power_time_slots,
        )

        power_sequence_update.additional_properties = d
        return power_sequence_update

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
