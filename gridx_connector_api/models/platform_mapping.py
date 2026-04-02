from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlatformMapping")


@_attrs_define
class PlatformMapping:
    """Represents a 1:1 mapping from a XENON account to a Platform workspace and application.

    Attributes:
        account_id (UUID): Unique identifier of a XENON account. Example: 6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        application_id (UUID): Unique identifier of the corresponding platform application. Example:
            7af138d7-717d-486e-8ad1-1d4ed4b1669e.
        workspace_id (UUID): Unique identifier of the corresponding platform workspace. Example: 2549665c-5067-49ad-
            af6a-9c74e74095e8.
    """

    account_id: UUID
    application_id: UUID
    workspace_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        application_id = str(self.application_id)

        workspace_id = str(self.workspace_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountID": account_id,
                "applicationID": application_id,
                "workspaceID": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("accountID"))

        application_id = UUID(d.pop("applicationID"))

        workspace_id = UUID(d.pop("workspaceID"))

        platform_mapping = cls(
            account_id=account_id,
            application_id=application_id,
            workspace_id=workspace_id,
        )

        platform_mapping.additional_properties = d
        return platform_mapping

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
