from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gsp_feature import GSPFeature

T = TypeVar("T", bound="GSP")


@_attrs_define
class GSP:
    """GSP-feature.

    Attributes:
        enabled (bool): Enabled is true if the GSP-feature is enabled Example: True.
        feature (GSPFeature): Name of the GSP-feature.
    """

    enabled: bool
    feature: GSPFeature
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        feature = self.feature.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "feature": feature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        feature = GSPFeature(d.pop("feature"))

        gsp = cls(
            enabled=enabled,
            feature=feature,
        )

        gsp.additional_properties = d
        return gsp

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
