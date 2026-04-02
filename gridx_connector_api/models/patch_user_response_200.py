from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_user_response_200_address import PatchUserResponse200Address
    from ..models.patch_user_response_200_language import PatchUserResponse200Language
    from ..models.patch_user_response_200_policy_group import PatchUserResponse200PolicyGroup


T = TypeVar("T", bound="PatchUserResponse200")


@_attrs_define
class PatchUserResponse200:
    """
    Attributes:
        id (UUID): Unique identifier of the user. Example: 43a4f165-8233-426b-a1a4-e569665a25dd.
        created_at (datetime.datetime): Time at which the user was created in UTC using the RFC3339 format. Example:
            2009-11-10T23:20:50Z.
        updated_at (datetime.datetime): Time at which the user was last updated in UTC using the RFC3339 format.
            Example: 2009-11-10T23:20:50Z.
        email (str): The email address of the user that is used for login. Example: john@doe.com.
        account_id (UUID | Unset): Unique identifier of the account that the user belongs to. Example:
            6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        new_password (str | Unset): Used to set a new password for the user.
        logins_count (int | Unset): Number of user logins.
        mfa_enabled (bool | Unset): Indicates whether MFA (Multi-Factor Authentication) is enabled.
        mfa_reset (bool | Unset): Can be set to true if MFA (Multi-Factor Authentication) needs to to be reset. This
            will remove the MFA.
        full_name (str | Unset): Full name of the user typically consisting of first name and last name. Example: John
            Doe.
        groups (list[PatchUserResponse200PolicyGroup] | Unset): Policy groups attached to this user which determine the
            effective permissions through policies.
        main_address (PatchUserResponse200Address | Unset): Represents a physical address of a customer.
        language (PatchUserResponse200Language | Unset): The language information of the user.
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email: str
    account_id: UUID | Unset = UNSET
    new_password: str | Unset = UNSET
    logins_count: int | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    mfa_reset: bool | Unset = UNSET
    full_name: str | Unset = UNSET
    groups: list[PatchUserResponse200PolicyGroup] | Unset = UNSET
    main_address: PatchUserResponse200Address | Unset = UNSET
    language: PatchUserResponse200Language | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email = self.email

        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        new_password = self.new_password

        logins_count = self.logins_count

        mfa_enabled = self.mfa_enabled

        mfa_reset = self.mfa_reset

        full_name = self.full_name

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        main_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_address, Unset):
            main_address = self.main_address.to_dict()

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "email": email,
            }
        )
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if logins_count is not UNSET:
            field_dict["loginsCount"] = logins_count
        if mfa_enabled is not UNSET:
            field_dict["mfaEnabled"] = mfa_enabled
        if mfa_reset is not UNSET:
            field_dict["mfaReset"] = mfa_reset
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if main_address is not UNSET:
            field_dict["mainAddress"] = main_address
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_user_response_200_address import PatchUserResponse200Address
        from ..models.patch_user_response_200_language import PatchUserResponse200Language
        from ..models.patch_user_response_200_policy_group import PatchUserResponse200PolicyGroup

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        email = d.pop("email")

        _account_id = d.pop("accountID", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        new_password = d.pop("newPassword", UNSET)

        logins_count = d.pop("loginsCount", UNSET)

        mfa_enabled = d.pop("mfaEnabled", UNSET)

        mfa_reset = d.pop("mfaReset", UNSET)

        full_name = d.pop("fullName", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[PatchUserResponse200PolicyGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = PatchUserResponse200PolicyGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        _main_address = d.pop("mainAddress", UNSET)
        main_address: PatchUserResponse200Address | Unset
        if isinstance(_main_address, Unset):
            main_address = UNSET
        else:
            main_address = PatchUserResponse200Address.from_dict(_main_address)

        _language = d.pop("language", UNSET)
        language: PatchUserResponse200Language | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = PatchUserResponse200Language.from_dict(_language)

        patch_user_response_200 = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            email=email,
            account_id=account_id,
            new_password=new_password,
            logins_count=logins_count,
            mfa_enabled=mfa_enabled,
            mfa_reset=mfa_reset,
            full_name=full_name,
            groups=groups,
            main_address=main_address,
            language=language,
        )

        patch_user_response_200.additional_properties = d
        return patch_user_response_200

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
