from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_filter import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter,
    )
    from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type import (
        GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType,
    )


T = TypeVar("T", bound="GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item")


@_attrs_define
class GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200Item:
    """
    Attributes:
        event_type (str | Unset):
        filters (list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter] | Unset):
        notification_type (GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType | Unset):
        locale (str | Unset):
        id (UUID | Unset):  Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        account_id (UUID | Unset):  Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        user_id (UUID | Unset):  Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
    """

    event_type: str | Unset = UNSET
    filters: list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter] | Unset = UNSET
    notification_type: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType | Unset = UNSET
    locale: str | Unset = UNSET
    id: UUID | Unset = UNSET
    account_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

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
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_filter import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter,
        )
        from ..models.get_accounts_account_id_users_user_id_notifications_rules_response_200_item_notification_type import (
            GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType,
        )

        d = dict(src_dict)
        event_type = d.pop("eventType", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemFilter.from_dict(
                    filters_item_data
                )

                filters.append(filters_item)

        _notification_type = d.pop("notificationType", UNSET)
        notification_type: GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = (
                GetAccountsAccountIDUsersUserIDNotificationsRulesResponse200ItemNotificationType.from_dict(
                    _notification_type
                )
            )

        locale = d.pop("locale", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _account_id = d.pop("accountID", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        _user_id = d.pop("userID", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        get_accounts_account_id_users_user_id_notifications_rules_response_200_item = cls(
            event_type=event_type,
            filters=filters,
            notification_type=notification_type,
            locale=locale,
            id=id,
            account_id=account_id,
            user_id=user_id,
        )

        get_accounts_account_id_users_user_id_notifications_rules_response_200_item.additional_properties = d
        return get_accounts_account_id_users_user_id_notifications_rules_response_200_item

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
