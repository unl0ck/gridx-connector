from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement")


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceEVChargingStationsMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Date and time the data point was collected.
        l_1_voltage (int | Unset): Voltage for first phase in mW.
        l_2_voltage (int | Unset): Voltage for second phase in mW.
        l_3_voltage (int | Unset): Voltage for third phase in mW.
        l_1_current (int | Unset): Current for first phase in mA.
        l_2_current (int | Unset): Current for second phase in mA.
        l_3_current (int | Unset): Current for third phase in mA.
        real_power (int | Unset): Real Power in mW. Positive values mean charging, negative values
            mean discharging (V2G; currently not done).
        power_factor (int | Unset): Power Factor in 0.1% (cosphi).
        l_1_real_power (int | Unset): Real Power L1 in mW.
        l_2_real_power (int | Unset): Real Power L2 in mW.
        l_3_real_power (int | Unset): Real Power L3 in mW.
        temperature (int | Unset): Temperature inside the charging station in Â°C.
        capacity (int | Unset): The total capacity of the EV battery in Wh.
        state_of_charge (float | Unset): The current state of charge of the EV battery in percent from 0.0 -
            100.0%.
        max_charge (int | Unset): Maximum allowed charge power in mW.
        min_charge (int | Unset): Minimum allowed charge power in mW, below this power the EV won't
            charge.
        max_discharge (int | Unset): Maximum allowed discharge power in mW.
        station_state (str | Unset): State indicating whether the charging station is charging, ready, in
            error state, etc.
        plug_state (str | Unset): State indicates whether an EV is plugged into the charging station.
        plugged_in (bool | Unset): PluggedIn true if an electric vehicle is currently plugged into the
            charging station.
        token_id (str | Unset): TokenID is the used authentication token at the charging station.
    """

    measured_at: datetime.datetime | Unset = UNSET
    l_1_voltage: int | Unset = UNSET
    l_2_voltage: int | Unset = UNSET
    l_3_voltage: int | Unset = UNSET
    l_1_current: int | Unset = UNSET
    l_2_current: int | Unset = UNSET
    l_3_current: int | Unset = UNSET
    real_power: int | Unset = UNSET
    power_factor: int | Unset = UNSET
    l_1_real_power: int | Unset = UNSET
    l_2_real_power: int | Unset = UNSET
    l_3_real_power: int | Unset = UNSET
    temperature: int | Unset = UNSET
    capacity: int | Unset = UNSET
    state_of_charge: float | Unset = UNSET
    max_charge: int | Unset = UNSET
    min_charge: int | Unset = UNSET
    max_discharge: int | Unset = UNSET
    station_state: str | Unset = UNSET
    plug_state: str | Unset = UNSET
    plugged_in: bool | Unset = UNSET
    token_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        l_1_voltage = self.l_1_voltage

        l_2_voltage = self.l_2_voltage

        l_3_voltage = self.l_3_voltage

        l_1_current = self.l_1_current

        l_2_current = self.l_2_current

        l_3_current = self.l_3_current

        real_power = self.real_power

        power_factor = self.power_factor

        l_1_real_power = self.l_1_real_power

        l_2_real_power = self.l_2_real_power

        l_3_real_power = self.l_3_real_power

        temperature = self.temperature

        capacity = self.capacity

        state_of_charge = self.state_of_charge

        max_charge = self.max_charge

        min_charge = self.min_charge

        max_discharge = self.max_discharge

        station_state = self.station_state

        plug_state = self.plug_state

        plugged_in = self.plugged_in

        token_id = self.token_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if l_1_voltage is not UNSET:
            field_dict["l1Voltage"] = l_1_voltage
        if l_2_voltage is not UNSET:
            field_dict["l2Voltage"] = l_2_voltage
        if l_3_voltage is not UNSET:
            field_dict["l3Voltage"] = l_3_voltage
        if l_1_current is not UNSET:
            field_dict["l1Current"] = l_1_current
        if l_2_current is not UNSET:
            field_dict["l2Current"] = l_2_current
        if l_3_current is not UNSET:
            field_dict["l3Current"] = l_3_current
        if real_power is not UNSET:
            field_dict["realPower"] = real_power
        if power_factor is not UNSET:
            field_dict["powerFactor"] = power_factor
        if l_1_real_power is not UNSET:
            field_dict["l1RealPower"] = l_1_real_power
        if l_2_real_power is not UNSET:
            field_dict["l2RealPower"] = l_2_real_power
        if l_3_real_power is not UNSET:
            field_dict["l3RealPower"] = l_3_real_power
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge
        if max_charge is not UNSET:
            field_dict["maxCharge"] = max_charge
        if min_charge is not UNSET:
            field_dict["minCharge"] = min_charge
        if max_discharge is not UNSET:
            field_dict["maxDischarge"] = max_discharge
        if station_state is not UNSET:
            field_dict["stationState"] = station_state
        if plug_state is not UNSET:
            field_dict["plugState"] = plug_state
        if plugged_in is not UNSET:
            field_dict["pluggedIn"] = plugged_in
        if token_id is not UNSET:
            field_dict["tokenID"] = token_id

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

        l_1_voltage = d.pop("l1Voltage", UNSET)

        l_2_voltage = d.pop("l2Voltage", UNSET)

        l_3_voltage = d.pop("l3Voltage", UNSET)

        l_1_current = d.pop("l1Current", UNSET)

        l_2_current = d.pop("l2Current", UNSET)

        l_3_current = d.pop("l3Current", UNSET)

        real_power = d.pop("realPower", UNSET)

        power_factor = d.pop("powerFactor", UNSET)

        l_1_real_power = d.pop("l1RealPower", UNSET)

        l_2_real_power = d.pop("l2RealPower", UNSET)

        l_3_real_power = d.pop("l3RealPower", UNSET)

        temperature = d.pop("temperature", UNSET)

        capacity = d.pop("capacity", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        max_charge = d.pop("maxCharge", UNSET)

        min_charge = d.pop("minCharge", UNSET)

        max_discharge = d.pop("maxDischarge", UNSET)

        station_state = d.pop("stationState", UNSET)

        plug_state = d.pop("plugState", UNSET)

        plugged_in = d.pop("pluggedIn", UNSET)

        token_id = d.pop("tokenID", UNSET)

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_ev_charging_stations_measurement = cls(
            measured_at=measured_at,
            l_1_voltage=l_1_voltage,
            l_2_voltage=l_2_voltage,
            l_3_voltage=l_3_voltage,
            l_1_current=l_1_current,
            l_2_current=l_2_current,
            l_3_current=l_3_current,
            real_power=real_power,
            power_factor=power_factor,
            l_1_real_power=l_1_real_power,
            l_2_real_power=l_2_real_power,
            l_3_real_power=l_3_real_power,
            temperature=temperature,
            capacity=capacity,
            state_of_charge=state_of_charge,
            max_charge=max_charge,
            min_charge=min_charge,
            max_discharge=max_discharge,
            station_state=station_state,
            plug_state=plug_state,
            plugged_in=plugged_in,
            token_id=token_id,
        )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_ev_charging_stations_measurement.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_ev_charging_stations_measurement

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
