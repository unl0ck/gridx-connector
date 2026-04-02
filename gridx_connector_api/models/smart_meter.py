from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmartMeter")


@_attrs_define
class SmartMeter:
    """Represents the metadata to report if a smart meter has been installed.

    Attributes:
        installed (bool | None | Unset): Reports if the smart meter has been installed.
        has_installation_date (bool | None | Unset): Reports if the provider has sent us a installation date that can be
            found in energy metadata.
    """

    installed: bool | None | Unset = UNSET
    has_installation_date: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installed: bool | None | Unset
        if isinstance(self.installed, Unset):
            installed = UNSET
        else:
            installed = self.installed

        has_installation_date: bool | None | Unset
        if isinstance(self.has_installation_date, Unset):
            has_installation_date = UNSET
        else:
            has_installation_date = self.has_installation_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installed is not UNSET:
            field_dict["installed"] = installed
        if has_installation_date is not UNSET:
            field_dict["hasInstallationDate"] = has_installation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_installed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        installed = _parse_installed(d.pop("installed", UNSET))

        def _parse_has_installation_date(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_installation_date = _parse_has_installation_date(d.pop("hasInstallationDate", UNSET))

        smart_meter = cls(
            installed=installed,
            has_installation_date=has_installation_date,
        )

        smart_meter.additional_properties = d
        return smart_meter

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
