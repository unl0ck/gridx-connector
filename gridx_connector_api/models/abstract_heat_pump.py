from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_heat_pump_type import AbstractHeatPumpType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_heat_pump_heat_pump_information import AbstractHeatPumpHeatPumpInformation


T = TypeVar("T", bound="AbstractHeatPump")


@_attrs_define
class AbstractHeatPump:
    """
    Attributes:
        type_ (AbstractHeatPumpType | Unset):
        manufacturer (str | Unset): Manufacturer of the heat pump. Example: Stiebel Eltron.
        model (str | Unset): Model of the heat pump. Example: WPMsystem.
        firmware (str | Unset): Firmware version of the heat pump. Example: mac_02:80:ad:24:d5:ab.
        heat_pump (AbstractHeatPumpHeatPumpInformation | Unset): The heat pump specific information.
    """

    type_: AbstractHeatPumpType | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    heat_pump: AbstractHeatPumpHeatPumpInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        manufacturer = self.manufacturer

        model = self.model

        firmware = self.firmware

        heat_pump: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heat_pump, Unset):
            heat_pump = self.heat_pump.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if heat_pump is not UNSET:
            field_dict["heatPump"] = heat_pump

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_heat_pump_heat_pump_information import AbstractHeatPumpHeatPumpInformation

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractHeatPumpType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractHeatPumpType(_type_)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        _heat_pump = d.pop("heatPump", UNSET)
        heat_pump: AbstractHeatPumpHeatPumpInformation | Unset
        if isinstance(_heat_pump, Unset):
            heat_pump = UNSET
        else:
            heat_pump = AbstractHeatPumpHeatPumpInformation.from_dict(_heat_pump)

        abstract_heat_pump = cls(
            type_=type_,
            manufacturer=manufacturer,
            model=model,
            firmware=firmware,
            heat_pump=heat_pump,
        )

        abstract_heat_pump.additional_properties = d
        return abstract_heat_pump

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
