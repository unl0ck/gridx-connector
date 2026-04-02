from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_container_type import AbstractContainerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_container_container import AbstractContainerContainer


T = TypeVar("T", bound="AbstractContainer")


@_attrs_define
class AbstractContainer:
    """
    Attributes:
        type_ (AbstractContainerType | Unset):
        manufacturer (str | Unset): Manufacturer of the container. Example: Loxone.
        model (str | Unset): Model of the container. Example: Miniserver.
        container (AbstractContainerContainer | Unset): The container specific information.
    """

    type_: AbstractContainerType | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    container: AbstractContainerContainer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        manufacturer = self.manufacturer

        model = self.model

        container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.container, Unset):
            container = self.container.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if container is not UNSET:
            field_dict["container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_container_container import AbstractContainerContainer

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractContainerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractContainerType(_type_)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        _container = d.pop("container", UNSET)
        container: AbstractContainerContainer | Unset
        if isinstance(_container, Unset):
            container = UNSET
        else:
            container = AbstractContainerContainer.from_dict(_container)

        abstract_container = cls(
            type_=type_,
            manufacturer=manufacturer,
            model=model,
            container=container,
        )

        abstract_container.additional_properties = d
        return abstract_container

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
