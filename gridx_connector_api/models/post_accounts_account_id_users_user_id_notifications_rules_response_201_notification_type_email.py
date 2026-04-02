from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail")


@_attrs_define
class PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail:
    """
    Attributes:
        address (str):
    """

    address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_email = cls(
            address=address,
        )

        post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_email.additional_properties = d
        return post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_email

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
