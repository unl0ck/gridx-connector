from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractProductFunctionality")


@_attrs_define
class AbstractProductFunctionality:
    """A product functionality describes a feature.

    It is used to manage access to this feature via product options.

    This is the base type for the more concrete usages and not used directly within operations.

        Attributes:
            name (str | Unset): Name of the product functionality. Example: EV Manager.
            hide (bool | Unset): Indicates whether the product functionality should be hidden or shown.
            description (str | Unset): Describes the purpose of the product functionality.
    """

    name: str | Unset = UNSET
    hide: bool | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        hide = self.hide

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hide is not UNSET:
            field_dict["hide"] = hide
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        hide = d.pop("hide", UNSET)

        description = d.pop("description", UNSET)

        abstract_product_functionality = cls(
            name=name,
            hide=hide,
            description=description,
        )

        abstract_product_functionality.additional_properties = d
        return abstract_product_functionality

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
