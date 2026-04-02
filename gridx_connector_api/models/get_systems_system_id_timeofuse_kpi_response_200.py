from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_systems_system_id_timeofuse_kpi_response_200_periods_item import (
        GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem,
    )


T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseKpiResponse200")


@_attrs_define
class GetSystemsSystemIDTimeofuseKpiResponse200:
    """Time-of-Use KPI history for the system for which the request is made.

    Attributes:
        periods (list[GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem] | Unset): Time-of-Use KPI collection.
    """

    periods: list[GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_timeofuse_kpi_response_200_periods_item import (
            GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem,
        )

        d = dict(src_dict)
        _periods = d.pop("periods", UNSET)
        periods: list[GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = GetSystemsSystemIDTimeofuseKpiResponse200PeriodsItem.from_dict(periods_item_data)

                periods.append(periods_item)

        get_systems_system_id_timeofuse_kpi_response_200 = cls(
            periods=periods,
        )

        get_systems_system_id_timeofuse_kpi_response_200.additional_properties = d
        return get_systems_system_id_timeofuse_kpi_response_200

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
