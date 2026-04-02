from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_systems_system_id_timeofuse_forecasts_meter_response_200_periods_item import (
        GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem,
    )


T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseForecastsMeterResponse200")


@_attrs_define
class GetSystemsSystemIDTimeofuseForecastsMeterResponse200:
    """
    Attributes:
        from_ (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the beginning of the validity period
            for the forecast.
             Example: 2020-09-21T00:00:00Z.
        to (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the end of the validity period for the
            forecast.
             Example: 2020-09-21T22:10:00Z.
        periods (list[GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem] | Unset):
        last_updated (datetime.datetime | Unset): Last time when the forecast was updated.
             Example: 2020-09-21T00:00:00Z.
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    periods: list[GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem] | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if periods is not UNSET:
            field_dict["periods"] = periods
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_timeofuse_forecasts_meter_response_200_periods_item import (
            GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem,
        )

        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        _periods = d.pop("periods", UNSET)
        periods: list[GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = GetSystemsSystemIDTimeofuseForecastsMeterResponse200PeriodsItem.from_dict(
                    periods_item_data
                )

                periods.append(periods_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        get_systems_system_id_timeofuse_forecasts_meter_response_200 = cls(
            from_=from_,
            to=to,
            periods=periods,
            last_updated=last_updated,
        )

        get_systems_system_id_timeofuse_forecasts_meter_response_200.additional_properties = d
        return get_systems_system_id_timeofuse_forecasts_meter_response_200

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
