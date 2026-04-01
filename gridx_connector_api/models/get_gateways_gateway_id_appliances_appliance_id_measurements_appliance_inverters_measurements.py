from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements_a_measurement_produced_by_a_battery_inverter import (
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter,
    )


T = TypeVar("T", bound="GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements")


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurements:
    """
    Attributes:
        measured_at (datetime.datetime): Time when the data was measured.
        grid_frequency (int | Unset): The locally measured grid frequency in centi (10^-2) Hz.
        ac_current (int | Unset): AC current in mA.
        l_1ac_current (int | Unset): AC current on phase L1 in mA.
        l_2ac_current (int | Unset): AC current on phase L2 in mA.
        l_3ac_current (int | Unset): AC current on phase L3 in mA.
        l_1ac_voltage (int | Unset): AC voltage on phase L1 in mV.
        l_2ac_voltage (int | Unset): AC voltage on phase L2 in mV.
        l_3ac_voltage (int | Unset): AC voltage on phase L3 mV.
        ac_active_power (int | Unset): AC active power in mW.
        ac_reactive_power (int | Unset): AC reactive power in VAr.
        ac_apparent_power (int | Unset): AC apparent power VA.
        dc_current (int | Unset): DC current in mA.
        dc_voltage (int | Unset): DC voltage in mV.
        dc_power (int | Unset): DC power in mW.
        battery (GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProduced
            ByABatteryInverter | Unset):
    """

    measured_at: datetime.datetime
    grid_frequency: int | Unset = UNSET
    ac_current: int | Unset = UNSET
    l_1ac_current: int | Unset = UNSET
    l_2ac_current: int | Unset = UNSET
    l_3ac_current: int | Unset = UNSET
    l_1ac_voltage: int | Unset = UNSET
    l_2ac_voltage: int | Unset = UNSET
    l_3ac_voltage: int | Unset = UNSET
    ac_active_power: int | Unset = UNSET
    ac_reactive_power: int | Unset = UNSET
    ac_apparent_power: int | Unset = UNSET
    dc_current: int | Unset = UNSET
    dc_voltage: int | Unset = UNSET
    dc_power: int | Unset = UNSET
    battery: (
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at = self.measured_at.isoformat()

        grid_frequency = self.grid_frequency

        ac_current = self.ac_current

        l_1ac_current = self.l_1ac_current

        l_2ac_current = self.l_2ac_current

        l_3ac_current = self.l_3ac_current

        l_1ac_voltage = self.l_1ac_voltage

        l_2ac_voltage = self.l_2ac_voltage

        l_3ac_voltage = self.l_3ac_voltage

        ac_active_power = self.ac_active_power

        ac_reactive_power = self.ac_reactive_power

        ac_apparent_power = self.ac_apparent_power

        dc_current = self.dc_current

        dc_voltage = self.dc_voltage

        dc_power = self.dc_power

        battery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery, Unset):
            battery = self.battery.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "measuredAt": measured_at,
            }
        )
        if grid_frequency is not UNSET:
            field_dict["gridFrequency"] = grid_frequency
        if ac_current is not UNSET:
            field_dict["acCurrent"] = ac_current
        if l_1ac_current is not UNSET:
            field_dict["l1ACCurrent"] = l_1ac_current
        if l_2ac_current is not UNSET:
            field_dict["l2ACCurrent"] = l_2ac_current
        if l_3ac_current is not UNSET:
            field_dict["l3ACCurrent"] = l_3ac_current
        if l_1ac_voltage is not UNSET:
            field_dict["l1ACVoltage"] = l_1ac_voltage
        if l_2ac_voltage is not UNSET:
            field_dict["l2ACVoltage"] = l_2ac_voltage
        if l_3ac_voltage is not UNSET:
            field_dict["l3ACVoltage"] = l_3ac_voltage
        if ac_active_power is not UNSET:
            field_dict["acActivePower"] = ac_active_power
        if ac_reactive_power is not UNSET:
            field_dict["acReactivePower"] = ac_reactive_power
        if ac_apparent_power is not UNSET:
            field_dict["acApparentPower"] = ac_apparent_power
        if dc_current is not UNSET:
            field_dict["dcCurrent"] = dc_current
        if dc_voltage is not UNSET:
            field_dict["dcVoltage"] = dc_voltage
        if dc_power is not UNSET:
            field_dict["dcPower"] = dc_power
        if battery is not UNSET:
            field_dict["battery"] = battery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements_a_measurement_produced_by_a_battery_inverter import (
            GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter,
        )

        d = dict(src_dict)
        measured_at = isoparse(d.pop("measuredAt"))

        grid_frequency = d.pop("gridFrequency", UNSET)

        ac_current = d.pop("acCurrent", UNSET)

        l_1ac_current = d.pop("l1ACCurrent", UNSET)

        l_2ac_current = d.pop("l2ACCurrent", UNSET)

        l_3ac_current = d.pop("l3ACCurrent", UNSET)

        l_1ac_voltage = d.pop("l1ACVoltage", UNSET)

        l_2ac_voltage = d.pop("l2ACVoltage", UNSET)

        l_3ac_voltage = d.pop("l3ACVoltage", UNSET)

        ac_active_power = d.pop("acActivePower", UNSET)

        ac_reactive_power = d.pop("acReactivePower", UNSET)

        ac_apparent_power = d.pop("acApparentPower", UNSET)

        dc_current = d.pop("dcCurrent", UNSET)

        dc_voltage = d.pop("dcVoltage", UNSET)

        dc_power = d.pop("dcPower", UNSET)

        _battery = d.pop("battery", UNSET)
        battery: (
            GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter
            | Unset
        )
        if isinstance(_battery, Unset):
            battery = UNSET
        else:
            battery = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceInvertersMeasurementsAMeasurementProducedByABatteryInverter.from_dict(
                _battery
            )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements = cls(
            measured_at=measured_at,
            grid_frequency=grid_frequency,
            ac_current=ac_current,
            l_1ac_current=l_1ac_current,
            l_2ac_current=l_2ac_current,
            l_3ac_current=l_3ac_current,
            l_1ac_voltage=l_1ac_voltage,
            l_2ac_voltage=l_2ac_voltage,
            l_3ac_voltage=l_3ac_voltage,
            ac_active_power=ac_active_power,
            ac_reactive_power=ac_reactive_power,
            ac_apparent_power=ac_apparent_power,
            dc_current=dc_current,
            dc_voltage=dc_voltage,
            dc_power=dc_power,
            battery=battery,
        )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_inverters_measurements

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
