from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserNotificationsNotificationIDResponse200")


@_attrs_define
class GetUserNotificationsNotificationIDResponse200:
    """
    Attributes:
        event_type (str): Type of the event that triggered the notification.
        content (str): Textual content that is displayed within the dashboard.
        read (bool): If true, the message has been read by the user, otherwise it was not read yet.
        timestamp (datetime.datetime): Time at which the event with `eventType` was issued by the notification system in
            UTC in RFC3339 format.
        id (UUID): Uniquely identifies the notification. Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        user_id (UUID): User ID of the recipient. Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        created_at (datetime.datetime): Time at which the notification was created in UTC in RFC3339 format.
        updated_at (datetime.datetime): Time at which the notification was updated in UTC in RFC3339 format.
        system_id (UUID | Unset): Identifies the affected system. Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
    """

    event_type: str
    content: str
    read: bool
    timestamp: datetime.datetime
    id: UUID
    user_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    system_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        content = self.content

        read = self.read

        timestamp = self.timestamp.isoformat()

        id = str(self.id)

        user_id = str(self.user_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        system_id: str | Unset = UNSET
        if not isinstance(self.system_id, Unset):
            system_id = str(self.system_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "content": content,
                "read": read,
                "timestamp": timestamp,
                "id": id,
                "userID": user_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if system_id is not UNSET:
            field_dict["systemID"] = system_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = d.pop("eventType")

        content = d.pop("content")

        read = d.pop("read")

        timestamp = isoparse(d.pop("timestamp"))

        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("userID"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _system_id = d.pop("systemID", UNSET)
        system_id: UUID | Unset
        if isinstance(_system_id, Unset):
            system_id = UNSET
        else:
            system_id = UUID(_system_id)

        get_user_notifications_notification_id_response_200 = cls(
            event_type=event_type,
            content=content,
            read=read,
            timestamp=timestamp,
            id=id,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            system_id=system_id,
        )

        get_user_notifications_notification_id_response_200.additional_properties = d
        return get_user_notifications_notification_id_response_200

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
