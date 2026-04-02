from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GSPAssetIDsStrict")


@_attrs_define
class GSPAssetIDsStrict:
    """Array of Asset IDs.

    Attributes:
        asset_i_ds (list[str]): Array of Asset IDs
    """

    asset_i_ds: list[str]

    def to_dict(self) -> dict[str, Any]:
        asset_i_ds = self.asset_i_ds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assetIDs": asset_i_ds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_i_ds = cast(list[str], d.pop("assetIDs"))

        gsp_asset_i_ds_strict = cls(
            asset_i_ds=asset_i_ds,
        )

        return gsp_asset_i_ds_strict
