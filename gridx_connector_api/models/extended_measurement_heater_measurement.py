from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedMeasurementHeaterMeasurement")


@_attrs_define
class ExtendedMeasurementHeaterMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Represents the time when the data was measured.
        appliance_id (str | Unset): Unique identifier for referencing a heater.
        power (float | Unset): Power consumed by the heater in W.
        power_l1 (float | Unset): Power consumed by the heater on the first phase in W.
        power_l2 (float | Unset): Power consumed by the heater on the second phase in W.
        power_l3 (float | Unset): Power consumed by the heater on the third phase in W.
        temperature (float | Unset): Temperature measured by this heater in Â°C.
        min_temperature (float | Unset): Minimum temperature measured by this heater in Â°C.
        max_temperature (float | Unset): Maximum temperature measured by this heater in Â°C.
    """

    measured_at: datetime.datetime | Unset = UNSET
    appliance_id: str | Unset = UNSET
    power: float | Unset = UNSET
    power_l1: float | Unset = UNSET
    power_l2: float | Unset = UNSET
    power_l3: float | Unset = UNSET
    temperature: float | Unset = UNSET
    min_temperature: float | Unset = UNSET
    max_temperature: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        appliance_id = self.appliance_id

        power = self.power

        power_l1 = self.power_l1

        power_l2 = self.power_l2

        power_l3 = self.power_l3

        temperature = self.temperature

        min_temperature = self.min_temperature

        max_temperature = self.max_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if power is not UNSET:
            field_dict["power"] = power
        if power_l1 is not UNSET:
            field_dict["powerL1"] = power_l1
        if power_l2 is not UNSET:
            field_dict["powerL2"] = power_l2
        if power_l3 is not UNSET:
            field_dict["powerL3"] = power_l3
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if min_temperature is not UNSET:
            field_dict["minTemperature"] = min_temperature
        if max_temperature is not UNSET:
            field_dict["maxTemperature"] = max_temperature

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

        appliance_id = d.pop("applianceID", UNSET)

        power = d.pop("power", UNSET)

        power_l1 = d.pop("powerL1", UNSET)

        power_l2 = d.pop("powerL2", UNSET)

        power_l3 = d.pop("powerL3", UNSET)

        temperature = d.pop("temperature", UNSET)

        min_temperature = d.pop("minTemperature", UNSET)

        max_temperature = d.pop("maxTemperature", UNSET)

        extended_measurement_heater_measurement = cls(
            measured_at=measured_at,
            appliance_id=appliance_id,
            power=power,
            power_l1=power_l1,
            power_l2=power_l2,
            power_l3=power_l3,
            temperature=temperature,
            min_temperature=min_temperature,
            max_temperature=max_temperature,
        )

        extended_measurement_heater_measurement.additional_properties = d
        return extended_measurement_heater_measurement

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
