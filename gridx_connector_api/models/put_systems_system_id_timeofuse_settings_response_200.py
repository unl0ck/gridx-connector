from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutSystemsSystemIDTimeofuseSettingsResponse200")


@_attrs_define
class PutSystemsSystemIDTimeofuseSettingsResponse200:
    """
    Attributes:
        enabled (bool): If `true`, Time-of-Use (ToU) optimization is enabled for this system.
        enabled_battery_charge_from_grid (bool): If `true`, the Time-of-Use (ToU) optimization is allowed to trigger
            charging of the battery while
            simultaneously importing electricity from the grid. Default: `true`
             Example: True.
        enabled_discharge_flexibility_to_grid (bool): If `true`, the Time-of-Use optimization is allowed to trigger
            discharging of electricity from any
            flexibility (battery and EVCS, when EVCS discharge is supported) into the grid. Default: `false`
        enabled_pv_curtailment (bool): If `true`, the Time-of-Use optimization allows curtailment of PV generation to
            prevent energy surplus feed-in
            during negative export prices.  Default: `false`
    """

    enabled: bool
    enabled_battery_charge_from_grid: bool
    enabled_discharge_flexibility_to_grid: bool
    enabled_pv_curtailment: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enabled_battery_charge_from_grid = self.enabled_battery_charge_from_grid

        enabled_discharge_flexibility_to_grid = self.enabled_discharge_flexibility_to_grid

        enabled_pv_curtailment = self.enabled_pv_curtailment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "enabledBatteryChargeFromGrid": enabled_battery_charge_from_grid,
                "enabledDischargeFlexibilityToGrid": enabled_discharge_flexibility_to_grid,
                "enabledPVCurtailment": enabled_pv_curtailment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        enabled_battery_charge_from_grid = d.pop("enabledBatteryChargeFromGrid")

        enabled_discharge_flexibility_to_grid = d.pop("enabledDischargeFlexibilityToGrid")

        enabled_pv_curtailment = d.pop("enabledPVCurtailment")

        put_systems_system_id_timeofuse_settings_response_200 = cls(
            enabled=enabled,
            enabled_battery_charge_from_grid=enabled_battery_charge_from_grid,
            enabled_discharge_flexibility_to_grid=enabled_discharge_flexibility_to_grid,
            enabled_pv_curtailment=enabled_pv_curtailment,
        )

        put_systems_system_id_timeofuse_settings_response_200.additional_properties = d
        return put_systems_system_id_timeofuse_settings_response_200

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
