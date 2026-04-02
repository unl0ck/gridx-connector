from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_gateways_gateway_id_response_200_additional_identifiers_of_the_grid_box_type import (
    PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBox")


@_attrs_define
class PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBox:
    """Additional identifiers used by the gridBox.

    Attributes:
        service (str | Unset): The service this identifier is referring to, e.g the protocol used for the appliance-
            gridBox handshake Example: EEBUS.
        type_ (PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType | Unset): The type of the
            identifier. Example: SKI.
        identifier (str | Unset): The actual identifier, e.g "SKI" used in the TLS certificate for the communication. If
            type is "SKI", it is hexadecimal-encoded.
    """

    service: str | Unset = UNSET
    type_: PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service = d.pop("service", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType(_type_)

        identifier = d.pop("identifier", UNSET)

        patch_gateways_gateway_id_response_200_additional_identifiers_of_the_grid_box = cls(
            service=service,
            type_=type_,
            identifier=identifier,
        )

        patch_gateways_gateway_id_response_200_additional_identifiers_of_the_grid_box.additional_properties = d
        return patch_gateways_gateway_id_response_200_additional_identifiers_of_the_grid_box

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
