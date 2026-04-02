from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AMeasurementProducedByABatteryInverter")


@_attrs_define
class AMeasurementProducedByABatteryInverter:
    """
    Attributes:
        present_charge (int | Unset): Current charge of the battery in mW.
        present_discharge (int | Unset): Current discharge of the battery in mW.
    """

    present_charge: int | Unset = UNSET
    present_discharge: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        present_charge = self.present_charge

        present_discharge = self.present_discharge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if present_charge is not UNSET:
            field_dict["presentCharge"] = present_charge
        if present_discharge is not UNSET:
            field_dict["presentDischarge"] = present_discharge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        present_charge = d.pop("presentCharge", UNSET)

        present_discharge = d.pop("presentDischarge", UNSET)

        a_measurement_produced_by_a_battery_inverter = cls(
            present_charge=present_charge,
            present_discharge=present_discharge,
        )

        a_measurement_produced_by_a_battery_inverter.additional_properties = d
        return a_measurement_produced_by_a_battery_inverter

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
