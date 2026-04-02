from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_systems_system_id_timeofuse_status_current_response_200_status import (
        GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status,
    )


T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseStatusCurrentResponse200")


@_attrs_define
class GetSystemsSystemIDTimeofuseStatusCurrentResponse200:
    """
    Attributes:
        status (GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status | Unset):
    """

    status: GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_timeofuse_status_current_response_200_status import (
            GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status,
        )

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetSystemsSystemIDTimeofuseStatusCurrentResponse200Status.from_dict(_status)

        get_systems_system_id_timeofuse_status_current_response_200 = cls(
            status=status,
        )

        get_systems_system_id_timeofuse_status_current_response_200.additional_properties = d
        return get_systems_system_id_timeofuse_status_current_response_200

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
