from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplianceUpdateEvLoadManagementParameters")


@_attrs_define
class ApplianceUpdateEvLoadManagementParameters:
    """Load management configuration for EV charging stations.

    **Deprecated** - Use the system's EV charging station configuration instead.

        Attributes:
            enabled (bool | Unset): Indicates whether the load management is enabled.
            max_power (float | Unset): The maximum power in W.
    """

    enabled: bool | Unset = UNSET
    max_power: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_power = self.max_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_power is not UNSET:
            field_dict["maxPower"] = max_power

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        max_power = d.pop("maxPower", UNSET)

        appliance_update_ev_load_management_parameters = cls(
            enabled=enabled,
            max_power=max_power,
        )

        appliance_update_ev_load_management_parameters.additional_properties = d
        return appliance_update_ev_load_management_parameters

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
