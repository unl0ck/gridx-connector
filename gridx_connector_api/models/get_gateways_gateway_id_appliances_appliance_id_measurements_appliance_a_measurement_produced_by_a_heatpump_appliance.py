from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance_operation_status import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceOperationStatus,
)
from ..models.get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance_ready_state import (
    GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceReadyState,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance"
)


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpAppliance:
    """
    Attributes:
        operation_status (GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpA
            pplianceOperationStatus):  Default: GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementPr
            oducedByAHeatpumpApplianceOperationStatus.UNKNOWN.
        measured_at (datetime.datetime | Unset): Time when the data was measured in UTC using RFC3339 format.
        power (int | Unset): Power of the heatpump in mW.
        power_l1 (int | Unset): Power for the first phase in mW .
        power_l2 (int | Unset):
        power_l3 (int | Unset):
        min_power (int | Unset):
        max_power (int | Unset):
        ready_state (GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplia
            nceReadyState | Unset):  Default: GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProd
            ucedByAHeatpumpApplianceReadyState.UNKNOWN.
        average_temperature (float | Unset):
        controlled_temperature (float | Unset):
        base_line_temperature (float | Unset):
        heat_source_temperature (float | Unset):
        outdoor_temperature (float | Unset):
        energy_heating (float | Unset):
        energy_drinking_hot_water (float | Unset):
    """

    operation_status: GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceOperationStatus = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceOperationStatus.UNKNOWN
    measured_at: datetime.datetime | Unset = UNSET
    power: int | Unset = UNSET
    power_l1: int | Unset = UNSET
    power_l2: int | Unset = UNSET
    power_l3: int | Unset = UNSET
    min_power: int | Unset = UNSET
    max_power: int | Unset = UNSET
    ready_state: (
        GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceReadyState
        | Unset
    ) = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceReadyState.UNKNOWN
    average_temperature: float | Unset = UNSET
    controlled_temperature: float | Unset = UNSET
    base_line_temperature: float | Unset = UNSET
    heat_source_temperature: float | Unset = UNSET
    outdoor_temperature: float | Unset = UNSET
    energy_heating: float | Unset = UNSET
    energy_drinking_hot_water: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_status = self.operation_status.value

        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        power = self.power

        power_l1 = self.power_l1

        power_l2 = self.power_l2

        power_l3 = self.power_l3

        min_power = self.min_power

        max_power = self.max_power

        ready_state: str | Unset = UNSET
        if not isinstance(self.ready_state, Unset):
            ready_state = self.ready_state.value

        average_temperature = self.average_temperature

        controlled_temperature = self.controlled_temperature

        base_line_temperature = self.base_line_temperature

        heat_source_temperature = self.heat_source_temperature

        outdoor_temperature = self.outdoor_temperature

        energy_heating = self.energy_heating

        energy_drinking_hot_water = self.energy_drinking_hot_water

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operationStatus": operation_status,
            }
        )
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if power is not UNSET:
            field_dict["power"] = power
        if power_l1 is not UNSET:
            field_dict["powerL1"] = power_l1
        if power_l2 is not UNSET:
            field_dict["powerL2"] = power_l2
        if power_l3 is not UNSET:
            field_dict["powerL3"] = power_l3
        if min_power is not UNSET:
            field_dict["minPower"] = min_power
        if max_power is not UNSET:
            field_dict["maxPower"] = max_power
        if ready_state is not UNSET:
            field_dict["readyState"] = ready_state
        if average_temperature is not UNSET:
            field_dict["averageTemperature"] = average_temperature
        if controlled_temperature is not UNSET:
            field_dict["controlledTemperature"] = controlled_temperature
        if base_line_temperature is not UNSET:
            field_dict["baseLineTemperature"] = base_line_temperature
        if heat_source_temperature is not UNSET:
            field_dict["heatSourceTemperature"] = heat_source_temperature
        if outdoor_temperature is not UNSET:
            field_dict["outdoorTemperature"] = outdoor_temperature
        if energy_heating is not UNSET:
            field_dict["energyHeating"] = energy_heating
        if energy_drinking_hot_water is not UNSET:
            field_dict["energyDrinkingHotWater"] = energy_drinking_hot_water

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_status = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceOperationStatus(
            d.pop("operationStatus")
        )

        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        power = d.pop("power", UNSET)

        power_l1 = d.pop("powerL1", UNSET)

        power_l2 = d.pop("powerL2", UNSET)

        power_l3 = d.pop("powerL3", UNSET)

        min_power = d.pop("minPower", UNSET)

        max_power = d.pop("maxPower", UNSET)

        _ready_state = d.pop("readyState", UNSET)
        ready_state: (
            GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceReadyState
            | Unset
        )
        if isinstance(_ready_state, Unset):
            ready_state = UNSET
        else:
            ready_state = GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceReadyState(
                _ready_state
            )

        average_temperature = d.pop("averageTemperature", UNSET)

        controlled_temperature = d.pop("controlledTemperature", UNSET)

        base_line_temperature = d.pop("baseLineTemperature", UNSET)

        heat_source_temperature = d.pop("heatSourceTemperature", UNSET)

        outdoor_temperature = d.pop("outdoorTemperature", UNSET)

        energy_heating = d.pop("energyHeating", UNSET)

        energy_drinking_hot_water = d.pop("energyDrinkingHotWater", UNSET)

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance = cls(
            operation_status=operation_status,
            measured_at=measured_at,
            power=power,
            power_l1=power_l1,
            power_l2=power_l2,
            power_l3=power_l3,
            min_power=min_power,
            max_power=max_power,
            ready_state=ready_state,
            average_temperature=average_temperature,
            controlled_temperature=controlled_temperature,
            base_line_temperature=base_line_temperature,
            heat_source_temperature=heat_source_temperature,
            outdoor_temperature=outdoor_temperature,
            energy_heating=energy_heating,
            energy_drinking_hot_water=energy_drinking_hot_water,
        )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_a_measurement_produced_by_a_heatpump_appliance

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
