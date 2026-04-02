from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GSPFeatureEnabledStrict")


@_attrs_define
class GSPFeatureEnabledStrict:
    """GSP en/disablement.

    Attributes:
        enabled (bool): En/disables a GSP-feature. Example: True.
    """

    enabled: bool

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        gsp_feature_enabled_strict = cls(
            enabled=enabled,
        )

        return gsp_feature_enabled_strict
