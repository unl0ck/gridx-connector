from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter",
)


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured in UTC using RFC3339 format.
        capacity (int | Unset): Capacity in Wh.
        nominal_capacity (int | Unset): Nominal capacity in Wh.
        state_of_charge (int | Unset): Value in range 0-100, state of charge in percent.
        state_of_health (int | Unset): Value in range 0-100, health of the battery in percent.
        temperature (int | Unset): Temperature of the battery in degrees Celsius.
        present_charge (int | Unset): Current charge of the battery in mW.
        present_discharge (int | Unset): Current discharge of the battery in mW.
    """

    measured_at: datetime.datetime | Unset = UNSET
    capacity: int | Unset = UNSET
    nominal_capacity: int | Unset = UNSET
    state_of_charge: int | Unset = UNSET
    state_of_health: int | Unset = UNSET
    temperature: int | Unset = UNSET
    present_charge: int | Unset = UNSET
    present_discharge: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        capacity = self.capacity

        nominal_capacity = self.nominal_capacity

        state_of_charge = self.state_of_charge

        state_of_health = self.state_of_health

        temperature = self.temperature

        present_charge = self.present_charge

        present_discharge = self.present_discharge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if nominal_capacity is not UNSET:
            field_dict["nominalCapacity"] = nominal_capacity
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge
        if state_of_health is not UNSET:
            field_dict["stateOfHealth"] = state_of_health
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if present_charge is not UNSET:
            field_dict["presentCharge"] = present_charge
        if present_discharge is not UNSET:
            field_dict["presentDischarge"] = present_discharge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        capacity = d.pop("capacity", UNSET)

        nominal_capacity = d.pop("nominalCapacity", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        state_of_health = d.pop("stateOfHealth", UNSET)

        temperature = d.pop("temperature", UNSET)

        present_charge = d.pop("presentCharge", UNSET)

        present_discharge = d.pop("presentDischarge", UNSET)

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements_a_measurement_produced_by_a_battery_inverter = cls(
            measured_at=measured_at,
            capacity=capacity,
            nominal_capacity=nominal_capacity,
            state_of_charge=state_of_charge,
            state_of_health=state_of_health,
            temperature=temperature,
            present_charge=present_charge,
            present_discharge=present_discharge,
        )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements_a_measurement_produced_by_a_battery_inverter.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements_a_measurement_produced_by_a_battery_inverter

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
