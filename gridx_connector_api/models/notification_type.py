from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_type_dashboard_notification import NotificationTypeDashboardNotification
    from ..models.notification_type_email import NotificationTypeEmail
    from ..models.notification_type_mobile import NotificationTypeMobile
    from ..models.notification_type_webhook import NotificationTypeWebhook


T = TypeVar("T", bound="NotificationType")


@_attrs_define
class NotificationType:
    """
    Attributes:
        email (NotificationTypeEmail | Unset):
        dashboard_notification (NotificationTypeDashboardNotification | Unset):
        webhook (NotificationTypeWebhook | Unset):
        mobile (NotificationTypeMobile | Unset):
    """

    email: NotificationTypeEmail | Unset = UNSET
    dashboard_notification: NotificationTypeDashboardNotification | Unset = UNSET
    webhook: NotificationTypeWebhook | Unset = UNSET
    mobile: NotificationTypeMobile | Unset = UNSET
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
        from ..models.notification_type_dashboard_notification import NotificationTypeDashboardNotification
        from ..models.notification_type_email import NotificationTypeEmail
        from ..models.notification_type_mobile import NotificationTypeMobile
        from ..models.notification_type_webhook import NotificationTypeWebhook

        d = dict(src_dict)
        _email = d.pop("email", UNSET)
        email: NotificationTypeEmail | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = NotificationTypeEmail.from_dict(_email)

        _dashboard_notification = d.pop("dashboardNotification", UNSET)
        dashboard_notification: NotificationTypeDashboardNotification | Unset
        if isinstance(_dashboard_notification, Unset):
            dashboard_notification = UNSET
        else:
            dashboard_notification = NotificationTypeDashboardNotification.from_dict(_dashboard_notification)

        _webhook = d.pop("webhook", UNSET)
        webhook: NotificationTypeWebhook | Unset
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = NotificationTypeWebhook.from_dict(_webhook)

        _mobile = d.pop("mobile", UNSET)
        mobile: NotificationTypeMobile | Unset
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = NotificationTypeMobile.from_dict(_mobile)

        notification_type = cls(
            email=email,
            dashboard_notification=dashboard_notification,
            webhook=webhook,
            mobile=mobile,
        )

        notification_type.additional_properties = d
        return notification_type

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
