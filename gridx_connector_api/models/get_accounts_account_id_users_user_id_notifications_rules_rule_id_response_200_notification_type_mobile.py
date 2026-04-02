from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse200NotificationTypeMobile")


@_attrs_define
class GetAccountsAccountIDUsersUserIDNotificationsRulesRuleIDResponse200NotificationTypeMobile:
    """
    Attributes:
        app_name (str | Unset):
        os (str | Unset):
        device_token (str | Unset):
    """

    app_name: str | Unset = UNSET
    os: str | Unset = UNSET
    device_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        os = self.os

        device_token = self.device_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if os is not UNSET:
            field_dict["os"] = os
        if device_token is not UNSET:
            field_dict["deviceToken"] = device_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_name = d.pop("appName", UNSET)

        os = d.pop("os", UNSET)

        device_token = d.pop("deviceToken", UNSET)

        get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_mobile = cls(
            app_name=app_name,
            os=os,
            device_token=device_token,
        )

        get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_mobile.additional_properties = d
        return get_accounts_account_id_users_user_id_notifications_rules_rule_id_response_200_notification_type_mobile

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
