from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAccountsAccountIDUsersUserIDNotificationsRulesBodyFilter")


@_attrs_define
class PostAccountsAccountIDUsersUserIDNotificationsRulesBodyFilter:
    """
    Attributes:
        name (str | Unset):
        condition (str | Unset):
    """

    name: str | Unset = UNSET
    condition: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        condition = self.condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        condition = d.pop("condition", UNSET)

        post_accounts_account_id_users_user_id_notifications_rules_body_filter = cls(
            name=name,
            condition=condition,
        )

        post_accounts_account_id_users_user_id_notifications_rules_body_filter.additional_properties = d
        return post_accounts_account_id_users_user_id_notifications_rules_body_filter

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
