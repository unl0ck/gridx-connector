from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.gateway_create_type import GatewayCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayCreate")


@_attrs_define
class GatewayCreate:
    """
    Attributes:
        startcode (str): Code used to register a new gateway. Example: 39FDDF7D85BAAD2D.
        name (str | Unset): Name of the gateway.
        debug_mode_until (datetime.datetime | Unset): Date until which debug messages are logged in RFC3339 format.
        vendor_id (UUID | Unset): ID of the vendor account to which the corresponding system is assigned. Example:
            6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        type_ (GatewayCreateType | Unset): Type of the gateway.

            **Deprecated** - Non-physical gateways will no longer be supported from 01.03.2024. This field will consequently
            be removed.
    """

    startcode: str
    name: str | Unset = UNSET
    debug_mode_until: datetime.datetime | Unset = UNSET
    vendor_id: UUID | Unset = UNSET
    type_: GatewayCreateType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        startcode = self.startcode

        name = self.name

        debug_mode_until: str | Unset = UNSET
        if not isinstance(self.debug_mode_until, Unset):
            debug_mode_until = self.debug_mode_until.isoformat()

        vendor_id: str | Unset = UNSET
        if not isinstance(self.vendor_id, Unset):
            vendor_id = str(self.vendor_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startcode": startcode,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if debug_mode_until is not UNSET:
            field_dict["debugModeUntil"] = debug_mode_until
        if vendor_id is not UNSET:
            field_dict["vendorID"] = vendor_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        startcode = d.pop("startcode")

        name = d.pop("name", UNSET)

        _debug_mode_until = d.pop("debugModeUntil", UNSET)
        debug_mode_until: datetime.datetime | Unset
        if isinstance(_debug_mode_until, Unset):
            debug_mode_until = UNSET
        else:
            debug_mode_until = isoparse(_debug_mode_until)

        _vendor_id = d.pop("vendorID", UNSET)
        vendor_id: UUID | Unset
        if isinstance(_vendor_id, Unset):
            vendor_id = UNSET
        else:
            vendor_id = UUID(_vendor_id)

        _type_ = d.pop("type", UNSET)
        type_: GatewayCreateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GatewayCreateType(_type_)

        gateway_create = cls(
            startcode=startcode,
            name=name,
            debug_mode_until=debug_mode_until,
            vendor_id=vendor_id,
            type_=type_,
        )

        gateway_create.additional_properties = d
        return gateway_create

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
