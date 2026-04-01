from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_meter_type import AbstractMeterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_meter_aux_meter import AbstractMeterAuxMeter


T = TypeVar("T", bound="AbstractMeter")


@_attrs_define
class AbstractMeter:
    """
    Attributes:
        type_ (AbstractMeterType | Unset):
        model (str | Unset): Model of the meter. Example: B-control Energy Manager 300.
        firmware (str | Unset): Firmware version of the meter. Example: 2.03.
        aux_meter (AbstractMeterAuxMeter | Unset): The meter specific information.
    """

    type_: AbstractMeterType | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    aux_meter: AbstractMeterAuxMeter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        model = self.model

        firmware = self.firmware

        aux_meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aux_meter, Unset):
            aux_meter = self.aux_meter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if aux_meter is not UNSET:
            field_dict["auxMeter"] = aux_meter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_meter_aux_meter import AbstractMeterAuxMeter

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractMeterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractMeterType(_type_)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        _aux_meter = d.pop("auxMeter", UNSET)
        aux_meter: AbstractMeterAuxMeter | Unset
        if isinstance(_aux_meter, Unset):
            aux_meter = UNSET
        else:
            aux_meter = AbstractMeterAuxMeter.from_dict(_aux_meter)

        abstract_meter = cls(
            type_=type_,
            model=model,
            firmware=firmware,
            aux_meter=aux_meter,
        )

        abstract_meter.additional_properties = d
        return abstract_meter

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
