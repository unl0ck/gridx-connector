from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncEntitySettings")


@_attrs_define
class SyncEntitySettings:
    """SyncEntitySettings configures entity synchronisation parameters.

    Attributes:
        sync_interval (float | None | Unset): SyncInterval defines the period in seconds for data to be synchronized
            between gridBox and cloud DER API.
        ttl (float | None | Unset): TTL defines the time to live in seconds for entity.
        disabled (bool | Unset): Disabled disables the sync of entities.
    """

    sync_interval: float | None | Unset = UNSET
    ttl: float | None | Unset = UNSET
    disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_interval: float | None | Unset
        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        else:
            sync_interval = self.sync_interval

        ttl: float | None | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_interval is not UNSET:
            field_dict["syncInterval"] = sync_interval
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_sync_interval(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sync_interval = _parse_sync_interval(d.pop("syncInterval", UNSET))

        def _parse_ttl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        disabled = d.pop("disabled", UNSET)

        sync_entity_settings = cls(
            sync_interval=sync_interval,
            ttl=ttl,
            disabled=disabled,
        )

        sync_entity_settings.additional_properties = d
        return sync_entity_settings

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
