from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.heater_heater_medium import HeaterHeaterMedium
from ..models.heater_heater_type import HeaterHeaterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HeaterHeater")


@_attrs_define
class HeaterHeater:
    """The heater specific information.

    Attributes:
        type_ (HeaterHeaterType | Unset): Describes the specific type of the heater.
        medium (HeaterHeaterMedium | Unset): The medium the heater is working with.
        nominal_power (int | Unset): The nominal power of the heater.
    """

    type_: HeaterHeaterType | Unset = UNSET
    medium: HeaterHeaterMedium | Unset = UNSET
    nominal_power: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        medium: int | Unset = UNSET
        if not isinstance(self.medium, Unset):
            medium = self.medium.value

        nominal_power = self.nominal_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if medium is not UNSET:
            field_dict["medium"] = medium
        if nominal_power is not UNSET:
            field_dict["nominalPower"] = nominal_power

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: HeaterHeaterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = HeaterHeaterType(_type_)

        _medium = d.pop("medium", UNSET)
        medium: HeaterHeaterMedium | Unset
        if isinstance(_medium, Unset):
            medium = UNSET
        else:
            medium = HeaterHeaterMedium(_medium)

        nominal_power = d.pop("nominalPower", UNSET)

        heater_heater = cls(
            type_=type_,
            medium=medium,
            nominal_power=nominal_power,
        )

        heater_heater.additional_properties = d
        return heater_heater

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
