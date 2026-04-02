from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organizational_api_token_user import OrganizationalAPITokenUser


T = TypeVar("T", bound="OrganizationalAPIToken")


@_attrs_define
class OrganizationalAPIToken:
    """
    Attributes:
        user (OrganizationalAPITokenUser):
        user_id (UUID): Reference to the user to which the API token belongs. Can be used to set the token's "scope" by
            assigning groups to the user. Example: 123ee525-669f-45de-9bca-bf5a51829de3.
    """

    user: OrganizationalAPITokenUser
    user_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "userID": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organizational_api_token_user import OrganizationalAPITokenUser

        d = dict(src_dict)
        user = OrganizationalAPITokenUser.from_dict(d.pop("user"))

        user_id = UUID(d.pop("userID"))

        organizational_api_token = cls(
            user=user,
            user_id=user_id,
        )

        organizational_api_token.additional_properties = d
        return organizational_api_token

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
