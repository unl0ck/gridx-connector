from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyGroupCreate")


@_attrs_define
class PolicyGroupCreate:
    """
    Attributes:
        name (str): Name of the policy group. Example: group name.
        description (str | Unset): Description of the group, omitted if empty Example: Group provides read-access to
            accounts.
        account_id (UUID | Unset): Unique identifier of the creator account. Example:
            97874c1b-d073-4b06-bf01-a1497fbe1146.
        policies (list[UUID] | Unset): the ID's of the policy documents that the group should be assigned to. Example:
            ['532365fc-5a0e-4323-bc66-4ce9f1308480'].
    """

    name: str
    description: str | Unset = UNSET
    account_id: UUID | Unset = UNSET
    policies: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        policies: list[str] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = str(policies_item_data)
                policies.append(policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if policies is not UNSET:
            field_dict["policies"] = policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _account_id = d.pop("accountID", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        _policies = d.pop("policies", UNSET)
        policies: list[UUID] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = UUID(policies_item_data)

                policies.append(policies_item)

        policy_group_create = cls(
            name=name,
            description=description,
            account_id=account_id,
            policies=policies,
        )

        policy_group_create.additional_properties = d
        return policy_group_create

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
