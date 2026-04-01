from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KPIHistoryPeriodsItem")


@_attrs_define
class KPIHistoryPeriodsItem:
    """Time-of-Use KPI record.

    Attributes:
        from_ (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the beginning of the period.
             Example: 2020-09-21T00:00:00Z.
        to (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the end of the period.
             Example: 2020-09-22T00:00:00Z.
        tou_cost (float | Unset): ToU cost for the requested interval.
        tou_cost_currency (str | Unset): A currency for a ToU cost for the requested interval.
        sso_cost (float | Unset): SSO cost for the requested interval.
        sso_cost_currency (str | Unset): A currency for a SSO cost for the requested interval.
        error_code (str | Unset): Error code describing the reason of a failed saving calculation run.
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    tou_cost: float | Unset = UNSET
    tou_cost_currency: str | Unset = UNSET
    sso_cost: float | Unset = UNSET
    sso_cost_currency: str | Unset = UNSET
    error_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        tou_cost = self.tou_cost

        tou_cost_currency = self.tou_cost_currency

        sso_cost = self.sso_cost

        sso_cost_currency = self.sso_cost_currency

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if tou_cost is not UNSET:
            field_dict["touCost"] = tou_cost
        if tou_cost_currency is not UNSET:
            field_dict["touCostCurrency"] = tou_cost_currency
        if sso_cost is not UNSET:
            field_dict["ssoCost"] = sso_cost
        if sso_cost_currency is not UNSET:
            field_dict["ssoCostCurrency"] = sso_cost_currency
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        tou_cost = d.pop("touCost", UNSET)

        tou_cost_currency = d.pop("touCostCurrency", UNSET)

        sso_cost = d.pop("ssoCost", UNSET)

        sso_cost_currency = d.pop("ssoCostCurrency", UNSET)

        error_code = d.pop("errorCode", UNSET)

        kpi_history_periods_item = cls(
            from_=from_,
            to=to,
            tou_cost=tou_cost,
            tou_cost_currency=tou_cost_currency,
            sso_cost=sso_cost,
            sso_cost_currency=sso_cost_currency,
            error_code=error_code,
        )

        kpi_history_periods_item.additional_properties = d
        return kpi_history_periods_item

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
