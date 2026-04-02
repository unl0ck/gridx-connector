from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_statement_effect import PolicyStatementEffect
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyStatement")


@_attrs_define
class PolicyStatement:
    """A policy statement grants or restricts the permission to perform an action.

    Attributes:
        name (str): Name of the policy statement.
        action (str): The action that this statement represents. An action is an operation on a resource. Example:
            groups:Create.
        effect (PolicyStatementEffect): Whether this statement restricts or grants the permission to perform the
            described action. Example: allow.
        fields (str): Used for fine-grained control over request bodies, e.g. to allow/deny a certain field in the
            payload. Example: *.
        resource (str): Hierarchical structure over resources to control endpoint access.

            For instance, "accounts:*" means that the user can read/modify any account (represented by the wildcard '*').
             Example: accounts:*:groups.
        id (UUID | Unset): Unique identifier of the policy statement. Example: 97874c1b-d073-4b06-bf01-a1497fbe1146.
    """

    name: str
    action: str
    effect: PolicyStatementEffect
    fields: str
    resource: str
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action = self.action

        effect = self.effect.value

        fields = self.fields

        resource = self.resource

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action": action,
                "effect": effect,
                "fields": fields,
                "resource": resource,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        action = d.pop("action")

        effect = PolicyStatementEffect(d.pop("effect"))

        fields = d.pop("fields")

        resource = d.pop("resource")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        policy_statement = cls(
            name=name,
            action=action,
            effect=effect,
            fields=fields,
            resource=resource,
            id=id,
        )

        policy_statement.additional_properties = d
        return policy_statement

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
