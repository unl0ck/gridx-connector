from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractInverterInverter")


@_attrs_define
class AbstractInverterInverter:
    """The inverter specific information.

    Attributes:
        max_active_power_output (int | Unset): Maximum active power output of the inverter in mW; set manually. Zero if
            not set.
        type_ (str | Unset): Describes the specific type of the inverter. Example: SUNGROW_SG_20_RT.
    """

    max_active_power_output: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_active_power_output = self.max_active_power_output

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_active_power_output is not UNSET:
            field_dict["maxActivePowerOutput"] = max_active_power_output
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_active_power_output = d.pop("maxActivePowerOutput", UNSET)

        type_ = d.pop("type", UNSET)

        abstract_inverter_inverter = cls(
            max_active_power_output=max_active_power_output,
            type_=type_,
        )

        abstract_inverter_inverter.additional_properties = d
        return abstract_inverter_inverter

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
