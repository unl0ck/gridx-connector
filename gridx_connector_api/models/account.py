from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_solution import AccountSolution
from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """An account describes an organizational unit to manage access to systems for one or multiple users.

    This is the base type for the more concrete usages and not used directly within operations.

        Attributes:
            name (str | Unset): Name of the account, can be chosen freely but should be kept terse and descriptive. Example:
                John Doe.
            email (str | Unset): The email field of the account can optionally be chosen e.g. for contact purposes (in order
                to reach the responsible person for the account). Example: john@doe.com.
            solution (AccountSolution | Unset): Represents the supported solutions within the account:
                - HOME if the account contains household-like systems.
                - CHARGE if the account is used solely for charging station fleet management.
                - GENERAL if unsure what the account should contain or if it's a mix of multiple solutions.
                - SMART_DISTRICT if the account is used solely for smart district management.
                If not set, the parent account's solution will be assumed.
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    solution: AccountSolution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        solution: str | Unset = UNSET
        if not isinstance(self.solution, Unset):
            solution = self.solution.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if solution is not UNSET:
            field_dict["solution"] = solution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _solution = d.pop("solution", UNSET)
        solution: AccountSolution | Unset
        if isinstance(_solution, Unset):
            solution = UNSET
        else:
            solution = AccountSolution(_solution)

        account = cls(
            name=name,
            email=email,
            solution=solution,
        )

        account.additional_properties = d
        return account

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
