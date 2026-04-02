from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.container_container_type import ContainerContainerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerContainer")


@_attrs_define
class ContainerContainer:
    """The container specific information.

    Attributes:
        type_ (ContainerContainerType | Unset): Describes the specific type of the container.
    """

    type_: ContainerContainerType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ContainerContainerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContainerContainerType(_type_)

        container_container = cls(
            type_=type_,
        )

        container_container.additional_properties = d
        return container_container

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
