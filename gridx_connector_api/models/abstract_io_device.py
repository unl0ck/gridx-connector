from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_io_device_type import AbstractIODeviceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_io_device_io_device_information import AbstractIODeviceIODeviceInformation


T = TypeVar("T", bound="AbstractIODevice")


@_attrs_define
class AbstractIODevice:
    """
    Attributes:
        type_ (AbstractIODeviceType | Unset):
        manufacturer (str | Unset): Manufacturer of the io device. Example: Siemens AG.
        model (str | Unset): Model of the io device. Example: Siemens AG 7KM2200-2EA30-1EA1.
        firmware (str | Unset): Firmware version of the io device. Example: HW 3 SW V3.2.2.
        io_device (AbstractIODeviceIODeviceInformation | Unset): The io device specific information.
    """

    type_: AbstractIODeviceType | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    io_device: AbstractIODeviceIODeviceInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        manufacturer = self.manufacturer

        model = self.model

        firmware = self.firmware

        io_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.io_device, Unset):
            io_device = self.io_device.to_dict()

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
        if io_device is not UNSET:
            field_dict["ioDevice"] = io_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_io_device_io_device_information import AbstractIODeviceIODeviceInformation

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractIODeviceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractIODeviceType(_type_)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        _io_device = d.pop("ioDevice", UNSET)
        io_device: AbstractIODeviceIODeviceInformation | Unset
        if isinstance(_io_device, Unset):
            io_device = UNSET
        else:
            io_device = AbstractIODeviceIODeviceInformation.from_dict(_io_device)

        abstract_io_device = cls(
            type_=type_,
            manufacturer=manufacturer,
            model=model,
            firmware=firmware,
            io_device=io_device,
        )

        abstract_io_device.additional_properties = d
        return abstract_io_device

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
