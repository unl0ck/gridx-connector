from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.embedded_accounts_account_kind import EmbeddedAccountsAccountKind
from ..models.embedded_accounts_account_solution import EmbeddedAccountsAccountSolution
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_accounts_account_address import EmbeddedAccountsAccountAddress


T = TypeVar("T", bound="EmbeddedAccountsAccount")


@_attrs_define
class EmbeddedAccountsAccount:
    """An account describes an organizational unit to manage access to systems for one or multiple users.

    Attributes:
        id (UUID): Uniquely identifies the account. Example: 49a4f165-8233-426b-a1a4-e569665a25dd.
        created_at (datetime.datetime): Specifies when the account was created.
        updated_at (datetime.datetime): Specifies when the account was updated.
        name (str | Unset): Name of the account, can be chosen freely but should be kept terse and descriptive. Example:
            John Doe.
        email (str | Unset): The email field of the account can optionally be chosen e.g. for contact purposes (in order
            to reach the responsible person for the account). Example: john@doe.com.
        solution (EmbeddedAccountsAccountSolution | Unset): Represents the supported solutions within the account:
            - HOME if the account contains household-like systems.
            - CHARGE if the account is used solely for charging station fleet management.
            - GENERAL if unsure what the account should contain or if it's a mix of multiple solutions.
            - SMART_DISTRICT if the account is used solely for smart district management.
            If not set, the parent account's solution will be assumed.
        parent_id (UUID | Unset): Parent of the account for a tree-like account structure. Only the root account does
            not have a parent ID. Example: 19a4f165-8233-426b-a1a4-e569665a25dd.
        systems_count (int | Unset): SystemCount is the number of systems assigned to this account Example: 1.
        kind (EmbeddedAccountsAccountKind | Unset): If b2b, the account is a regular account. If end-user, the account
            is a customer account which contains just one user.
        main_address (EmbeddedAccountsAccountAddress | Unset): Represents a physical address of a customer.
        customization (Any | Unset): Customization can be used to store arbitrary data.
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    solution: EmbeddedAccountsAccountSolution | Unset = UNSET
    parent_id: UUID | Unset = UNSET
    systems_count: int | Unset = UNSET
    kind: EmbeddedAccountsAccountKind | Unset = UNSET
    main_address: EmbeddedAccountsAccountAddress | Unset = UNSET
    customization: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        email = self.email

        solution: str | Unset = UNSET
        if not isinstance(self.solution, Unset):
            solution = self.solution.value

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

        systems_count = self.systems_count

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        main_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_address, Unset):
            main_address = self.main_address.to_dict()

        customization = self.customization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if solution is not UNSET:
            field_dict["solution"] = solution
        if parent_id is not UNSET:
            field_dict["parentID"] = parent_id
        if systems_count is not UNSET:
            field_dict["systemsCount"] = systems_count
        if kind is not UNSET:
            field_dict["kind"] = kind
        if main_address is not UNSET:
            field_dict["mainAddress"] = main_address
        if customization is not UNSET:
            field_dict["customization"] = customization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_accounts_account_address import EmbeddedAccountsAccountAddress

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _solution = d.pop("solution", UNSET)
        solution: EmbeddedAccountsAccountSolution | Unset
        if isinstance(_solution, Unset):
            solution = UNSET
        else:
            solution = EmbeddedAccountsAccountSolution(_solution)

        _parent_id = d.pop("parentID", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        systems_count = d.pop("systemsCount", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: EmbeddedAccountsAccountKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = EmbeddedAccountsAccountKind(_kind)

        _main_address = d.pop("mainAddress", UNSET)
        main_address: EmbeddedAccountsAccountAddress | Unset
        if isinstance(_main_address, Unset):
            main_address = UNSET
        else:
            main_address = EmbeddedAccountsAccountAddress.from_dict(_main_address)

        customization = d.pop("customization", UNSET)

        embedded_accounts_account = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            email=email,
            solution=solution,
            parent_id=parent_id,
            systems_count=systems_count,
            kind=kind,
            main_address=main_address,
            customization=customization,
        )

        embedded_accounts_account.additional_properties = d
        return embedded_accounts_account

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
