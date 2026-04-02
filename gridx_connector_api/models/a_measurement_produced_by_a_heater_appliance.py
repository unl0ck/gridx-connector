from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AMeasurementProducedByAHeaterAppliance")


@_attrs_define
class AMeasurementProducedByAHeaterAppliance:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured in UTC using RFC3339 format.
        flow_rate (float | Unset): Volumetric flow rate given in mÂ³/s.
        reading_positive (float | Unset): Energy meter reading that was gained during circulation from inflow to outflow
            in Wh.
        reading_negative (float | Unset): Energy meter reading that was consumed during circulation from inflow to
            outflow in Wh.
        power (float | Unset): Power in mW.
        inflow_temperature (float | Unset): Inflow temperature given in Â°C
        outflow_temperature (float | Unset): Outflow temperature given in Â°C
    """

    measured_at: datetime.datetime | Unset = UNSET
    flow_rate: float | Unset = UNSET
    reading_positive: float | Unset = UNSET
    reading_negative: float | Unset = UNSET
    power: float | Unset = UNSET
    inflow_temperature: float | Unset = UNSET
    outflow_temperature: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        flow_rate = self.flow_rate

        reading_positive = self.reading_positive

        reading_negative = self.reading_negative

        power = self.power

        inflow_temperature = self.inflow_temperature

        outflow_temperature = self.outflow_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if flow_rate is not UNSET:
            field_dict["flowRate"] = flow_rate
        if reading_positive is not UNSET:
            field_dict["readingPositive"] = reading_positive
        if reading_negative is not UNSET:
            field_dict["readingNegative"] = reading_negative
        if power is not UNSET:
            field_dict["power"] = power
        if inflow_temperature is not UNSET:
            field_dict["inflowTemperature"] = inflow_temperature
        if outflow_temperature is not UNSET:
            field_dict["outflowTemperature"] = outflow_temperature

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

        flow_rate = d.pop("flowRate", UNSET)

        reading_positive = d.pop("readingPositive", UNSET)

        reading_negative = d.pop("readingNegative", UNSET)

        power = d.pop("power", UNSET)

        inflow_temperature = d.pop("inflowTemperature", UNSET)

        outflow_temperature = d.pop("outflowTemperature", UNSET)

        a_measurement_produced_by_a_heater_appliance = cls(
            measured_at=measured_at,
            flow_rate=flow_rate,
            reading_positive=reading_positive,
            reading_negative=reading_negative,
            power=power,
            inflow_temperature=inflow_temperature,
            outflow_temperature=outflow_temperature,
        )

        a_measurement_produced_by_a_heater_appliance.additional_properties = d
        return a_measurement_produced_by_a_heater_appliance

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
