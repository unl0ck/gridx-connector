from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meter_aux_meter_location import MeterAuxMeterLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeterAuxMeter")


@_attrs_define
class MeterAuxMeter:
    """The meter specific information.

    Attributes:
        location (MeterAuxMeterLocation | Unset): Indicates that the meter is in front of given location for measuring
            the consumption and production.
        type_ (str | Unset): Describes the specific type of the meter. Example: SE_SINGLE_PHASE.
        modbus_address (int | Unset):
    """

    location: MeterAuxMeterLocation | Unset = UNSET
    type_: str | Unset = UNSET
    modbus_address: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location: str | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.value

        type_ = self.type_

        modbus_address = self.modbus_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if type_ is not UNSET:
            field_dict["type"] = type_
        if modbus_address is not UNSET:
            field_dict["modbusAddress"] = modbus_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _location = d.pop("location", UNSET)
        location: MeterAuxMeterLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = MeterAuxMeterLocation(_location)

        type_ = d.pop("type", UNSET)

        modbus_address = d.pop("modbusAddress", UNSET)

        meter_aux_meter = cls(
            location=location,
            type_=type_,
            modbus_address=modbus_address,
        )

        meter_aux_meter.additional_properties = d
        return meter_aux_meter

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
