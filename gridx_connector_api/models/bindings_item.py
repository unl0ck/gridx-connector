from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bindings_item_type import BindingsItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BindingsItem")


@_attrs_define
class BindingsItem:
    """
    Attributes:
        type_ (BindingsItemType): The resource type for which the binding is created. Example: powerSequence.
        name (str): User-friendly name of binding partner. Example: bindingName.
        binding_id (str | Unset): ID of binding entry, must be unique in path. The bindingId is provided by the server
            and must not specified on client side. Example: jaxbv2.
        url (str | Unset): Convenience pointer to endpoint for this binding. The validity is provided by the server and
            must not be specified on client side. Example: https://api.eebus.org/devices/1041A421/bindings/jaxbv2.
        validity (datetime.datetime | Unset): A Binding is valid for 24 hours and will be released if not renewed in
            time. The validity is provided by the server and must not be specified on client side. Example:
            2021-07-24T23:59:59Z.
    """

    type_: BindingsItemType
    name: str
    binding_id: str | Unset = UNSET
    url: str | Unset = UNSET
    validity: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        binding_id = self.binding_id

        url = self.url

        validity: str | Unset = UNSET
        if not isinstance(self.validity, Unset):
            validity = self.validity.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if binding_id is not UNSET:
            field_dict["bindingId"] = binding_id
        if url is not UNSET:
            field_dict["url"] = url
        if validity is not UNSET:
            field_dict["validity"] = validity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = BindingsItemType(d.pop("type"))

        name = d.pop("name")

        binding_id = d.pop("bindingId", UNSET)

        url = d.pop("url", UNSET)

        _validity = d.pop("validity", UNSET)
        validity: datetime.datetime | Unset
        if isinstance(_validity, Unset):
            validity = UNSET
        else:
            validity = isoparse(_validity)

        bindings_item = cls(
            type_=type_,
            name=name,
            binding_id=binding_id,
            url=url,
            validity=validity,
        )

        bindings_item.additional_properties = d
        return bindings_item

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
