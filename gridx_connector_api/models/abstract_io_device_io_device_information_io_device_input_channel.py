from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_io_device_io_device_information_io_device_input_channel_io_device_input_action import (
        AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction,
    )


T = TypeVar("T", bound="AbstractIODeviceIODeviceInformationIODeviceInputChannel")


@_attrs_define
class AbstractIODeviceIODeviceInformationIODeviceInputChannel:
    """
    Attributes:
        bit_mask (str | Unset): BitMask used to identify the channel.
        bit_value (str | Unset): BitValue used to trigger the action.
        actions (list[AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction] | Unset):
    """

    bit_mask: str | Unset = UNSET
    bit_value: str | Unset = UNSET
    actions: list[AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bit_mask = self.bit_mask

        bit_value = self.bit_value

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
        if bit_value is not UNSET:
            field_dict["bitValue"] = bit_value
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_io_device_io_device_information_io_device_input_channel_io_device_input_action import (
            AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction,
        )

        d = dict(src_dict)
        bit_mask = d.pop("bitMask", UNSET)

        bit_value = d.pop("bitValue", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = AbstractIODeviceIODeviceInformationIODeviceInputChannelIODeviceInputAction.from_dict(
                    actions_item_data
                )

                actions.append(actions_item)

        abstract_io_device_io_device_information_io_device_input_channel = cls(
            bit_mask=bit_mask,
            bit_value=bit_value,
            actions=actions,
        )

        abstract_io_device_io_device_information_io_device_input_channel.additional_properties = d
        return abstract_io_device_io_device_information_io_device_input_channel

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
