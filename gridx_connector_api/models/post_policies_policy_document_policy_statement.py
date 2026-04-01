from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_policies_policy_document_policy_statement_effect import (
    PostPoliciesPolicyDocumentPolicyStatementEffect,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPoliciesPolicyDocumentPolicyStatement")


@_attrs_define
class PostPoliciesPolicyDocumentPolicyStatement:
    """
    Attributes:
        id (UUID): Unique identifier of the policy statement. Example: 97874c1b-d073-4b06-bf01-a1497fbe1146.
        name (str): Name of the policy statement.
        action (str): The action that this statement represents. An action is an operation on a resource. Example:
            groups:Create.
        effect (PostPoliciesPolicyDocumentPolicyStatementEffect): Whether this statement restricts or grants the
            permission to perform the described action. Example: allow.
        fields (str): Used for fine-grained control over request bodies, e.g. to allow/deny a certain field in the
            payload. Example: *.
        resource (str): Hierarchical structure over resources to control endpoint access.

            For instance, "accounts:*" means that the user can read/modify any account (represented by the wildcard '*').
             Example: accounts:*:groups.
        created_at (datetime.datetime): Date when the policy statement was created in UTC (RFC 3339 format).
        updated_at (datetime.datetime | Unset): Date when the policy statement was last updated in UTC (RFC 3339
            format).
    """

    id: UUID
    name: str
    action: str
    effect: PostPoliciesPolicyDocumentPolicyStatementEffect
    fields: str
    resource: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        action = self.action

        effect = self.effect.value

        fields = self.fields

        resource = self.resource

        created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "action": action,
                "effect": effect,
                "fields": fields,
                "resource": resource,
                "createdAt": created_at,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        action = d.pop("action")

        effect = PostPoliciesPolicyDocumentPolicyStatementEffect(d.pop("effect"))

        fields = d.pop("fields")

        resource = d.pop("resource")

        created_at = isoparse(d.pop("createdAt"))

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        post_policies_policy_document_policy_statement = cls(
            id=id,
            name=name,
            action=action,
            effect=effect,
            fields=fields,
            resource=resource,
            created_at=created_at,
            updated_at=updated_at,
        )

        post_policies_policy_document_policy_statement.additional_properties = d
        return post_policies_policy_document_policy_statement

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
