from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_update_kind import AccountUpdateKind
from ..models.account_update_solution import AccountUpdateSolution
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_update_address import AccountUpdateAddress


T = TypeVar("T", bound="AccountUpdate")


@_attrs_define
class AccountUpdate:
    """
    Attributes:
        name (str | Unset): Name of the account, can be chosen freely but should be kept terse and descriptive. Example:
            John Doe.
        email (str | Unset): The email field of the account can optionally be chosen e.g. for contact purposes (in order
            to reach the responsible person for the account). Example: john@doe.com.
        solution (AccountUpdateSolution | Unset): Represents the supported solutions within the account:
            - HOME if the account contains household-like systems.
            - CHARGE if the account is used solely for charging station fleet management.
            - GENERAL if unsure what the account should contain or if it's a mix of multiple solutions.
            - SMART_DISTRICT if the account is used solely for smart district management.
            If not set, the parent account's solution will be assumed.
        kind (AccountUpdateKind | Unset): If b2b, the account is a regular account. If end-user, the account is a
            customer account which contains just one user.
        customization (Any | Unset): Customization can be used to store arbitrary data.
        main_address (AccountUpdateAddress | Unset): Represents a physical address of a customer.
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    solution: AccountUpdateSolution | Unset = UNSET
    kind: AccountUpdateKind | Unset = UNSET
    customization: Any | Unset = UNSET
    main_address: AccountUpdateAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        solution: str | Unset = UNSET
        if not isinstance(self.solution, Unset):
            solution = self.solution.value

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        customization = self.customization

        main_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_address, Unset):
            main_address = self.main_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if solution is not UNSET:
            field_dict["solution"] = solution
        if kind is not UNSET:
            field_dict["kind"] = kind
        if customization is not UNSET:
            field_dict["customization"] = customization
        if main_address is not UNSET:
            field_dict["mainAddress"] = main_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_update_address import AccountUpdateAddress

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _solution = d.pop("solution", UNSET)
        solution: AccountUpdateSolution | Unset
        if isinstance(_solution, Unset):
            solution = UNSET
        else:
            solution = AccountUpdateSolution(_solution)

        _kind = d.pop("kind", UNSET)
        kind: AccountUpdateKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = AccountUpdateKind(_kind)

        customization = d.pop("customization", UNSET)

        _main_address = d.pop("mainAddress", UNSET)
        main_address: AccountUpdateAddress | Unset
        if isinstance(_main_address, Unset):
            main_address = UNSET
        else:
            main_address = AccountUpdateAddress.from_dict(_main_address)

        account_update = cls(
            name=name,
            email=email,
            solution=solution,
            kind=kind,
            customization=customization,
            main_address=main_address,
        )

        account_update.additional_properties = d
        return account_update

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
