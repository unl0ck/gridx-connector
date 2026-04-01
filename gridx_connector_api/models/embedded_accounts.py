from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_accounts_account import EmbeddedAccountsAccount


T = TypeVar("T", bound="EmbeddedAccounts")


@_attrs_define
class EmbeddedAccounts:
    """Hierarchy of accounts the system belongs to, from the authenticated account down to the end customer's.

    Attributes:
        accounts (list[EmbeddedAccountsAccount] | Unset):
    """

    accounts: list[EmbeddedAccountsAccount] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_accounts_account import EmbeddedAccountsAccount

        d = dict(src_dict)
        _accounts = d.pop("accounts", UNSET)
        accounts: list[EmbeddedAccountsAccount] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = EmbeddedAccountsAccount.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        embedded_accounts = cls(
            accounts=accounts,
        )

        embedded_accounts.additional_properties = d
        return embedded_accounts

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
