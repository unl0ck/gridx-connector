from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductFunctionalitiesResponse200Item")


@_attrs_define
class GetProductFunctionalitiesResponse200Item:
    """
    Attributes:
        name (str): Name of the product functionality. Example: EV Manager.
        hide (bool): Indicates whether the product functionality should be hidden or shown.
        id (UUID): Unique identifier of the product functionality. Example: 4e3392ce-ed94-4946-8a11-665e0443723e.
        description (str | Unset): Describes the purpose of the product functionality.
    """

    name: str
    hide: bool
    id: UUID
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        hide = self.hide

        id = str(self.id)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "hide": hide,
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        hide = d.pop("hide")

        id = UUID(d.pop("id"))

        description = d.pop("description", UNSET)

        get_product_functionalities_response_200_item = cls(
            name=name,
            hide=hide,
            id=id,
            description=description,
        )

        get_product_functionalities_response_200_item.additional_properties = d
        return get_product_functionalities_response_200_item

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
