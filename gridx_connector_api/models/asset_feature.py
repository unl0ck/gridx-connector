from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_feature_features_item import AssetFeatureFeaturesItem


T = TypeVar("T", bound="AssetFeature")


@_attrs_define
class AssetFeature:
    """Asset GSP feature.

    Attributes:
        asset_id (UUID | Unset): Unique identifier of an asset. Example: 19a4f165-8233-426b-a1a4-e569665a25dd.
        features (list[AssetFeatureFeaturesItem] | Unset):
    """

    asset_id: UUID | Unset = UNSET
    features: list[AssetFeatureFeaturesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetID"] = asset_id
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_feature_features_item import AssetFeatureFeaturesItem

        d = dict(src_dict)
        _asset_id = d.pop("assetID", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _features = d.pop("features", UNSET)
        features: list[AssetFeatureFeaturesItem] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = AssetFeatureFeaturesItem.from_dict(features_item_data)

                features.append(features_item)

        asset_feature = cls(
            asset_id=asset_id,
            features=features,
        )

        asset_feature.additional_properties = d
        return asset_feature

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
