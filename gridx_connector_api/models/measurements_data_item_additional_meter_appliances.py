from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeasurementsDataItemAdditionalMeterAppliances")


@_attrs_define
class MeasurementsDataItemAdditionalMeterAppliances:
    """Used in installations that have multiple grid meters, e.g. for
    multi family homes which a central PV but multiple meters.

        Attributes:
            appliance_id (str): gridX API internal identifier of the meter. Example: a7d56cb5-2dac-48d4-952a-6eb75ee0ce18.
            power (float | Unset): Power/energy measured for this meter in W.
            kind (str | Unset): Kind of the appliance measurement.
    """

    appliance_id: str
    power: float | Unset = UNSET
    kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_id = self.appliance_id

        power = self.power

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applianceID": appliance_id,
            }
        )
        if power is not UNSET:
            field_dict["power"] = power
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_id = d.pop("applianceID")

        power = d.pop("power", UNSET)

        kind = d.pop("kind", UNSET)

        measurements_data_item_additional_meter_appliances = cls(
            appliance_id=appliance_id,
            power=power,
            kind=kind,
        )

        measurements_data_item_additional_meter_appliances.additional_properties = d
        return measurements_data_item_additional_meter_appliances

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
