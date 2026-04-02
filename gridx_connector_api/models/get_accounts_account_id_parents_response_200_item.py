from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAccountsAccountIDParentsResponse200Item")


@_attrs_define
class GetAccountsAccountIDParentsResponse200Item:
    """
    Attributes:
        account_id (str):
        audience (str | Unset):
    """

    account_id: str
    audience: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountID": account_id,
            }
        )
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountID")

        audience = d.pop("audience", UNSET)

        get_accounts_account_id_parents_response_200_item = cls(
            account_id=account_id,
            audience=audience,
        )

        get_accounts_account_id_parents_response_200_item.additional_properties = d
        return get_accounts_account_id_parents_response_200_item

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
