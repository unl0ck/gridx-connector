from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.a_measurement_produced_by_a_heatpump_appliance_ready_state import (
    AMeasurementProducedByAHeatpumpApplianceReadyState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AMeasurementProducedByAHeatpumpAppliance")


@_attrs_define
class AMeasurementProducedByAHeatpumpAppliance:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        appliance_id (UUID | Unset): Unique identifier
        type_ (str | Unset): Describes the 'physical' type of the appliance.
        kind (str | Unset): Indicates the role of the heatpump.
        power (int | Unset): Power of the heatpump in mW.
        power_l1 (int | Unset): Power for the first phase in mW .
        power_l2 (int | Unset):
        power_l3 (int | Unset):
        min_power (int | Unset):
        max_power (int | Unset):
        ready_state (AMeasurementProducedByAHeatpumpApplianceReadyState | Unset):  Default:
            AMeasurementProducedByAHeatpumpApplianceReadyState.UNKNOWN.
    """

    measured_at: datetime.datetime | Unset = UNSET
    appliance_id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    kind: str | Unset = UNSET
    power: int | Unset = UNSET
    power_l1: int | Unset = UNSET
    power_l2: int | Unset = UNSET
    power_l3: int | Unset = UNSET
    min_power: int | Unset = UNSET
    max_power: int | Unset = UNSET
    ready_state: AMeasurementProducedByAHeatpumpApplianceReadyState | Unset = (
        AMeasurementProducedByAHeatpumpApplianceReadyState.UNKNOWN
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        appliance_id: str | Unset = UNSET
        if not isinstance(self.appliance_id, Unset):
            appliance_id = str(self.appliance_id)

        type_ = self.type_

        kind = self.kind

        power = self.power

        power_l1 = self.power_l1

        power_l2 = self.power_l2

        power_l3 = self.power_l3

        min_power = self.min_power

        max_power = self.max_power

        ready_state: str | Unset = UNSET
        if not isinstance(self.ready_state, Unset):
            ready_state = self.ready_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if kind is not UNSET:
            field_dict["kind"] = kind
        if power is not UNSET:
            field_dict["power"] = power
        if power_l1 is not UNSET:
            field_dict["powerL1"] = power_l1
        if power_l2 is not UNSET:
            field_dict["powerL2"] = power_l2
        if power_l3 is not UNSET:
            field_dict["powerL3"] = power_l3
        if min_power is not UNSET:
            field_dict["minPower"] = min_power
        if max_power is not UNSET:
            field_dict["maxPower"] = max_power
        if ready_state is not UNSET:
            field_dict["readyState"] = ready_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        _appliance_id = d.pop("applianceID", UNSET)
        appliance_id: UUID | Unset
        if isinstance(_appliance_id, Unset):
            appliance_id = UNSET
        else:
            appliance_id = UUID(_appliance_id)

        type_ = d.pop("type", UNSET)

        kind = d.pop("kind", UNSET)

        power = d.pop("power", UNSET)

        power_l1 = d.pop("powerL1", UNSET)

        power_l2 = d.pop("powerL2", UNSET)

        power_l3 = d.pop("powerL3", UNSET)

        min_power = d.pop("minPower", UNSET)

        max_power = d.pop("maxPower", UNSET)

        _ready_state = d.pop("readyState", UNSET)
        ready_state: AMeasurementProducedByAHeatpumpApplianceReadyState | Unset
        if isinstance(_ready_state, Unset):
            ready_state = UNSET
        else:
            ready_state = AMeasurementProducedByAHeatpumpApplianceReadyState(_ready_state)

        a_measurement_produced_by_a_heatpump_appliance = cls(
            measured_at=measured_at,
            appliance_id=appliance_id,
            type_=type_,
            kind=kind,
            power=power,
            power_l1=power_l1,
            power_l2=power_l2,
            power_l3=power_l3,
            min_power=min_power,
            max_power=max_power,
            ready_state=ready_state,
        )

        a_measurement_produced_by_a_heatpump_appliance.additional_properties = d
        return a_measurement_produced_by_a_heatpump_appliance

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
