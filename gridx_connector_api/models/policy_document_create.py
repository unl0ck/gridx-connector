from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_document_create_policy_statement import PolicyDocumentCreatePolicyStatement


T = TypeVar("T", bound="PolicyDocumentCreate")


@_attrs_define
class PolicyDocumentCreate:
    """
    Attributes:
        name (str): Name of the policy. Example: Default Policy.
        version (str): Version of the policy. Example: Default Policy.
        statements (list[PolicyDocumentCreatePolicyStatement] | Unset):
    """

    name: str
    version: str
    statements: list[PolicyDocumentCreatePolicyStatement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        statements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statements, Unset):
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
            }
        )
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_document_create_policy_statement import PolicyDocumentCreatePolicyStatement

        d = dict(src_dict)
        name = d.pop("name")

        version = d.pop("version")

        _statements = d.pop("statements", UNSET)
        statements: list[PolicyDocumentCreatePolicyStatement] | Unset = UNSET
        if _statements is not UNSET:
            statements = []
            for statements_item_data in _statements:
                statements_item = PolicyDocumentCreatePolicyStatement.from_dict(statements_item_data)

                statements.append(statements_item)

        policy_document_create = cls(
            name=name,
            version=version,
            statements=statements,
        )

        policy_document_create.additional_properties = d
        return policy_document_create

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
