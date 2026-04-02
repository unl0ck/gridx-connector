from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.systems_ams_metadata_counts import SystemsAMSMetadataCounts


T = TypeVar("T", bound="SystemsAMSMetadata")


@_attrs_define
class SystemsAMSMetadata:
    """Provides information about the returned object, such as length of the list and distinct values.

    Attributes:
        counts (SystemsAMSMetadataCounts | Unset): This will only be available if the response is a list or contains
            multiple items. It provides multiple
            "counts" of the list that is being returned.
    """

    counts: SystemsAMSMetadataCounts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.systems_ams_metadata_counts import SystemsAMSMetadataCounts

        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: SystemsAMSMetadataCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = SystemsAMSMetadataCounts.from_dict(_counts)

        systems_ams_metadata = cls(
            counts=counts,
        )

        systems_ams_metadata.additional_properties = d
        return systems_ams_metadata

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
