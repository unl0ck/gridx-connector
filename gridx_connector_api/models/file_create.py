from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FileCreate")


@_attrs_define
class FileCreate:
    """
    Attributes:
        key (str):
        size (float):
        modified (datetime.datetime):
        link (str): URI location of the uploaded file
    """

    key: str
    size: float
    modified: datetime.datetime
    link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        size = self.size

        modified = self.modified.isoformat()

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "size": size,
                "modified": modified,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        size = d.pop("size")

        modified = isoparse(d.pop("modified"))

        link = d.pop("link")

        file_create = cls(
            key=key,
            size=size,
            modified=modified,
            link=link,
        )

        file_create.additional_properties = d
        return file_create

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
