from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergyManagementMeasurement")


@_attrs_define
class EnergyManagementMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        strategy_id (str | Unset): True if the PV power is dynamically limited based on the available
            battery capacity.
        dynamic_feed_in_curtailment (bool | Unset): True if the PV power is dynamically limited based on the available
            battery capacity.
        prognosis_based_battery_charging (bool | Unset): True if a forecast is used to determine the future feed-in into
            the
            batteries.
        active_power_setpoint (int | Unset): The setpoint the appliance should follow in mW.
        active_power_setpoint_systemic_error (int | Unset): The measured deviation from the setpoint for the active
            power value
            in mW.
        l_1_current_setpoint (int | Unset): Is the setpoint the appliance should follow in mA on phase 1.
        l_2_current_setpoint (int | Unset): Is the setpoint the appliance should follow in mA on phase 2.
        l_3_current_setpoint (int | Unset): Is the setpoint the appliance should follow in mA on phase 3.
        max_state_of_charge_after_max_feed_in (int | Unset): MaxStateOfChargeAfterMaxFeedIn is the max state of charge
            (0-100%) the
            battery can reach while considering the capacity needed to store the
            energy above max feed-in. (eBatMax - eBatOverFeedIn) * 100 /
            eBatMax.
        predicted_energy_output (int | Unset): PredictedEnergyOutput is the predicted electrical energy output of
            this appliance in Wh based on the forecast model, including error
            adjustments.
        energy_over_feed_in_cumulated_daily (int | Unset): EnergyOverFeedInCumulatedDaily is the cumulated energy over
            the
            feed-in that is saved this day thanks to the energy management. This
            value is reported by the grid meter in Wh.
    """

    measured_at: datetime.datetime | Unset = UNSET
    strategy_id: str | Unset = UNSET
    dynamic_feed_in_curtailment: bool | Unset = UNSET
    prognosis_based_battery_charging: bool | Unset = UNSET
    active_power_setpoint: int | Unset = UNSET
    active_power_setpoint_systemic_error: int | Unset = UNSET
    l_1_current_setpoint: int | Unset = UNSET
    l_2_current_setpoint: int | Unset = UNSET
    l_3_current_setpoint: int | Unset = UNSET
    max_state_of_charge_after_max_feed_in: int | Unset = UNSET
    predicted_energy_output: int | Unset = UNSET
    energy_over_feed_in_cumulated_daily: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        strategy_id = self.strategy_id

        dynamic_feed_in_curtailment = self.dynamic_feed_in_curtailment

        prognosis_based_battery_charging = self.prognosis_based_battery_charging

        active_power_setpoint = self.active_power_setpoint

        active_power_setpoint_systemic_error = self.active_power_setpoint_systemic_error

        l_1_current_setpoint = self.l_1_current_setpoint

        l_2_current_setpoint = self.l_2_current_setpoint

        l_3_current_setpoint = self.l_3_current_setpoint

        max_state_of_charge_after_max_feed_in = self.max_state_of_charge_after_max_feed_in

        predicted_energy_output = self.predicted_energy_output

        energy_over_feed_in_cumulated_daily = self.energy_over_feed_in_cumulated_daily

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if strategy_id is not UNSET:
            field_dict["strategyID"] = strategy_id
        if dynamic_feed_in_curtailment is not UNSET:
            field_dict["dynamicFeedInCurtailment"] = dynamic_feed_in_curtailment
        if prognosis_based_battery_charging is not UNSET:
            field_dict["prognosisBasedBatteryCharging"] = prognosis_based_battery_charging
        if active_power_setpoint is not UNSET:
            field_dict["activePowerSetpoint"] = active_power_setpoint
        if active_power_setpoint_systemic_error is not UNSET:
            field_dict["activePowerSetpointSystemicError"] = active_power_setpoint_systemic_error
        if l_1_current_setpoint is not UNSET:
            field_dict["l1CurrentSetpoint"] = l_1_current_setpoint
        if l_2_current_setpoint is not UNSET:
            field_dict["l2CurrentSetpoint"] = l_2_current_setpoint
        if l_3_current_setpoint is not UNSET:
            field_dict["l3CurrentSetpoint"] = l_3_current_setpoint
        if max_state_of_charge_after_max_feed_in is not UNSET:
            field_dict["maxStateOfChargeAfterMaxFeedIn"] = max_state_of_charge_after_max_feed_in
        if predicted_energy_output is not UNSET:
            field_dict["predictedEnergyOutput"] = predicted_energy_output
        if energy_over_feed_in_cumulated_daily is not UNSET:
            field_dict["energyOverFeedInCumulatedDaily"] = energy_over_feed_in_cumulated_daily

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

        strategy_id = d.pop("strategyID", UNSET)

        dynamic_feed_in_curtailment = d.pop("dynamicFeedInCurtailment", UNSET)

        prognosis_based_battery_charging = d.pop("prognosisBasedBatteryCharging", UNSET)

        active_power_setpoint = d.pop("activePowerSetpoint", UNSET)

        active_power_setpoint_systemic_error = d.pop("activePowerSetpointSystemicError", UNSET)

        l_1_current_setpoint = d.pop("l1CurrentSetpoint", UNSET)

        l_2_current_setpoint = d.pop("l2CurrentSetpoint", UNSET)

        l_3_current_setpoint = d.pop("l3CurrentSetpoint", UNSET)

        max_state_of_charge_after_max_feed_in = d.pop("maxStateOfChargeAfterMaxFeedIn", UNSET)

        predicted_energy_output = d.pop("predictedEnergyOutput", UNSET)

        energy_over_feed_in_cumulated_daily = d.pop("energyOverFeedInCumulatedDaily", UNSET)

        energy_management_measurement = cls(
            measured_at=measured_at,
            strategy_id=strategy_id,
            dynamic_feed_in_curtailment=dynamic_feed_in_curtailment,
            prognosis_based_battery_charging=prognosis_based_battery_charging,
            active_power_setpoint=active_power_setpoint,
            active_power_setpoint_systemic_error=active_power_setpoint_systemic_error,
            l_1_current_setpoint=l_1_current_setpoint,
            l_2_current_setpoint=l_2_current_setpoint,
            l_3_current_setpoint=l_3_current_setpoint,
            max_state_of_charge_after_max_feed_in=max_state_of_charge_after_max_feed_in,
            predicted_energy_output=predicted_energy_output,
            energy_over_feed_in_cumulated_daily=energy_over_feed_in_cumulated_daily,
        )

        energy_management_measurement.additional_properties = d
        return energy_management_measurement

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
