from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready import (
        ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady,
    )


T = TypeVar("T", bound="ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction")


@_attrs_define
class ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction:
    """An individual output action, that can be registered to an output channel of an IODevice.

    Attributes:
        bit_value (str | Unset): The value to write to the IODevice's output channel. Each action has its own bit value,
            to allow arbitrary combinations to be written to the output channel.
        sg_ready
            (ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady |
            Unset): Used to specify a connection to a heat pump supporting the SGReady standard.
    """

    bit_value: str | Unset = UNSET
    sg_ready: (
        ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bit_value = self.bit_value

        sg_ready: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sg_ready, Unset):
            sg_ready = self.sg_ready.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bit_value is not UNSET:
            field_dict["bitValue"] = bit_value
        if sg_ready is not UNSET:
            field_dict["sgReady"] = sg_ready

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready import (
            ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady,
        )

        d = dict(src_dict)
        bit_value = d.pop("bitValue", UNSET)

        _sg_ready = d.pop("sgReady", UNSET)
        sg_ready: (
            ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady
            | Unset
        )
        if isinstance(_sg_ready, Unset):
            sg_ready = UNSET
        else:
            sg_ready = ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady.from_dict(
                _sg_ready
            )

        appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action = cls(
            bit_value=bit_value,
            sg_ready=sg_ready,
        )

        appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action.additional_properties = d
        return appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action

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
