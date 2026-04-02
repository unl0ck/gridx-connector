from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergyMarketData")


@_attrs_define
class EnergyMarketData:
    """
    Attributes:
        price_unit (str | Unset): Currency unit which the prices are (ct/kWh). Example: EUR/MWh.
        average_price_day (float | Unset): Average price of the second to last day in EUR/MWh. Example: 33.6.
        period_start (str | Unset): Starting date at which the prices are fetched in RFC3339 format. Example:
            2020-09-24T00:00:00Z.
        period_end (str | Unset): Ending date at which the prices are fetched in RFC3339 format. Example:
            2022-09-27T00:00:00Z.
        total_prices (list[list[float | str]] | Unset): Contains an array of arrays in the format [time, price].

            The fetched prices are in the following order:
            * Average prices for each day between [PeriodStart, SecondToLastDay].
            * Prices for the second to last day from the given interval with resolution 1h.
            * Price for the last day of the given interval with resolution 1h.
             Example: [['2022-09-25T22:00:00Z', 2.5], ['2022-09-25T23:00:00Z', 1], ['2022-09-26T00:00:00Z', 2],
            ['2022-09-26T01:00:00Z', 3], ['2022-09-26T02:00:00Z', 4], ['2022-09-26T23:00:00Z', 1], ['2022-09-27T00:00:00Z',
            2], ['2022-09-27T01:00:00Z', 3], ['2022-09-27T02:00:00Z', 4]].
    """

    price_unit: str | Unset = UNSET
    average_price_day: float | Unset = UNSET
    period_start: str | Unset = UNSET
    period_end: str | Unset = UNSET
    total_prices: list[list[float | str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price_unit = self.price_unit

        average_price_day = self.average_price_day

        period_start = self.period_start

        period_end = self.period_end

        total_prices: list[list[float | str]] | Unset = UNSET
        if not isinstance(self.total_prices, Unset):
            total_prices = []
            for total_prices_item_data in self.total_prices:
                total_prices_item = []
                for total_prices_item_item_data in total_prices_item_data:
                    total_prices_item_item: float | str
                    total_prices_item_item = total_prices_item_item_data
                    total_prices_item.append(total_prices_item_item)

                total_prices.append(total_prices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_unit is not UNSET:
            field_dict["priceUnit"] = price_unit
        if average_price_day is not UNSET:
            field_dict["averagePriceDay"] = average_price_day
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if total_prices is not UNSET:
            field_dict["totalPrices"] = total_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_unit = d.pop("priceUnit", UNSET)

        average_price_day = d.pop("averagePriceDay", UNSET)

        period_start = d.pop("periodStart", UNSET)

        period_end = d.pop("periodEnd", UNSET)

        _total_prices = d.pop("totalPrices", UNSET)
        total_prices: list[list[float | str]] | Unset = UNSET
        if _total_prices is not UNSET:
            total_prices = []
            for total_prices_item_data in _total_prices:
                total_prices_item = []
                _total_prices_item = total_prices_item_data
                for total_prices_item_item_data in _total_prices_item:

                    def _parse_total_prices_item_item(data: object) -> float | str:
                        return cast(float | str, data)

                    total_prices_item_item = _parse_total_prices_item_item(total_prices_item_item_data)

                    total_prices_item.append(total_prices_item_item)

                total_prices.append(total_prices_item)

        energy_market_data = cls(
            price_unit=price_unit,
            average_price_day=average_price_day,
            period_start=period_start,
            period_end=period_end,
            total_prices=total_prices,
        )

        energy_market_data.additional_properties = d
        return energy_market_data

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
