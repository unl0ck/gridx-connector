from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_bindings_item import DeviceBindingsItem
    from ..models.device_resources_item import DeviceResourcesItem
    from ..models.device_usecases_item import DeviceUsecasesItem


T = TypeVar("T", bound="Device")


@_attrs_define
class Device:
    """
    Attributes:
        id (str): ID for device, must be url encoded. E.g. deviceId as specified by manufacturer. Example:
            27jslrNMHpUx266.
        url (str): URL of the device.
        type_ (str): Type of the device. Example: washer.
        bindings (list[DeviceBindingsItem]): List of bindings.
        usecases (list[DeviceUsecasesItem]): List of supported use-cases for this device.
        resources (list[DeviceResourcesItem]): List of resources available on this device.
        parent_url (str | Unset): URL of parent device.
        device_address (str | Unset): SPINE DeviceAddress. Example: d:_n:NaTeYtMjnNGtQqQvbuJT4AoSY-LBq_;:7Jbs,L"Qz.hQg.
        label (str | Unset): User-defined label via an external app e.g Home Connect. Example: My new dishwasher.
    """

    id: str
    url: str
    type_: str
    bindings: list[DeviceBindingsItem]
    usecases: list[DeviceUsecasesItem]
    resources: list[DeviceResourcesItem]
    parent_url: str | Unset = UNSET
    device_address: str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        type_ = self.type_

        bindings = []
        for bindings_item_data in self.bindings:
            bindings_item = bindings_item_data.to_dict()
            bindings.append(bindings_item)

        usecases = []
        for usecases_item_data in self.usecases:
            usecases_item = usecases_item_data.to_dict()
            usecases.append(usecases_item)

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        parent_url = self.parent_url

        device_address = self.device_address

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "type": type_,
                "bindings": bindings,
                "usecases": usecases,
                "resources": resources,
            }
        )
        if parent_url is not UNSET:
            field_dict["parentURL"] = parent_url
        if device_address is not UNSET:
            field_dict["deviceAddress"] = device_address
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_bindings_item import DeviceBindingsItem
        from ..models.device_resources_item import DeviceResourcesItem
        from ..models.device_usecases_item import DeviceUsecasesItem

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        type_ = d.pop("type")

        bindings = []
        _bindings = d.pop("bindings")
        for bindings_item_data in _bindings:
            bindings_item = DeviceBindingsItem.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        usecases = []
        _usecases = d.pop("usecases")
        for usecases_item_data in _usecases:
            usecases_item = DeviceUsecasesItem.from_dict(usecases_item_data)

            usecases.append(usecases_item)

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = DeviceResourcesItem.from_dict(resources_item_data)

            resources.append(resources_item)

        parent_url = d.pop("parentURL", UNSET)

        device_address = d.pop("deviceAddress", UNSET)

        label = d.pop("label", UNSET)

        device = cls(
            id=id,
            url=url,
            type_=type_,
            bindings=bindings,
            usecases=usecases,
            resources=resources,
            parent_url=parent_url,
            device_address=device_address,
            label=label,
        )

        device.additional_properties = d
        return device

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
