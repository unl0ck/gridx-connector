from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Gateway")


@_attrs_define
class Gateway:
    """A gateway used to monitor and control appliances.

    For instance, our beloved gridbox is a gateway.

        Attributes:
            name (str | Unset): Name of the gateway.
            debug_mode_until (datetime.datetime | Unset): Date until which debug messages are logged in RFC3339 format.
    """

    name: str | Unset = UNSET
    debug_mode_until: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        debug_mode_until: str | Unset = UNSET
        if not isinstance(self.debug_mode_until, Unset):
            debug_mode_until = self.debug_mode_until.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if debug_mode_until is not UNSET:
            field_dict["debugModeUntil"] = debug_mode_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _debug_mode_until = d.pop("debugModeUntil", UNSET)
        debug_mode_until: datetime.datetime | Unset
        if isinstance(_debug_mode_until, Unset):
            debug_mode_until = UNSET
        else:
            debug_mode_until = isoparse(_debug_mode_until)

        gateway = cls(
            name=name,
            debug_mode_until=debug_mode_until,
        )

        gateway.additional_properties = d
        return gateway

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
