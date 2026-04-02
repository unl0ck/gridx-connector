from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemAccountAssignmentStrict")


@_attrs_define
class SystemAccountAssignmentStrict:
    """
    Attributes:
        uuids (list[str]): System IDs that will be moved to the target account.
        move_systems_and_customers (bool | Unset): - `true`: Moves the system from the origin account to the target
            account (accountID parameter) and its parent accounts. The customers that belong to that account are also moved
            to the target account.
            - `false`: Assigns the system to the target account (accountID parameter) and its parent accounts.
        move_vendor_id (bool | Unset): `true` by default when moveSystemsAndCustomers is `true`.
              - `true`: Updates the vendorID of the gateway of the specified system to the target accountID.
              - `false`: Does not update the vendorID of the gateway of the specified system.
    """

    uuids: list[str]
    move_systems_and_customers: bool | Unset = UNSET
    move_vendor_id: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuids = self.uuids

        move_systems_and_customers = self.move_systems_and_customers

        move_vendor_id = self.move_vendor_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuids": uuids,
            }
        )
        if move_systems_and_customers is not UNSET:
            field_dict["moveSystemsAndCustomers"] = move_systems_and_customers
        if move_vendor_id is not UNSET:
            field_dict["moveVendorID"] = move_vendor_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuids = cast(list[str], d.pop("uuids"))

        move_systems_and_customers = d.pop("moveSystemsAndCustomers", UNSET)

        move_vendor_id = d.pop("moveVendorID", UNSET)

        system_account_assignment_strict = cls(
            uuids=uuids,
            move_systems_and_customers=move_systems_and_customers,
            move_vendor_id=move_vendor_id,
        )

        system_account_assignment_strict.additional_properties = d
        return system_account_assignment_strict

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
