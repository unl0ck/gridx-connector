from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeterSensorSettings")


@_attrs_define
class MeterSensorSettings:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        sensor_l1 (int | Unset):
        sensor_l2 (int | Unset):
        sensor_l3 (int | Unset):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    sensor_l1: int | Unset = UNSET
    sensor_l2: int | Unset = UNSET
    sensor_l3: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        sensor_l1 = self.sensor_l1

        sensor_l2 = self.sensor_l2

        sensor_l3 = self.sensor_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
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
        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        sensor_l1 = d.pop("sensorL1", UNSET)

        sensor_l2 = d.pop("sensorL2", UNSET)

        sensor_l3 = d.pop("sensorL3", UNSET)

        meter_sensor_settings = cls(
            created_at=created_at,
            updated_at=updated_at,
            sensor_l1=sensor_l1,
            sensor_l2=sensor_l2,
            sensor_l3=sensor_l3,
        )

        meter_sensor_settings.additional_properties = d
        return meter_sensor_settings

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
