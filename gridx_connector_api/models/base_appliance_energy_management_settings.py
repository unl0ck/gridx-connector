from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseApplianceEnergyManagementSettings")


@_attrs_define
class BaseApplianceEnergyManagementSettings:
    """Contains energy management information

    Attributes:
        updated_at (datetime.datetime): Specifies when the energy management settings were updated the last time.
        min_control_interval (int | Unset):
        soc_max (float | Unset): The maximum state of charge an energy storage can be charged to in a range from [0-100]
            in %.
        soc_lock_max (float | Unset): The threshold above which no charging is allowed once SoC max is reached, in a
            range from [0-100] in %.
            Must be smaller than or equal to socMax.
        soc_min (float | Unset): The minimum state of charge an energy storage can be discharged to in a range from
            [0-100] in %.
        soc_lock_min (float | Unset): The threshold below which no discharging is allowed once SoC min is reached, in a
            range from [0-100] in %.
            Must be larger than or equal to socMin.
        soc_deep_discharge (float | Unset): The lowest state of charge an energy storage can reach, in a range from
            [0-100] in %.
            Below this it is not usable and a forced recharge to at least socMin is required.
        phase_mapping (list[int] | None | Unset): Contains three indices representing the actual phases on the grid
            connection point this appliance is connected to.
            Note that the first phase has index 0 and last phase index 2.
            The index of the sequence is the phase on the gcp and the values are the appliance phases. Unused phases are
            marked with -1.
        temperature_extreme_max (float | Unset): The temperature to which the system should be heated up to in Â°C, if
            there is an energy surplus.
        temperature_extreme_min (float | Unset): The minimum temperature the system can reach in Â°C.
        temperature_comfort_max (float | Unset): The temperature to which the system should be heated up to in Â°C, if
            there is no energy surplus.
        temperature_comfort_min (float | Unset): The temperature at which the system starts to heat up to in Â°C.
        surplus_threshold (int | Unset): The supply surplus threshold for the EMS to activate the appliance (in Watt).
    """

    updated_at: datetime.datetime
    min_control_interval: int | Unset = UNSET
    soc_max: float | Unset = UNSET
    soc_lock_max: float | Unset = UNSET
    soc_min: float | Unset = UNSET
    soc_lock_min: float | Unset = UNSET
    soc_deep_discharge: float | Unset = UNSET
    phase_mapping: list[int] | None | Unset = UNSET
    temperature_extreme_max: float | Unset = UNSET
    temperature_extreme_min: float | Unset = UNSET
    temperature_comfort_max: float | Unset = UNSET
    temperature_comfort_min: float | Unset = UNSET
    surplus_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        min_control_interval = self.min_control_interval

        soc_max = self.soc_max

        soc_lock_max = self.soc_lock_max

        soc_min = self.soc_min

        soc_lock_min = self.soc_lock_min

        soc_deep_discharge = self.soc_deep_discharge

        phase_mapping: list[int] | None | Unset
        if isinstance(self.phase_mapping, Unset):
            phase_mapping = UNSET
        elif isinstance(self.phase_mapping, list):
            phase_mapping = self.phase_mapping

        else:
            phase_mapping = self.phase_mapping

        temperature_extreme_max = self.temperature_extreme_max

        temperature_extreme_min = self.temperature_extreme_min

        temperature_comfort_max = self.temperature_comfort_max

        temperature_comfort_min = self.temperature_comfort_min

        surplus_threshold = self.surplus_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updatedAt": updated_at,
            }
        )
        if min_control_interval is not UNSET:
            field_dict["minControlInterval"] = min_control_interval
        if soc_max is not UNSET:
            field_dict["socMax"] = soc_max
        if soc_lock_max is not UNSET:
            field_dict["socLockMax"] = soc_lock_max
        if soc_min is not UNSET:
            field_dict["socMin"] = soc_min
        if soc_lock_min is not UNSET:
            field_dict["socLockMin"] = soc_lock_min
        if soc_deep_discharge is not UNSET:
            field_dict["socDeepDischarge"] = soc_deep_discharge
        if phase_mapping is not UNSET:
            field_dict["phaseMapping"] = phase_mapping
        if temperature_extreme_max is not UNSET:
            field_dict["temperatureExtremeMax"] = temperature_extreme_max
        if temperature_extreme_min is not UNSET:
            field_dict["temperatureExtremeMin"] = temperature_extreme_min
        if temperature_comfort_max is not UNSET:
            field_dict["temperatureComfortMax"] = temperature_comfort_max
        if temperature_comfort_min is not UNSET:
            field_dict["temperatureComfortMin"] = temperature_comfort_min
        if surplus_threshold is not UNSET:
            field_dict["surplusThreshold"] = surplus_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updatedAt"))

        min_control_interval = d.pop("minControlInterval", UNSET)

        soc_max = d.pop("socMax", UNSET)

        soc_lock_max = d.pop("socLockMax", UNSET)

        soc_min = d.pop("socMin", UNSET)

        soc_lock_min = d.pop("socLockMin", UNSET)

        soc_deep_discharge = d.pop("socDeepDischarge", UNSET)

        def _parse_phase_mapping(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phase_mapping_type_0 = cast(list[int], data)

                return phase_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        phase_mapping = _parse_phase_mapping(d.pop("phaseMapping", UNSET))

        temperature_extreme_max = d.pop("temperatureExtremeMax", UNSET)

        temperature_extreme_min = d.pop("temperatureExtremeMin", UNSET)

        temperature_comfort_max = d.pop("temperatureComfortMax", UNSET)

        temperature_comfort_min = d.pop("temperatureComfortMin", UNSET)

        surplus_threshold = d.pop("surplusThreshold", UNSET)

        base_appliance_energy_management_settings = cls(
            updated_at=updated_at,
            min_control_interval=min_control_interval,
            soc_max=soc_max,
            soc_lock_max=soc_lock_max,
            soc_min=soc_min,
            soc_lock_min=soc_lock_min,
            soc_deep_discharge=soc_deep_discharge,
            phase_mapping=phase_mapping,
            temperature_extreme_max=temperature_extreme_max,
            temperature_extreme_min=temperature_extreme_min,
            temperature_comfort_max=temperature_comfort_max,
            temperature_comfort_min=temperature_comfort_min,
            surplus_threshold=surplus_threshold,
        )

        base_appliance_energy_management_settings.additional_properties = d
        return base_appliance_energy_management_settings

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
