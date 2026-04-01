from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_dashboard_notification import (
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification,
    )
    from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_email import (
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail,
    )
    from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_mobile import (
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile,
    )
    from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_webhook import (
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook,
    )


T = TypeVar("T", bound="PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationType")


@_attrs_define
class PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationType:
    """
    Attributes:
        email (PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail | Unset):
        dashboard_notification
            (PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification | Unset):
        webhook (PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook | Unset):
        mobile (PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile | Unset):
    """

    email: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail | Unset = UNSET
    dashboard_notification: (
        PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification | Unset
    ) = UNSET
    webhook: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook | Unset = UNSET
    mobile: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile | Unset = UNSET
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
        from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_dashboard_notification import (
            PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification,
        )
        from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_email import (
            PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail,
        )
        from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_mobile import (
            PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile,
        )
        from ..models.post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type_webhook import (
            PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook,
        )

        d = dict(src_dict)
        _email = d.pop("email", UNSET)
        email: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeEmail.from_dict(_email)

        _dashboard_notification = d.pop("dashboardNotification", UNSET)
        dashboard_notification: (
            PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification | Unset
        )
        if isinstance(_dashboard_notification, Unset):
            dashboard_notification = UNSET
        else:
            dashboard_notification = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeDashboardNotification.from_dict(
                _dashboard_notification
            )

        _webhook = d.pop("webhook", UNSET)
        webhook: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook | Unset
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeWebhook.from_dict(
                _webhook
            )

        _mobile = d.pop("mobile", UNSET)
        mobile: PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile | Unset
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = PostAccountsAccountIDUsersUserIDNotificationsRulesResponse201NotificationTypeMobile.from_dict(
                _mobile
            )

        post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type = cls(
            email=email,
            dashboard_notification=dashboard_notification,
            webhook=webhook,
            mobile=mobile,
        )

        post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type.additional_properties = d
        return post_accounts_account_id_users_user_id_notifications_rules_response_201_notification_type

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
