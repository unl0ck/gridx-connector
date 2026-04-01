from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerNetwork")


@_attrs_define
class ContainerNetwork:
    """Represents a network connection.

    Attributes:
        interface (str | Unset): Used network interface such as "eth0", "vpn0" etc. Example: eth0.
        address (str | Unset): IP address of the device. Example: 192.168.178.153.
        port (int | Unset): Port used for the connection.
        protocol (str | Unset): Protocol used for the connection. Example: tcp/modbus.
    """

    interface: str | Unset = UNSET
    address: str | Unset = UNSET
    port: int | Unset = UNSET
    protocol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        address = self.address

        port = self.port

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface", UNSET)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        protocol = d.pop("protocol", UNSET)

        container_network = cls(
            interface=interface,
            address=address,
            port=port,
            protocol=protocol,
        )

        container_network.additional_properties = d
        return container_network

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
