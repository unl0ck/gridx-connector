from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAccountsAccountIDSystemsResponse200ItemUsersItemLanguage")


@_attrs_define
class GetAccountsAccountIDSystemsResponse200ItemUsersItemLanguage:
    """The language information of the user.

    Attributes:
        tag (str): Tag is the IETF language tag's primary identifier for this language.

            See [here](https://tools.ietf.org/rfc/bcp/bcp47.txt) and the example below for more information.
             Example: de_DE.
        name (str): The name of the language in English. Example: German.
        name_native (str): The name of the language in the language itself. Example: Deutsch.
    """

    tag: str
    name: str
    name_native: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        name = self.name

        name_native = self.name_native

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
                "name": name,
                "nameNative": name_native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag = d.pop("tag")

        name = d.pop("name")

        name_native = d.pop("nameNative")

        get_accounts_account_id_systems_response_200_item_users_item_language = cls(
            tag=tag,
            name=name,
            name_native=name_native,
        )

        get_accounts_account_id_systems_response_200_item_users_item_language.additional_properties = d
        return get_accounts_account_id_systems_response_200_item_users_item_language

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
