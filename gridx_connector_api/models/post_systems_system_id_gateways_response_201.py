from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_systems_system_id_gateways_response_201_scanners_item import (
    PostSystemsSystemIDGatewaysResponse201ScannersItem,
)
from ..models.post_systems_system_id_gateways_response_201_type import PostSystemsSystemIDGatewaysResponse201Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_systems_system_id_gateways_response_201_additional_identifiers_of_the_grid_box import (
        PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox,
    )
    from ..models.post_systems_system_id_gateways_response_201_connection_status import (
        PostSystemsSystemIDGatewaysResponse201ConnectionStatus,
    )


T = TypeVar("T", bound="PostSystemsSystemIDGatewaysResponse201")


@_attrs_define
class PostSystemsSystemIDGatewaysResponse201:
    """
    Attributes:
        id (UUID): Unique identifier of a gateway. Example: 6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        type_ (PostSystemsSystemIDGatewaysResponse201Type): Type of the gateway.

            **Deprecated** - Non-physical gateways will no longer be supported from 01.03.2024. This field will consequently
            be removed.
        created_at (datetime.datetime): Date when the Gateway was created in RFC3339 format.
        updated_at (datetime.datetime): Date when the Gateway was last updated in RFC3339 format.
        connection_status (PostSystemsSystemIDGatewaysResponse201ConnectionStatus):
        name (str | Unset): Name of the gateway.
        debug_mode_until (datetime.datetime | Unset): Date until which debug messages are logged in RFC3339 format.
        registered_at (datetime.datetime | Unset): Date when the Gateway was first registered in RFC3339 format.
        vendor_id (UUID | Unset): ID of the vendor account to which the corresponding system is assigned. Example:
            6dd0a658-5828-4d30-bc65-a03c6d6e425f.
        startcode (str | Unset): Code used to register a new gateway. Example: 39FDDF7D85BAAD2D.
        manufacturer (str | Unset): Manufacturer of the gateway. Example: gridX.
        model (str | Unset): Model of the gateway. Example: 2.00P-X.
        serialnumber (str | Unset): Serial number of the gateway. Example: C083-200-000-000-199-P-X.
        additional_identifiers (list[PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox] | Unset):
            Additional identifiers used by the gateway.
        scanners (list[PostSystemsSystemIDGatewaysResponse201ScannersItem] | Unset): List of scanner names that are
            enabled for this gateway.
        appliance_composition (list[str] | Unset): Appliance types that are connected to the gateway for overview
            purposes. Example: ['HEAT_PUMP'].
    """

    id: UUID
    type_: PostSystemsSystemIDGatewaysResponse201Type
    created_at: datetime.datetime
    updated_at: datetime.datetime
    connection_status: PostSystemsSystemIDGatewaysResponse201ConnectionStatus
    name: str | Unset = UNSET
    debug_mode_until: datetime.datetime | Unset = UNSET
    registered_at: datetime.datetime | Unset = UNSET
    vendor_id: UUID | Unset = UNSET
    startcode: str | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    serialnumber: str | Unset = UNSET
    additional_identifiers: list[PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox] | Unset = (
        UNSET
    )
    scanners: list[PostSystemsSystemIDGatewaysResponse201ScannersItem] | Unset = UNSET
    appliance_composition: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        connection_status = self.connection_status.to_dict()

        name = self.name

        debug_mode_until: str | Unset = UNSET
        if not isinstance(self.debug_mode_until, Unset):
            debug_mode_until = self.debug_mode_until.isoformat()

        registered_at: str | Unset = UNSET
        if not isinstance(self.registered_at, Unset):
            registered_at = self.registered_at.isoformat()

        vendor_id: str | Unset = UNSET
        if not isinstance(self.vendor_id, Unset):
            vendor_id = str(self.vendor_id)

        startcode = self.startcode

        manufacturer = self.manufacturer

        model = self.model

        serialnumber = self.serialnumber

        additional_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_identifiers, Unset):
            additional_identifiers = []
            for additional_identifiers_item_data in self.additional_identifiers:
                additional_identifiers_item = additional_identifiers_item_data.to_dict()
                additional_identifiers.append(additional_identifiers_item)

        scanners: list[str] | Unset = UNSET
        if not isinstance(self.scanners, Unset):
            scanners = []
            for scanners_item_data in self.scanners:
                scanners_item = scanners_item_data.value
                scanners.append(scanners_item)

        appliance_composition: list[str] | Unset = UNSET
        if not isinstance(self.appliance_composition, Unset):
            appliance_composition = self.appliance_composition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "connectionStatus": connection_status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if debug_mode_until is not UNSET:
            field_dict["debugModeUntil"] = debug_mode_until
        if registered_at is not UNSET:
            field_dict["registeredAt"] = registered_at
        if vendor_id is not UNSET:
            field_dict["vendorID"] = vendor_id
        if startcode is not UNSET:
            field_dict["startcode"] = startcode
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if serialnumber is not UNSET:
            field_dict["serialnumber"] = serialnumber
        if additional_identifiers is not UNSET:
            field_dict["additionalIdentifiers"] = additional_identifiers
        if scanners is not UNSET:
            field_dict["scanners"] = scanners
        if appliance_composition is not UNSET:
            field_dict["applianceComposition"] = appliance_composition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_systems_system_id_gateways_response_201_additional_identifiers_of_the_grid_box import (
            PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox,
        )
        from ..models.post_systems_system_id_gateways_response_201_connection_status import (
            PostSystemsSystemIDGatewaysResponse201ConnectionStatus,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = PostSystemsSystemIDGatewaysResponse201Type(d.pop("type"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        connection_status = PostSystemsSystemIDGatewaysResponse201ConnectionStatus.from_dict(d.pop("connectionStatus"))

        name = d.pop("name", UNSET)

        _debug_mode_until = d.pop("debugModeUntil", UNSET)
        debug_mode_until: datetime.datetime | Unset
        if isinstance(_debug_mode_until, Unset):
            debug_mode_until = UNSET
        else:
            debug_mode_until = isoparse(_debug_mode_until)

        _registered_at = d.pop("registeredAt", UNSET)
        registered_at: datetime.datetime | Unset
        if isinstance(_registered_at, Unset):
            registered_at = UNSET
        else:
            registered_at = isoparse(_registered_at)

        _vendor_id = d.pop("vendorID", UNSET)
        vendor_id: UUID | Unset
        if isinstance(_vendor_id, Unset):
            vendor_id = UNSET
        else:
            vendor_id = UUID(_vendor_id)

        startcode = d.pop("startcode", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        serialnumber = d.pop("serialnumber", UNSET)

        _additional_identifiers = d.pop("additionalIdentifiers", UNSET)
        additional_identifiers: (
            list[PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox] | Unset
        ) = UNSET
        if _additional_identifiers is not UNSET:
            additional_identifiers = []
            for additional_identifiers_item_data in _additional_identifiers:
                additional_identifiers_item = (
                    PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBox.from_dict(
                        additional_identifiers_item_data
                    )
                )

                additional_identifiers.append(additional_identifiers_item)

        _scanners = d.pop("scanners", UNSET)
        scanners: list[PostSystemsSystemIDGatewaysResponse201ScannersItem] | Unset = UNSET
        if _scanners is not UNSET:
            scanners = []
            for scanners_item_data in _scanners:
                scanners_item = PostSystemsSystemIDGatewaysResponse201ScannersItem(scanners_item_data)

                scanners.append(scanners_item)

        appliance_composition = cast(list[str], d.pop("applianceComposition", UNSET))

        post_systems_system_id_gateways_response_201 = cls(
            id=id,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            connection_status=connection_status,
            name=name,
            debug_mode_until=debug_mode_until,
            registered_at=registered_at,
            vendor_id=vendor_id,
            startcode=startcode,
            manufacturer=manufacturer,
            model=model,
            serialnumber=serialnumber,
            additional_identifiers=additional_identifiers,
            scanners=scanners,
            appliance_composition=appliance_composition,
        )

        post_systems_system_id_gateways_response_201.additional_properties = d
        return post_systems_system_id_gateways_response_201

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
