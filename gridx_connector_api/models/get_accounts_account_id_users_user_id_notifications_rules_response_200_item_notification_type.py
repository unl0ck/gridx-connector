from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_dashboard_notification import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification,
    )
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_email import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail,
    )
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_mobile import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile,
    )
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_webhook import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook,
    )


T = TypeVar("T", bound="GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType")


@_attrs_define
class GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType:
    """
    Attributes:
        email (GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail | Unset):
        dashboard_notification
            (GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification | Unset):
        webhook (GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook | Unset):
        mobile (GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile | Unset):
    """

    email: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail | Unset = UNSET
    dashboard_notification: (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification | Unset
    ) = UNSET
    webhook: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook | Unset = UNSET
    mobile: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        dashboard_notification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dashboard_notification, Unset):
            dashboard_notification = self.dashboard_notification.to_dict()

        webhook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook, Unset):
            webhook = self.webhook.to_dict()

        mobile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if dashboard_notification is not UNSET:
            field_dict["dashboardNotification"] = dashboard_notification
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_dashboard_notification import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification,
        )
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_email import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail,
        )
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_mobile import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile,
        )
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type_webhook import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook,
        )

        d = dict(src_dict)
        _email = d.pop("email", UNSET)
        email: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeEmail.from_dict(
                _email
            )

        _dashboard_notification = d.pop("dashboardNotification", UNSET)
        dashboard_notification: (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification
            | Unset
        )
        if isinstance(_dashboard_notification, Unset):
            dashboard_notification = UNSET
        else:
            dashboard_notification = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeDashboardNotification.from_dict(
                _dashboard_notification
            )

        _webhook = d.pop("webhook", UNSET)
        webhook: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook | Unset
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeWebhook.from_dict(
                _webhook
            )

        _mobile = d.pop("mobile", UNSET)
        mobile: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile | Unset
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationTypeMobile.from_dict(
                _mobile
            )

        get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type = cls(
            email=email,
            dashboard_notification=dashboard_notification,
            webhook=webhook,
            mobile=mobile,
        )

        get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type.additional_properties = d
        return get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type

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
