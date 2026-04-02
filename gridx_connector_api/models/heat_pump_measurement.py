from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.heat_pump_measurement_sg_ready_state import HeatPumpMeasurementSgReadyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HeatPumpMeasurement")


@_attrs_define
class HeatPumpMeasurement:
    """
    Attributes:
        appliance_id (str | Unset):
        power (float | Unset):
        sg_ready_state (HeatPumpMeasurementSgReadyState | Unset): Defines the state set for SG Ready. Default:
            HeatPumpMeasurementSgReadyState.UNKNOWN.
    """

    appliance_id: str | Unset = UNSET
    power: float | Unset = UNSET
    sg_ready_state: HeatPumpMeasurementSgReadyState | Unset = HeatPumpMeasurementSgReadyState.UNKNOWN
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_id = self.appliance_id

        power = self.power

        sg_ready_state: str | Unset = UNSET
        if not isinstance(self.sg_ready_state, Unset):
            sg_ready_state = self.sg_ready_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if power is not UNSET:
            field_dict["power"] = power
        if sg_ready_state is not UNSET:
            field_dict["sgReadyState"] = sg_ready_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_id = d.pop("applianceID", UNSET)

        power = d.pop("power", UNSET)

        _sg_ready_state = d.pop("sgReadyState", UNSET)
        sg_ready_state: HeatPumpMeasurementSgReadyState | Unset
        if isinstance(_sg_ready_state, Unset):
            sg_ready_state = UNSET
        else:
            sg_ready_state = HeatPumpMeasurementSgReadyState(_sg_ready_state)

        heat_pump_measurement = cls(
            appliance_id=appliance_id,
            power=power,
            sg_ready_state=sg_ready_state,
        )

        heat_pump_measurement.additional_properties = d
        return heat_pump_measurement

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
