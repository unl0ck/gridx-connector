from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_accounts_account_id_groups_group_id_policies_policy_document_policy_statement import (
        GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocumentPolicyStatement,
    )


T = TypeVar("T", bound="GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument")


@_attrs_define
class GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocument:
    """
    Attributes:
        name (str): Name of the policy. Example: Default Policy.
        version (str): Version of the policy. Example: Default Policy.
        id (UUID): Unique identifier of the policy document. Example: 97874c1b-d073-4b06-bf01-a1497fbe1146.
        created_at (datetime.datetime): Date when the policy was created in UTC (RFC 3339 format).
        updated_at (datetime.datetime): Date when the policy was last updated in UTC (RFC 3339 format).
        statements (list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocumentPolicyStatement]):
    """

    name: str
    version: str
    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    statements: list[GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocumentPolicyStatement]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        statements = []
        for statements_item_data in self.statements:
            statements_item = statements_item_data.to_dict()
            statements.append(statements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "statements": statements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accounts_account_id_groups_group_id_policies_policy_document_policy_statement import (
            GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocumentPolicyStatement,
        )

        d = dict(src_dict)
        name = d.pop("name")

        version = d.pop("version")

        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        statements = []
        _statements = d.pop("statements")
        for statements_item_data in _statements:
            statements_item = GetAccountsAccountIDGroupsGroupIDPoliciesPolicyDocumentPolicyStatement.from_dict(
                statements_item_data
            )

            statements.append(statements_item)

        get_accounts_account_id_groups_group_id_policies_policy_document = cls(
            name=name,
            version=version,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            statements=statements,
        )

        get_accounts_account_id_groups_group_id_policies_policy_document.additional_properties = d
        return get_accounts_account_id_groups_group_id_policies_policy_document

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
