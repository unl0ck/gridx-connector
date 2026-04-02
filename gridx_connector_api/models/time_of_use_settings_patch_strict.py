from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeOfUseSettingsPatchStrict")


@_attrs_define
class TimeOfUseSettingsPatchStrict:
    """
    Attributes:
        enabled (bool | Unset): If `true`, Time-of-Use (ToU) optimization is enabled for this system.
        enabled_battery_charge_from_grid (bool | Unset): If `true`, the Time-of-Use (ToU) optimization is allowed to
            trigger charging of the battery while
            simultaneously importing electricity from the grid. Default: `true`
             Example: True.
        enabled_discharge_flexibility_to_grid (bool | Unset): If `true`, the Time-of-Use optimization is allowed to
            trigger discharging of electricity from any
            flexibility (battery and EVCS, when EVCS discharge is supported) into the grid. Default: `false`
        enabled_pv_curtailment (bool | Unset): If `true`, the Time-of-Use optimization allows curtailment of PV
            generation to prevent energy surplus feed-in
            during negative export prices.  Default: `false`
    """

    enabled: bool | Unset = UNSET
    enabled_battery_charge_from_grid: bool | Unset = UNSET
    enabled_discharge_flexibility_to_grid: bool | Unset = UNSET
    enabled_pv_curtailment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enabled_battery_charge_from_grid = self.enabled_battery_charge_from_grid

        enabled_discharge_flexibility_to_grid = self.enabled_discharge_flexibility_to_grid

        enabled_pv_curtailment = self.enabled_pv_curtailment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_battery_charge_from_grid is not UNSET:
            field_dict["enabledBatteryChargeFromGrid"] = enabled_battery_charge_from_grid
        if enabled_discharge_flexibility_to_grid is not UNSET:
            field_dict["enabledDischargeFlexibilityToGrid"] = enabled_discharge_flexibility_to_grid
        if enabled_pv_curtailment is not UNSET:
            field_dict["enabledPVCurtailment"] = enabled_pv_curtailment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        enabled_battery_charge_from_grid = d.pop("enabledBatteryChargeFromGrid", UNSET)

        enabled_discharge_flexibility_to_grid = d.pop("enabledDischargeFlexibilityToGrid", UNSET)

        enabled_pv_curtailment = d.pop("enabledPVCurtailment", UNSET)

        time_of_use_settings_patch_strict = cls(
            enabled=enabled,
            enabled_battery_charge_from_grid=enabled_battery_charge_from_grid,
            enabled_discharge_flexibility_to_grid=enabled_discharge_flexibility_to_grid,
            enabled_pv_curtailment=enabled_pv_curtailment,
        )

        time_of_use_settings_patch_strict.additional_properties = d
        return time_of_use_settings_patch_strict

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
