from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetSystemTagResponse201")


@_attrs_define
class SetSystemTagResponse201:
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
        created_at (datetime.datetime | Unset): Date when the system tag was created in RFC3339 format. Example:
            2017-12-22T14:20:50Z.
        updated_at (datetime.datetime | Unset): Date when the system tag was last updated in RFC3339 format. Example:
            2017-12-24T08:33:00Z.
    """

    name: str
    value: str
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        set_system_tag_response_201 = cls(
            name=name,
            value=value,
            created_at=created_at,
            updated_at=updated_at,
        )

        set_system_tag_response_201.additional_properties = d
        return set_system_tag_response_201

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
