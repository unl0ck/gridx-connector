from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StarredSystem")


@_attrs_define
class StarredSystem:
    """Represents a starred system which holds an additional starredAt timestamp.

    A System represents the logical view of one gateway and its appliances.
    For example, a household can be represented as a system with a gateway such as a
    gridBox, and its connected appliances.

        Attributes:
            starred_at (datetime.datetime): Date when the system was starred in RFC3339 format. Example:
                2020-11-10T13:13:00Z.
    """

    starred_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starred_at = self.starred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starredAt": starred_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starred_at = isoparse(d.pop("starredAt"))

        starred_system = cls(
            starred_at=starred_at,
        )

        starred_system.additional_properties = d
        return starred_system

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
