from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedEVStationMeasurement")


@_attrs_define
class ExtendedEVStationMeasurement:
    """
    Attributes:
        charge (float | Unset): The measured charging power of the EV.
        discharge (float | Unset): Power/energy discharged from the EV.
        state_of_charge (float | Unset): Percentage of EV battery charged (0.0-1.0).
        current_l1 (float | Unset): Current on the first phase of the EV station in A (ampere).
        current_l2 (float | Unset): Current on the second phase of the EV station in A.
        current_l3 (float | Unset): Current on the third phase of the EV station in A.
    """

    charge: float | Unset = UNSET
    discharge: float | Unset = UNSET
    state_of_charge: float | Unset = UNSET
    current_l1: float | Unset = UNSET
    current_l2: float | Unset = UNSET
    current_l3: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge = self.charge

        discharge = self.discharge

        state_of_charge = self.state_of_charge

        current_l1 = self.current_l1

        current_l2 = self.current_l2

        current_l3 = self.current_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge is not UNSET:
            field_dict["charge"] = charge
        if discharge is not UNSET:
            field_dict["discharge"] = discharge
        if state_of_charge is not UNSET:
            field_dict["stateOfCharge"] = state_of_charge
        if current_l1 is not UNSET:
            field_dict["currentL1"] = current_l1
        if current_l2 is not UNSET:
            field_dict["currentL2"] = current_l2
        if current_l3 is not UNSET:
            field_dict["currentL3"] = current_l3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge = d.pop("charge", UNSET)

        discharge = d.pop("discharge", UNSET)

        state_of_charge = d.pop("stateOfCharge", UNSET)

        current_l1 = d.pop("currentL1", UNSET)

        current_l2 = d.pop("currentL2", UNSET)

        current_l3 = d.pop("currentL3", UNSET)

        extended_ev_station_measurement = cls(
            charge=charge,
            discharge=discharge,
            state_of_charge=state_of_charge,
            current_l1=current_l1,
            current_l2=current_l2,
            current_l3=current_l3,
        )

        extended_ev_station_measurement.additional_properties = d
        return extended_ev_station_measurement

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
