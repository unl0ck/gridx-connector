from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthEvent")


@_attrs_define
class AuthEvent:
    """AuthEvent represents auth events such as login, password reset.

    Attributes:
        created_at (datetime.datetime | Unset):
        type_ (str | Unset):
        ip (str | Unset): IP is the IP address of the person who created the event Example: 192.168.178.153.
    """

    created_at: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        type_ = self.type_

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        type_ = d.pop("type", UNSET)

        ip = d.pop("ip", UNSET)

        auth_event = cls(
            created_at=created_at,
            type_=type_,
            ip=ip,
        )

        auth_event.additional_properties = d
        return auth_event

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
