from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemsSystemIDHistoricalMeasurementsTotalBatteryMeasurement")


@_attrs_define
class GetSystemsSystemIDHistoricalMeasurementsTotalBatteryMeasurement:
    """MeasurementBattery represents the aggregated power or energy the gateway
    measured from a battery.

        Attributes:
            appliance_id (str | Unset): ApplianceID is the battery's appliance ID. It is empty for
                aggregated batteries.
                 Example: a7d56cb5-2dac-48d4-952a-6eb75ee0ce18.
            power (float | Unset): Power is the measured power used to charge/discharge the battery.

                Unit W, Meaning, Positive values indicate discharging. Negative
                values indicate charging.
            remaining_charge (float | Unset): RemainingCharge is the amount of energy left.
            capacity (float | Unset): Maximum energy the battery can provide in Wh.
            nominal_capacity (float | Unset): Nominal capacity of the battery in Wh.
            state_of_charge (float | Unset): State of Charge indicates how full a battery is. Unit Percentage
                points 0.0-1.0.
    """

    appliance_id: str | Unset = UNSET
    power: float | Unset = UNSET
    remaining_charge: float | Unset = UNSET
    capacity: float | Unset = UNSET
    nominal_capacity: float | Unset = UNSET
    state_of_charge: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_id = self.appliance_id

        power = self.power

        remaining_charge = self.remaining_charge

        capacity = self.capacity

        nominal_capacity = self.nominal_capacity

        state_of_charge = self.state_of_charge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if power is not UNSET:
            field_dict["power"] = power
        if remaining_charge is not UNSET:
            field_dict["remainingCharge"] = remaining_charge
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if nominal_capacity is not UNSET:
            field_dict["nominalCapacity"] = nominal_capacity
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_id = d.pop("applianceID", UNSET)

        power = d.pop("power", UNSET)

        remaining_charge = d.pop("remainingCharge", UNSET)

        capacity = d.pop("capacity", UNSET)

        nominal_capacity = d.pop("nominalCapacity", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        get_systems_system_id_historical_measurements_total_battery_measurement = cls(
            appliance_id=appliance_id,
            power=power,
            remaining_charge=remaining_charge,
            capacity=capacity,
            nominal_capacity=nominal_capacity,
            state_of_charge=state_of_charge,
        )

        get_systems_system_id_historical_measurements_total_battery_measurement.additional_properties = d
        return get_systems_system_id_historical_measurements_total_battery_measurement

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
