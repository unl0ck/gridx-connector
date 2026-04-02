from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_resources_item_data_item_type_0 import DeviceResourcesItemDataItemType0


T = TypeVar("T", bound="DeviceResourcesItem")


@_attrs_define
class DeviceResourcesItem:
    """A specific resource describes a capability (e.g. flexible start of white goods).

    Attributes:
        url (str): URL of the resource. Example: https://api.eebus.org/devices/1041A421/powerSequences.
        type_ (str): Type of the resource. Example: powerSequence.
        supports_binding (bool): Explicit definition whether the resource supports exclusive binding. Example: True.
        data (list[DeviceResourcesItemDataItemType0]):
        specialization (str | Unset): Specialization of the resource. Example: flexibleStart.
    """

    url: str
    type_: str
    supports_binding: bool
    data: list[DeviceResourcesItemDataItemType0]
    specialization: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_resources_item_data_item_type_0 import DeviceResourcesItemDataItemType0

        url = self.url

        type_ = self.type_

        supports_binding = self.supports_binding

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, DeviceResourcesItemDataItemType0):
                data_item = data_item_data.to_dict()

            data.append(data_item)

        specialization = self.specialization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "type": type_,
                "supportsBinding": supports_binding,
                "data": data,
            }
        )
        if specialization is not UNSET:
            field_dict["specialization"] = specialization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_resources_item_data_item_type_0 import DeviceResourcesItemDataItemType0

        d = dict(src_dict)
        url = d.pop("url")

        type_ = d.pop("type")

        supports_binding = d.pop("supportsBinding")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(data: object) -> DeviceResourcesItemDataItemType0:
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_0 = DeviceResourcesItemDataItemType0.from_dict(data)

                return data_item_type_0

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        specialization = d.pop("specialization", UNSET)

        device_resources_item = cls(
            url=url,
            type_=type_,
            supports_binding=supports_binding,
            data=data,
            specialization=specialization,
        )

        device_resources_item.additional_properties = d
        return device_resources_item

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
