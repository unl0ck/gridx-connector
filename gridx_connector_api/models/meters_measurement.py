from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetersMeasurement")


@_attrs_define
class MetersMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        appliance_id (UUID | Unset): Unique identifier
        type_ (str | Unset): Describes the 'physical' type of the appliance.
        kind (str | Unset): Indicates the role of the meter.
        l_1_active_power (int | Unset): L1 Active Power in mW.
        l_1_current (int | Unset): L1 Current in mA.
        l_1_voltage (int | Unset): L1 Voltage in mV.
        l_1_import_power_limit (int | Unset): L1 maximum imported power in mW.
        l_2_import_power_limit (int | Unset): L2 maximum imported power in mW.
        l_3_import_power_limit (int | Unset): L3 maximum imported power in mW.
        sum_active_power (int | Unset): Sum Active Power in mW.
    """

    measured_at: datetime.datetime | Unset = UNSET
    appliance_id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    kind: str | Unset = UNSET
    l_1_active_power: int | Unset = UNSET
    l_1_current: int | Unset = UNSET
    l_1_voltage: int | Unset = UNSET
    l_1_import_power_limit: int | Unset = UNSET
    l_2_import_power_limit: int | Unset = UNSET
    l_3_import_power_limit: int | Unset = UNSET
    sum_active_power: int | Unset = UNSET
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

        l_1_active_power = self.l_1_active_power

        l_1_current = self.l_1_current

        l_1_voltage = self.l_1_voltage

        l_1_import_power_limit = self.l_1_import_power_limit

        l_2_import_power_limit = self.l_2_import_power_limit

        l_3_import_power_limit = self.l_3_import_power_limit

        sum_active_power = self.sum_active_power

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
        if l_1_active_power is not UNSET:
            field_dict["l1ActivePower"] = l_1_active_power
        if l_1_current is not UNSET:
            field_dict["l1Current"] = l_1_current
        if l_1_voltage is not UNSET:
            field_dict["l1Voltage"] = l_1_voltage
        if l_1_import_power_limit is not UNSET:
            field_dict["l1ImportPowerLimit"] = l_1_import_power_limit
        if l_2_import_power_limit is not UNSET:
            field_dict["l2ImportPowerLimit"] = l_2_import_power_limit
        if l_3_import_power_limit is not UNSET:
            field_dict["l3ImportPowerLimit"] = l_3_import_power_limit
        if sum_active_power is not UNSET:
            field_dict["sumActivePower"] = sum_active_power

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

        l_1_active_power = d.pop("l1ActivePower", UNSET)

        l_1_current = d.pop("l1Current", UNSET)

        l_1_voltage = d.pop("l1Voltage", UNSET)

        l_1_import_power_limit = d.pop("l1ImportPowerLimit", UNSET)

        l_2_import_power_limit = d.pop("l2ImportPowerLimit", UNSET)

        l_3_import_power_limit = d.pop("l3ImportPowerLimit", UNSET)

        sum_active_power = d.pop("sumActivePower", UNSET)

        meters_measurement = cls(
            measured_at=measured_at,
            appliance_id=appliance_id,
            type_=type_,
            kind=kind,
            l_1_active_power=l_1_active_power,
            l_1_current=l_1_current,
            l_1_voltage=l_1_voltage,
            l_1_import_power_limit=l_1_import_power_limit,
            l_2_import_power_limit=l_2_import_power_limit,
            l_3_import_power_limit=l_3_import_power_limit,
            sum_active_power=sum_active_power,
        )

        meters_measurement.additional_properties = d
        return meters_measurement

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
