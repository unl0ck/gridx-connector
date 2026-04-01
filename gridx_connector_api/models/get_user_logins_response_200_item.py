from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserLoginsResponse200Item")


@_attrs_define
class GetUserLoginsResponse200Item:
    """Represents a user login event that can occur either on login success or failure.

    Attributes:
        created_at (datetime.datetime | Unset): Time when the event occurred in UTC. Example: 2020-11-10T13:13:00Z.
        type_ (str | Unset): The type of the login event. Example: LOGIN_SUCCESS.
        ip (str | Unset): The IP address that caused the login event. Example: 8.8.8.8.
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

        get_user_logins_response_200_item = cls(
            created_at=created_at,
            type_=type_,
            ip=ip,
        )

        get_user_logins_response_200_item.additional_properties = d
        return get_user_logins_response_200_item

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
