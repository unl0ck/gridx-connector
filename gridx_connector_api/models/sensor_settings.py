from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SensorSettings")


@_attrs_define
class SensorSettings:
    """
    Attributes:
        sensor_l1 (int | Unset):
        sensor_l2 (int | Unset):
        sensor_l3 (int | Unset):
    """

    sensor_l1: int | Unset = UNSET
    sensor_l2: int | Unset = UNSET
    sensor_l3: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sensor_l1 = self.sensor_l1

        sensor_l2 = self.sensor_l2

        sensor_l3 = self.sensor_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sensor_l1 is not UNSET:
            field_dict["sensorL1"] = sensor_l1
        if sensor_l2 is not UNSET:
            field_dict["sensorL2"] = sensor_l2
        if sensor_l3 is not UNSET:
            field_dict["sensorL3"] = sensor_l3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sensor_l1 = d.pop("sensorL1", UNSET)

        sensor_l2 = d.pop("sensorL2", UNSET)

        sensor_l3 = d.pop("sensorL3", UNSET)

        sensor_settings = cls(
            sensor_l1=sensor_l1,
            sensor_l2=sensor_l2,
            sensor_l3=sensor_l3,
        )

        sensor_settings.additional_properties = d
        return sensor_settings

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
