from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemsResponse200ItemUsersItemPolicyGroup")


@_attrs_define
class GetSystemsResponse200ItemUsersItemPolicyGroup:
    """
    Attributes:
        name (str): Name of the policy group. Example: group name.
        id (UUID): Unique identifier of the policy group. Example: 97874c1b-d073-4b06-bf01-a1497fbe1146.
        account_id (UUID): Unique identifier of the creator account. Example: 97874c1b-d073-4b06-bf01-a1497fbe1146.
        created_at (datetime.datetime): Time at which the policy group was created in UTC (RFC 3339 format). Example:
            2019-11-06T15:33:00Z.
        updated_at (datetime.datetime): Time at which the policy group was last updated in UTC (RFC 3339 format).
            Example: 2019-11-08T23:20:50Z.
        description (str | Unset): Description of the group, omitted if empty Example: Group provides read-access to
            accounts.
        user_count (int | Unset): Amount of users that are in this group. Example: 10.
    """

    name: str
    id: UUID
    account_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    user_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        account_id = str(self.account_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        user_count = self.user_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "accountID": account_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if user_count is not UNSET:
            field_dict["userCount"] = user_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        account_id = UUID(d.pop("accountID"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        description = d.pop("description", UNSET)

        user_count = d.pop("userCount", UNSET)

        get_systems_response_200_item_users_item_policy_group = cls(
            name=name,
            id=id,
            account_id=account_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            user_count=user_count,
        )

        get_systems_response_200_item_users_item_policy_group.additional_properties = d
        return get_systems_response_200_item_users_item_policy_group

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
