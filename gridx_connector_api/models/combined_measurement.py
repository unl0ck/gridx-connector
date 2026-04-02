from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_measurement_energy_management_measurement import (
        CombinedMeasurementEnergyManagementMeasurement,
    )


T = TypeVar("T", bound="CombinedMeasurement")


@_attrs_define
class CombinedMeasurement:
    """Combined appliance and energy management measurement.

    Attributes:
        energy_management (CombinedMeasurementEnergyManagementMeasurement | Unset):
    """

    energy_management: CombinedMeasurementEnergyManagementMeasurement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy_management, Unset):
            energy_management = self.energy_management.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy_management is not UNSET:
            field_dict["energyManagement"] = energy_management

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_measurement_energy_management_measurement import (
            CombinedMeasurementEnergyManagementMeasurement,
        )

        d = dict(src_dict)
        _energy_management = d.pop("energyManagement", UNSET)
        energy_management: CombinedMeasurementEnergyManagementMeasurement | Unset
        if isinstance(_energy_management, Unset):
            energy_management = UNSET
        else:
            energy_management = CombinedMeasurementEnergyManagementMeasurement.from_dict(_energy_management)

        combined_measurement = cls(
            energy_management=energy_management,
        )

        combined_measurement.additional_properties = d
        return combined_measurement

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
