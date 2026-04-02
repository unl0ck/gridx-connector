from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedMeasurementExtendedBatteryMeasurement")


@_attrs_define
class ExtendedMeasurementExtendedBatteryMeasurement:
    """
    Attributes:
        charge (float | Unset): Power/energy charged to the battery.
        discharge (float | Unset): Power/energy discharged from the battery.
        state_of_charge (float | Unset): Percentage of battery capacity charged (0.0-1.0).
        capacity (float | Unset): Capacity is the maximum energy the battery can provide in Wh.
        nominal_capacity (float | Unset): NominalCapacity is the nominal capacity of battery in Wh.
    """

    charge: float | Unset = UNSET
    discharge: float | Unset = UNSET
    state_of_charge: float | Unset = UNSET
    capacity: float | Unset = UNSET
    nominal_capacity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge = self.charge

        discharge = self.discharge

        state_of_charge = self.state_of_charge

        capacity = self.capacity

        nominal_capacity = self.nominal_capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge is not UNSET:
            field_dict["charge"] = charge
        if discharge is not UNSET:
            field_dict["discharge"] = discharge
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if nominal_capacity is not UNSET:
            field_dict["nominalCapacity"] = nominal_capacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge = d.pop("charge", UNSET)

        discharge = d.pop("discharge", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        capacity = d.pop("capacity", UNSET)

        nominal_capacity = d.pop("nominalCapacity", UNSET)

        extended_measurement_extended_battery_measurement = cls(
            charge=charge,
            discharge=discharge,
            state_of_charge=state_of_charge,
            capacity=capacity,
            nominal_capacity=nominal_capacity,
        )

        extended_measurement_extended_battery_measurement.additional_properties = d
        return extended_measurement_extended_battery_measurement

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
