from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_systems_system_id_timeofuse_readiness_response_200_reasons_item import (
    GetSystemsSystemIDTimeofuseReadinessResponse200ReasonsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseReadinessResponse200")


@_attrs_define
class GetSystemsSystemIDTimeofuseReadinessResponse200:
    """
    Attributes:
        is_tou_ready (bool): Truth value whether system is ready for ToU.
        reasons (list[GetSystemsSystemIDTimeofuseReadinessResponse200ReasonsItem] | Unset): List of reasons detailing
            the cause(s) of the truth value of ToU Readiness
    """

    is_tou_ready: bool
    reasons: list[GetSystemsSystemIDTimeofuseReadinessResponse200ReasonsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_tou_ready = self.is_tou_ready

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.value
                reasons.append(reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isTouReady": is_tou_ready,
            }
        )
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_tou_ready = d.pop("isTouReady")

        _reasons = d.pop("reasons", UNSET)
        reasons: list[GetSystemsSystemIDTimeofuseReadinessResponse200ReasonsItem] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = GetSystemsSystemIDTimeofuseReadinessResponse200ReasonsItem(reasons_item_data)

                reasons.append(reasons_item)

        get_systems_system_id_timeofuse_readiness_response_200 = cls(
            is_tou_ready=is_tou_ready,
            reasons=reasons,
        )

        get_systems_system_id_timeofuse_readiness_response_200.additional_properties = d
        return get_systems_system_id_timeofuse_readiness_response_200

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
