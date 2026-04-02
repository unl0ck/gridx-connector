from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station_plug_state import (
    MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation",
)


@_attrs_define
class MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation:
    """
    Attributes:
        appliance_id (str | Unset): gridX API internal ID of the appliance. Example:
            a7d56cb5-2dac-48d4-952a-6eb75ee0ce18.
        power (float | Unset): Measured power used to charge/discharge via EV station,
            positive values indicate charging, negatives discharging.
        state_of_charge (float | Unset): Percentage of the EVs battery capacity charged (0.0-1.0).
        reading_total (float | Unset): The sum of all meter readings in Wh.
        reading_tariff_1 (float | Unset): The meter reading of meter tariff 1 in Wh.
        reading_tariff_2 (float | Unset): The meter reading of meter tariff 2 in Wh.
        plug_state (MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingS
            tationPlugState | Unset): Defines whether this EV is currently plugged in the charging station and whether it's
            charging. Default: MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvCh
            argingStationPlugState.UNPLUGGED.
        current_l1 (float | Unset): Current of the first phase in Ampere.
        current_l2 (float | Unset): Current of the second phase in Ampere.
        current_l3 (float | Unset): Current of the third phase in Ampere.
    """

    appliance_id: str | Unset = UNSET
    power: float | Unset = UNSET
    state_of_charge: float | Unset = UNSET
    reading_total: float | Unset = UNSET
    reading_tariff_1: float | Unset = UNSET
    reading_tariff_2: float | Unset = UNSET
    plug_state: (
        MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState
        | Unset
    ) = MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState.UNPLUGGED
    current_l1: float | Unset = UNSET
    current_l2: float | Unset = UNSET
    current_l3: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_id = self.appliance_id

        power = self.power

        state_of_charge = self.state_of_charge

        reading_total = self.reading_total

        reading_tariff_1 = self.reading_tariff_1

        reading_tariff_2 = self.reading_tariff_2

        plug_state: str | Unset = UNSET
        if not isinstance(self.plug_state, Unset):
            plug_state = self.plug_state.value

        current_l1 = self.current_l1

        current_l2 = self.current_l2

        current_l3 = self.current_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if power is not UNSET:
            field_dict["power"] = power
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge
        if reading_total is not UNSET:
            field_dict["readingTotal"] = reading_total
        if reading_tariff_1 is not UNSET:
            field_dict["readingTariff1"] = reading_tariff_1
        if reading_tariff_2 is not UNSET:
            field_dict["readingTariff2"] = reading_tariff_2
        if plug_state is not UNSET:
            field_dict["plugState"] = plug_state
        if current_l1 is not UNSET:
            field_dict["currentL1"] = current_l1
        if current_l2 is not UNSET:
            field_dict["currentL2"] = current_l2
        if current_l3 is not UNSET:
            field_dict["currentL3"] = current_l3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_id = d.pop("applianceID", UNSET)

        power = d.pop("power", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        reading_total = d.pop("readingTotal", UNSET)

        reading_tariff_1 = d.pop("readingTariff1", UNSET)

        reading_tariff_2 = d.pop("readingTariff2", UNSET)

        _plug_state = d.pop("plugState", UNSET)
        plug_state: (
            MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState
            | Unset
        )
        if isinstance(_plug_state, Unset):
            plug_state = UNSET
        else:
            plug_state = MeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState(
                _plug_state
            )

        current_l1 = d.pop("currentL1", UNSET)

        current_l2 = d.pop("currentL2", UNSET)

        current_l3 = d.pop("currentL3", UNSET)

        measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station = cls(
            appliance_id=appliance_id,
            power=power,
            state_of_charge=state_of_charge,
            reading_total=reading_total,
            reading_tariff_1=reading_tariff_1,
            reading_tariff_2=reading_tariff_2,
            plug_state=plug_state,
            current_l1=current_l1,
            current_l2=current_l2,
            current_l3=current_l3,
        )

        measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station.additional_properties = d
        return measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station

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
