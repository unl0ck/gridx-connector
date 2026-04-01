from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notifications_rule_set_strict_filter import NotificationsRuleSetStrictFilter
    from ..models.notifications_rule_set_strict_notification_type import NotificationsRuleSetStrictNotificationType


T = TypeVar("T", bound="NotificationsRuleSetStrict")


@_attrs_define
class NotificationsRuleSetStrict:
    """
    Attributes:
        event_type (str | Unset):
        filters (list[NotificationsRuleSetStrictFilter] | Unset):
        notification_type (NotificationsRuleSetStrictNotificationType | Unset):
        locale (str | Unset):
    """

    event_type: str | Unset = UNSET
    filters: list[NotificationsRuleSetStrictFilter] | Unset = UNSET
    notification_type: NotificationsRuleSetStrictNotificationType | Unset = UNSET
    locale: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        notification_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.to_dict()

        locale = self.locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if filters is not UNSET:
            field_dict["filters"] = filters
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notifications_rule_set_strict_filter import NotificationsRuleSetStrictFilter
        from ..models.notifications_rule_set_strict_notification_type import NotificationsRuleSetStrictNotificationType

        d = dict(src_dict)
        event_type = d.pop("eventType", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[NotificationsRuleSetStrictFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = NotificationsRuleSetStrictFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        _notification_type = d.pop("notificationType", UNSET)
        notification_type: NotificationsRuleSetStrictNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = NotificationsRuleSetStrictNotificationType.from_dict(_notification_type)

        locale = d.pop("locale", UNSET)

        notifications_rule_set_strict = cls(
            event_type=event_type,
            filters=filters,
            notification_type=notification_type,
            locale=locale,
        )

        notifications_rule_set_strict.additional_properties = d
        return notifications_rule_set_strict

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
