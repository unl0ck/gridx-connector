from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.io_device_information_type import IODeviceInformationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.io_device_information_io_device_input_channel import IODeviceInformationIODeviceInputChannel
    from ..models.io_device_information_io_device_output_channel import IODeviceInformationIODeviceOutputChannel


T = TypeVar("T", bound="IODeviceInformation")


@_attrs_define
class IODeviceInformation:
    """The io device specific information.

    Attributes:
        type_ (IODeviceInformationType | Unset): Describes the specific type of the device.
        in_channels_count (int | Unset): The number of input ports on the device, real physical ports you can connect a
            cable to.
        out_channels_count (int | Unset): The number of output ports on the device, real physical ports you can connect
            a cable to.
        input_channels (list[IODeviceInformationIODeviceInputChannel] | Unset): Input channels of the fieldbus coupler,
            containing actions.
        output_channels (list[IODeviceInformationIODeviceOutputChannel] | Unset): Output channels of the IODevice,
            containing actions. An output channel must not always use exactly one port, but can use multiple physical
            connections.
            SGReady heat pumps for example are connected using two output ports (which are grouped in one OutputChannel).
    """

    type_: IODeviceInformationType | Unset = UNSET
    in_channels_count: int | Unset = UNSET
    out_channels_count: int | Unset = UNSET
    input_channels: list[IODeviceInformationIODeviceInputChannel] | Unset = UNSET
    output_channels: list[IODeviceInformationIODeviceOutputChannel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        in_channels_count = self.in_channels_count

        out_channels_count = self.out_channels_count

        input_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_channels, Unset):
            input_channels = []
            for input_channels_item_data in self.input_channels:
                input_channels_item = input_channels_item_data.to_dict()
                input_channels.append(input_channels_item)

        output_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.output_channels, Unset):
            output_channels = []
            for output_channels_item_data in self.output_channels:
                output_channels_item = output_channels_item_data.to_dict()
                output_channels.append(output_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if in_channels_count is not UNSET:
            field_dict["inChannelsCount"] = in_channels_count
        if out_channels_count is not UNSET:
            field_dict["outChannelsCount"] = out_channels_count
        if input_channels is not UNSET:
            field_dict["inputChannels"] = input_channels
        if output_channels is not UNSET:
            field_dict["outputChannels"] = output_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.io_device_information_io_device_input_channel import IODeviceInformationIODeviceInputChannel
        from ..models.io_device_information_io_device_output_channel import IODeviceInformationIODeviceOutputChannel

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: IODeviceInformationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IODeviceInformationType(_type_)

        in_channels_count = d.pop("inChannelsCount", UNSET)

        out_channels_count = d.pop("outChannelsCount", UNSET)

        _input_channels = d.pop("inputChannels", UNSET)
        input_channels: list[IODeviceInformationIODeviceInputChannel] | Unset = UNSET
        if _input_channels is not UNSET:
            input_channels = []
            for input_channels_item_data in _input_channels:
                input_channels_item = IODeviceInformationIODeviceInputChannel.from_dict(input_channels_item_data)

                input_channels.append(input_channels_item)

        _output_channels = d.pop("outputChannels", UNSET)
        output_channels: list[IODeviceInformationIODeviceOutputChannel] | Unset = UNSET
        if _output_channels is not UNSET:
            output_channels = []
            for output_channels_item_data in _output_channels:
                output_channels_item = IODeviceInformationIODeviceOutputChannel.from_dict(output_channels_item_data)

                output_channels.append(output_channels_item)

        io_device_information = cls(
            type_=type_,
            in_channels_count=in_channels_count,
            out_channels_count=out_channels_count,
            input_channels=input_channels,
            output_channels=output_channels,
        )

        io_device_information.additional_properties = d
        return io_device_information

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
