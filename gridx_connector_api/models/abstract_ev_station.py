from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_ev_station_type import AbstractEVStationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_ev_station_ev_load_management_parameters import AbstractEVStationEvLoadManagementParameters


T = TypeVar("T", bound="AbstractEVStation")


@_attrs_define
class AbstractEVStation:
    """
    Attributes:
        type_ (AbstractEVStationType | Unset):
        manufacturer (str | Unset): Manufacturer of the ev charging station. Example: Echarge Hardy Barth.
        model (str | Unset): Model of the ev charging station. Example: eCHARGE/PV.
        firmware (str | Unset): Firmware version of the ev charging station. Example: 0.38-78000001.
        evse_id (str | Unset): The EVSE-ID related to the charge point.
        ev_load_management_parameters (AbstractEVStationEvLoadManagementParameters | Unset): Load management
            configuration for EV charging stations.

            **Deprecated** - Use the system's EV charging station configuration instead.
    """

    type_: AbstractEVStationType | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    evse_id: str | Unset = UNSET
    ev_load_management_parameters: AbstractEVStationEvLoadManagementParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        manufacturer = self.manufacturer

        model = self.model

        firmware = self.firmware

        evse_id = self.evse_id

        ev_load_management_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ev_load_management_parameters, Unset):
            ev_load_management_parameters = self.ev_load_management_parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if evse_id is not UNSET:
            field_dict["evseID"] = evse_id
        if ev_load_management_parameters is not UNSET:
            field_dict["evLoadManagementParameters"] = ev_load_management_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_ev_station_ev_load_management_parameters import (
            AbstractEVStationEvLoadManagementParameters,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractEVStationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractEVStationType(_type_)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        evse_id = d.pop("evseID", UNSET)

        _ev_load_management_parameters = d.pop("evLoadManagementParameters", UNSET)
        ev_load_management_parameters: AbstractEVStationEvLoadManagementParameters | Unset
        if isinstance(_ev_load_management_parameters, Unset):
            ev_load_management_parameters = UNSET
        else:
            ev_load_management_parameters = AbstractEVStationEvLoadManagementParameters.from_dict(
                _ev_load_management_parameters
            )

        abstract_ev_station = cls(
            type_=type_,
            manufacturer=manufacturer,
            model=model,
            firmware=firmware,
            evse_id=evse_id,
            ev_load_management_parameters=ev_load_management_parameters,
        )

        abstract_ev_station.additional_properties = d
        return abstract_ev_station

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
