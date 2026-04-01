from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action import (
        ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction,
    )


T = TypeVar("T", bound="ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannel")


@_attrs_define
class ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannel:
    """Represents one output channel of the IODevice.

    Attributes:
        bit_mask (str | Unset): Bit mask identifying the output channel.
        actions (list[ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction] | Unset):
            Actions (name/value pairs) that are applied to the channel when enabled.
    """

    bit_mask: str | Unset = UNSET
    actions: list[ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bit_mask = self.bit_mask

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bit_mask is not UNSET:
            field_dict["bitMask"] = bit_mask
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appliance_update_strict_io_device_information_io_device_output_channel_io_device_output_action import (
            ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction,
        )

        d = dict(src_dict)
        bit_mask = d.pop("bitMask", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = (
                    ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputAction.from_dict(
                        actions_item_data
                    )
                )

                actions.append(actions_item)

        appliance_update_strict_io_device_information_io_device_output_channel = cls(
            bit_mask=bit_mask,
            actions=actions,
        )

        appliance_update_strict_io_device_information_io_device_output_channel.additional_properties = d
        return appliance_update_strict_io_device_information_io_device_output_channel

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
