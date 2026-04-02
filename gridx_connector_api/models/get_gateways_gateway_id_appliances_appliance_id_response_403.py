from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGatewaysGatewayIDAppliancesApplianceIDResponse403")


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDResponse403:
    """
    Attributes:
        message (str): Message represents the message reported to the user.
        details (list[str] | Unset): Details represents detail information for the user to fix this
            problem
    """

    message: str
    details: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        details: list[str] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        details = cast(list[str], d.pop("details", UNSET))

        get_gateways_gateway_id_appliances_appliance_id_response_403 = cls(
            message=message,
            details=details,
        )

        get_gateways_gateway_id_appliances_appliance_id_response_403.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_response_403

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
