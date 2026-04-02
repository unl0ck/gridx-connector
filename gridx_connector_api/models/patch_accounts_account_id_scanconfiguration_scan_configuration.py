from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAccountsAccountIDScanconfigurationScanConfiguration")


@_attrs_define
class PatchAccountsAccountIDScanconfigurationScanConfiguration:
    """ScanConfiguration determines the behavior of a scan.

    Attributes:
        account_id (UUID | Unset): The account ID the configuration belongs to. Example:
            6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        configuration (list[str] | Unset): The names of the scanners in this configuration.
        created_at (datetime.datetime | Unset): Date when the configuration was created.
        updated_at (datetime.datetime | Unset): Date when the configuration was updated the last time.
    """

    account_id: UUID | Unset = UNSET
    configuration: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        configuration: list[str] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _account_id = d.pop("accountID", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        configuration = cast(list[str], d.pop("configuration", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patch_accounts_account_id_scanconfiguration_scan_configuration = cls(
            account_id=account_id,
            configuration=configuration,
            created_at=created_at,
            updated_at=updated_at,
        )

        patch_accounts_account_id_scanconfiguration_scan_configuration.additional_properties = d
        return patch_accounts_account_id_scanconfiguration_scan_configuration

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
