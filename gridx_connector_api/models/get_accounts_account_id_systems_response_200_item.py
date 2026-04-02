from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accounts_account_id_systems_response_200_item_users_item import (
        GetAccountsAccountIDSystemsResponse200ItemUsersItem,
    )


T = TypeVar("T", bound="GetAccountsAccountIDSystemsResponse200Item")


@_attrs_define
class GetAccountsAccountIDSystemsResponse200Item:
    """
    Attributes:
        users (list[GetAccountsAccountIDSystemsResponse200ItemUsersItem] | Unset): The users belonging to this system.
            Only set if `embed` query parameter includes `user`.
    """

    users: list[GetAccountsAccountIDSystemsResponse200ItemUsersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accounts_account_id_systems_response_200_item_users_item import (
            GetAccountsAccountIDSystemsResponse200ItemUsersItem,
        )

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[GetAccountsAccountIDSystemsResponse200ItemUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = GetAccountsAccountIDSystemsResponse200ItemUsersItem.from_dict(users_item_data)

                users.append(users_item)

        get_accounts_account_id_systems_response_200_item = cls(
            users=users,
        )

        get_accounts_account_id_systems_response_200_item.additional_properties = d
        return get_accounts_account_id_systems_response_200_item

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
