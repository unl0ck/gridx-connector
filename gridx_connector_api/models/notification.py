from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        event_type (str | Unset): Type of the event that triggered the notification.
        system_id (UUID | Unset): Identifies the affected system. Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        content (str | Unset): Textual content that is displayed within the dashboard.
        read (bool | Unset): If true, the message has been read by the user, otherwise it was not read yet.
        timestamp (datetime.datetime | Unset): Time at which the event with `eventType` was issued by the notification
            system in UTC in RFC3339 format.
    """

    event_type: str | Unset = UNSET
    system_id: UUID | Unset = UNSET
    content: str | Unset = UNSET
    read: bool | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        system_id: str | Unset = UNSET
        if not isinstance(self.system_id, Unset):
            system_id = str(self.system_id)

        content = self.content

        read = self.read

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if system_id is not UNSET:
            field_dict["systemID"] = system_id
        if content is not UNSET:
            field_dict["content"] = content
        if read is not UNSET:
            field_dict["read"] = read
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = d.pop("eventType", UNSET)

        _system_id = d.pop("systemID", UNSET)
        system_id: UUID | Unset
        if isinstance(_system_id, Unset):
            system_id = UNSET
        else:
            system_id = UUID(_system_id)

        content = d.pop("content", UNSET)

        read = d.pop("read", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        notification = cls(
            event_type=event_type,
            system_id=system_id,
            content=content,
            read=read,
            timestamp=timestamp,
        )

        notification.additional_properties = d
        return notification

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
