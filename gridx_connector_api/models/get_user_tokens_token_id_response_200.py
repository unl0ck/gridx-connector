from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserTokensTokenIDResponse200")


@_attrs_define
class GetUserTokensTokenIDResponse200:
    """
    Attributes:
        id (UUID):  Example: fc8ee525-669f-45de-9bca-bf5a51829de3.
        created_at (datetime.datetime): Time at which the token was created in UTC using the RFC3339 format. Example:
            2021-10-10T23:20:50Z.
        description (str | Unset):  Example: My api token.
        expires_at (datetime.datetime | Unset): Time at which the token expires in UTC using the RFC3339 format.

            **WARNING** - if `expiresAt` is not set, the token will never expire. We strongly recommend
            that you set an expiration date to help keep your account and information secure.
             Example: 2021-11-10T23:00:00Z.
    """

    id: UUID
    created_at: datetime.datetime
    description: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        description = self.description

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        get_user_tokens_token_id_response_200 = cls(
            id=id,
            created_at=created_at,
            description=description,
            expires_at=expires_at,
        )

        get_user_tokens_token_id_response_200.additional_properties = d
        return get_user_tokens_token_id_response_200

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
