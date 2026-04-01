from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemsAMSMetadataCounts")


@_attrs_define
class SystemsAMSMetadataCounts:
    """This will only be available if the response is a list or contains multiple items. It provides multiple
    "counts" of the list that is being returned.

        Attributes:
            total (int | Unset): The total number of objects in the list, regardless of any query parameters such as
                filtering or
                pagination.
                 Example: 321.
            filtered (int | Unset): The number of objects in the list after the filters have been applied. This ignores
                pagination and will
                show how many objects are available with the given filters. This number will always be less than or
                equal to the `total` count.
                 Example: 123.
    """

    total: int | Unset = UNSET
    filtered: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        filtered = self.filtered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if filtered is not UNSET:
            field_dict["filtered"] = filtered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        filtered = d.pop("filtered", UNSET)

        systems_ams_metadata_counts = cls(
            total=total,
            filtered=filtered,
        )

        systems_ams_metadata_counts.additional_properties = d
        return systems_ams_metadata_counts

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
