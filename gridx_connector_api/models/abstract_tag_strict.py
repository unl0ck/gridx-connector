from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AbstractTagStrict")


@_attrs_define
class AbstractTagStrict:
    """
    Attributes:
        name (str): The unique identifier of the tag within the context of the system.
            The tag name must consist only of lowercase letters (a-z), numbers (0-9), and hyphens (-), and must not start or
            end with a hyphen.
            It can be at most 128 characters long.
             Example: category.
        value (str): The value associated with the tag name.
            This can be any valid string up to 128 characters.
             Example: technology.
    """

    name: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        abstract_tag_strict = cls(
            name=name,
            value=value,
        )

        abstract_tag_strict.additional_properties = d
        return abstract_tag_strict

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
