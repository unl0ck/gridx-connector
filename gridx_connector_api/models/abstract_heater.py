from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_heater_type import AbstractHeaterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_heater_heater import AbstractHeaterHeater


T = TypeVar("T", bound="AbstractHeater")


@_attrs_define
class AbstractHeater:
    """
    Attributes:
        type_ (AbstractHeaterType | Unset):
        firmware (str | Unset): Firmware version of the heater. Example: 101.3.
        heater (AbstractHeaterHeater | Unset): The heater specific information.
    """

    type_: AbstractHeaterType | Unset = UNSET
    firmware: str | Unset = UNSET
    heater: AbstractHeaterHeater | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        firmware = self.firmware

        heater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heater, Unset):
            heater = self.heater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if heater is not UNSET:
            field_dict["heater"] = heater

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_heater_heater import AbstractHeaterHeater

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractHeaterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractHeaterType(_type_)

        firmware = d.pop("firmware", UNSET)

        _heater = d.pop("heater", UNSET)
        heater: AbstractHeaterHeater | Unset
        if isinstance(_heater, Unset):
            heater = UNSET
        else:
            heater = AbstractHeaterHeater.from_dict(_heater)

        abstract_heater = cls(
            type_=type_,
            firmware=firmware,
            heater=heater,
        )

        abstract_heater.additional_properties = d
        return abstract_heater

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
