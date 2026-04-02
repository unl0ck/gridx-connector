from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse200NotificationTypeDashboardNotification"
)


@_attrs_define
class GetAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse200NotificationTypeDashboardNotification:
    """
    Attributes:
        user_id (str):
        end_user (bool | Unset):
    """

    user_id: str
    end_user: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        end_user = self.end_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userID": user_id,
            }
        )
        if end_user is not UNSET:
            field_dict["endUser"] = end_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userID")

        end_user = d.pop("endUser", UNSET)

        get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_dashboard_notification = cls(
            user_id=user_id,
            end_user=end_user,
        )

        get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_dashboard_notification.additional_properties = d
        return get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_dashboard_notification

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
