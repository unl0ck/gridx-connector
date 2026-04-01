from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicesAdditionalPropertyItemResourcesItemDataItemType0PowerTimeSlotsItem")


@_attrs_define
class DevicesAdditionalPropertyItemResourcesItemDataItemType0PowerTimeSlotsItem:
    """
    Attributes:
        slot_id (int | Unset): A SUB IDENTIFIER within powerSequence. The slot IDs within one power sequence shall be
            assigned according to the chronological order of the slots. Example: 1.
        default_duration (str | Unset): See EEBUS FSWG-063. Example: 00:23:00.
        power_min (float | Unset): See EEBUS FSWG-062. Example: 100.
        power_expected_value (float | Unset): See EEBUS FSWG-062. Example: 200.
        power_max (float | Unset): See EEBUS FSWG-062. Example: 1000.
    """

    slot_id: int | Unset = UNSET
    default_duration: str | Unset = UNSET
    power_min: float | Unset = UNSET
    power_expected_value: float | Unset = UNSET
    power_max: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot_id = self.slot_id

        default_duration = self.default_duration

        power_min = self.power_min

        power_expected_value = self.power_expected_value

        power_max = self.power_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slot_id is not UNSET:
            field_dict["slotId"] = slot_id
        if default_duration is not UNSET:
            field_dict["defaultDuration"] = default_duration
        if power_min is not UNSET:
            field_dict["powerMin"] = power_min
        if power_expected_value is not UNSET:
            field_dict["powerExpectedValue"] = power_expected_value
        if power_max is not UNSET:
            field_dict["powerMax"] = power_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slot_id = d.pop("slotId", UNSET)

        default_duration = d.pop("defaultDuration", UNSET)

        power_min = d.pop("powerMin", UNSET)

        power_expected_value = d.pop("powerExpectedValue", UNSET)

        power_max = d.pop("powerMax", UNSET)

        devices_additional_property_item_resources_item_data_item_type_0_power_time_slots_item = cls(
            slot_id=slot_id,
            default_duration=default_duration,
            power_min=power_min,
            power_expected_value=power_expected_value,
            power_max=power_max,
        )

        devices_additional_property_item_resources_item_data_item_type_0_power_time_slots_item.additional_properties = d
        return devices_additional_property_item_resources_item_data_item_type_0_power_time_slots_item

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
