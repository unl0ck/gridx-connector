from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationalAPITokenCreation")


@_attrs_define
class OrganizationalAPITokenCreation:
    """
    Attributes:
        email (str | Unset): Used to specify the email address associated with the user responsible for the
            organizational token upon its creation (account email is used by default). Example: john@doe.com.
        groups (list[str] | Unset): Used to specify the permissions assigned to the organizational token.
    """

    email: str | Unset = UNSET
    groups: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        organizational_api_token_creation = cls(
            email=email,
            groups=groups,
        )

        organizational_api_token_creation.additional_properties = d
        return organizational_api_token_creation

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
