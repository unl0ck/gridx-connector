from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurements_total_measurement_grid_measurement_grid_meter_reading import (
        MeasurementsTotalMeasurementGridMeasurementGridMeterReading,
    )


T = TypeVar("T", bound="MeasurementsTotalMeasurementGrid")


@_attrs_define
class MeasurementsTotalMeasurementGrid:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        feed_in (float | Unset):
        supply (float | Unset):
        supply_limit (float | Unset):
        meter_reading (MeasurementsTotalMeasurementGridMeasurementGridMeterReading | Unset):
    """

    measured_at: datetime.datetime | Unset = UNSET
    feed_in: float | Unset = UNSET
    supply: float | Unset = UNSET
    supply_limit: float | Unset = UNSET
    meter_reading: MeasurementsTotalMeasurementGridMeasurementGridMeterReading | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        feed_in = self.feed_in

        supply = self.supply

        supply_limit = self.supply_limit

        meter_reading: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter_reading, Unset):
            meter_reading = self.meter_reading.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if feed_in is not UNSET:
            field_dict["feedIn"] = feed_in
        if supply is not UNSET:
            field_dict["supply"] = supply
        if supply_limit is not UNSET:
            field_dict["supplyLimit"] = supply_limit
        if meter_reading is not UNSET:
            field_dict["meterReading"] = meter_reading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurements_total_measurement_grid_measurement_grid_meter_reading import (
            MeasurementsTotalMeasurementGridMeasurementGridMeterReading,
        )

        d = dict(src_dict)
        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        feed_in = d.pop("feedIn", UNSET)

        supply = d.pop("supply", UNSET)

        supply_limit = d.pop("supplyLimit", UNSET)

        _meter_reading = d.pop("meterReading", UNSET)
        meter_reading: MeasurementsTotalMeasurementGridMeasurementGridMeterReading | Unset
        if isinstance(_meter_reading, Unset):
            meter_reading = UNSET
        else:
            meter_reading = MeasurementsTotalMeasurementGridMeasurementGridMeterReading.from_dict(_meter_reading)

        measurements_total_measurement_grid = cls(
            measured_at=measured_at,
            feed_in=feed_in,
            supply=supply,
            supply_limit=supply_limit,
            meter_reading=meter_reading,
        )

        measurements_total_measurement_grid.additional_properties = d
        return measurements_total_measurement_grid

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
