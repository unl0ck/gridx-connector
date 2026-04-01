from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI")


@_attrs_define
class HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI:
    """
    Attributes:
        max_import_measured_timestamp (datetime.datetime): Time at which the import power limit was created in UTC using
            the RFC3339 format. Example: 2021-10-10T23:20:50Z.
        max_import_total (int): Maximum total import power in mW.
        max_import_l1 (int): Maximum total import power in the first phase in mW.
        max_import_l2 (int): Maximum total import power in the second phase in mW.
        max_import_l3 (int): Maximum total import power in the third phase in mW.
        max_import_ev_margin_total (int): maxImportTotal - importEVMarginTotal is the maximum import power considered in
            total in mW.
        max_import_ev_margin_l1 (int): Maximum import power margin in the first phase in mW.
        max_import_ev_margin_l2 (int): Maximum import power margin in the second phase in mW.
        max_import_ev_margin_l3 (int): Maximum import power margin in the third phase in mW.
        max_import_ev_margin_worst_case_total (int): The assumed maximum charging power in mW for all EVs in case the
            connection to the grid connection point is lost.
        max_import_ev_margin_worst_case_l1 (int): The assumed maximum charging power in mW for all EVs in case the
            connection to the grid connection point is lost for the first phase.
        max_import_ev_margin_worst_case_l2 (int): The assumed maximum charging power in mW for all EVs in case the
            connection to the grid connection point is lost for the second phase.
        max_import_ev_margin_worst_case_l3 (int): The assumed maximum charging power in mW for all EVs in case the
            connection to the grid connection point is lost for the third phase.
    """

    max_import_measured_timestamp: datetime.datetime
    max_import_total: int
    max_import_l1: int
    max_import_l2: int
    max_import_l3: int
    max_import_ev_margin_total: int
    max_import_ev_margin_l1: int
    max_import_ev_margin_l2: int
    max_import_ev_margin_l3: int
    max_import_ev_margin_worst_case_total: int
    max_import_ev_margin_worst_case_l1: int
    max_import_ev_margin_worst_case_l2: int
    max_import_ev_margin_worst_case_l3: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_import_measured_timestamp = self.max_import_measured_timestamp.isoformat()

        max_import_total = self.max_import_total

        max_import_l1 = self.max_import_l1

        max_import_l2 = self.max_import_l2

        max_import_l3 = self.max_import_l3

        max_import_ev_margin_total = self.max_import_ev_margin_total

        max_import_ev_margin_l1 = self.max_import_ev_margin_l1

        max_import_ev_margin_l2 = self.max_import_ev_margin_l2

        max_import_ev_margin_l3 = self.max_import_ev_margin_l3

        max_import_ev_margin_worst_case_total = self.max_import_ev_margin_worst_case_total

        max_import_ev_margin_worst_case_l1 = self.max_import_ev_margin_worst_case_l1

        max_import_ev_margin_worst_case_l2 = self.max_import_ev_margin_worst_case_l2

        max_import_ev_margin_worst_case_l3 = self.max_import_ev_margin_worst_case_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxImportMeasuredTimestamp": max_import_measured_timestamp,
                "maxImportTotal": max_import_total,
                "maxImportL1": max_import_l1,
                "maxImportL2": max_import_l2,
                "maxImportL3": max_import_l3,
                "maxImportEvMarginTotal": max_import_ev_margin_total,
                "maxImportEvMarginL1": max_import_ev_margin_l1,
                "maxImportEvMarginL2": max_import_ev_margin_l2,
                "maxImportEvMarginL3": max_import_ev_margin_l3,
                "maxImportEvMarginWorstCaseTotal": max_import_ev_margin_worst_case_total,
                "maxImportEvMarginWorstCaseL1": max_import_ev_margin_worst_case_l1,
                "maxImportEvMarginWorstCaseL2": max_import_ev_margin_worst_case_l2,
                "maxImportEvMarginWorstCaseL3": max_import_ev_margin_worst_case_l3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_import_measured_timestamp = isoparse(d.pop("maxImportMeasuredTimestamp"))

        max_import_total = d.pop("maxImportTotal")

        max_import_l1 = d.pop("maxImportL1")

        max_import_l2 = d.pop("maxImportL2")

        max_import_l3 = d.pop("maxImportL3")

        max_import_ev_margin_total = d.pop("maxImportEvMarginTotal")

        max_import_ev_margin_l1 = d.pop("maxImportEvMarginL1")

        max_import_ev_margin_l2 = d.pop("maxImportEvMarginL2")

        max_import_ev_margin_l3 = d.pop("maxImportEvMarginL3")

        max_import_ev_margin_worst_case_total = d.pop("maxImportEvMarginWorstCaseTotal")

        max_import_ev_margin_worst_case_l1 = d.pop("maxImportEvMarginWorstCaseL1")

        max_import_ev_margin_worst_case_l2 = d.pop("maxImportEvMarginWorstCaseL2")

        max_import_ev_margin_worst_case_l3 = d.pop("maxImportEvMarginWorstCaseL3")

        historical_import_power_limit_import_power_limits_stored_with_the_dynamic_api = cls(
            max_import_measured_timestamp=max_import_measured_timestamp,
            max_import_total=max_import_total,
            max_import_l1=max_import_l1,
            max_import_l2=max_import_l2,
            max_import_l3=max_import_l3,
            max_import_ev_margin_total=max_import_ev_margin_total,
            max_import_ev_margin_l1=max_import_ev_margin_l1,
            max_import_ev_margin_l2=max_import_ev_margin_l2,
            max_import_ev_margin_l3=max_import_ev_margin_l3,
            max_import_ev_margin_worst_case_total=max_import_ev_margin_worst_case_total,
            max_import_ev_margin_worst_case_l1=max_import_ev_margin_worst_case_l1,
            max_import_ev_margin_worst_case_l2=max_import_ev_margin_worst_case_l2,
            max_import_ev_margin_worst_case_l3=max_import_ev_margin_worst_case_l3,
        )

        historical_import_power_limit_import_power_limits_stored_with_the_dynamic_api.additional_properties = d
        return historical_import_power_limit_import_power_limits_stored_with_the_dynamic_api

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
