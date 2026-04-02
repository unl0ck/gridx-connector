from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBodyNotificationTypeWebhook")


@_attrs_define
class PutAccountsAccountIDUsersUserIDNotificationsRulesRuleIDBodyNotificationTypeWebhook:
    """
    Attributes:
        target_url (str):
        secret (str):
    """

    target_url: str
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_url = self.target_url

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetURL": target_url,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_url = d.pop("targetURL")

        secret = d.pop("secret")

        put_accounts_account_id_users_user_id_notifications_rules_rule_id_body_notification_type_webhook = cls(
            target_url=target_url,
            secret=secret,
        )

        put_accounts_account_id_users_user_id_notifications_rules_rule_id_body_notification_type_webhook.additional_properties = d
        return put_accounts_account_id_users_user_id_notifications_rules_rule_id_body_notification_type_webhook

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
