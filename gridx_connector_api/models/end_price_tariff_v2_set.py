from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.end_price_tariff_v2_set_end_price_tariff_v2_period import EndPriceTariffV2SetEndPriceTariffV2Period


T = TypeVar("T", bound="EndPriceTariffV2Set")


@_attrs_define
class EndPriceTariffV2Set:
    """
    Attributes:
        periods (list[EndPriceTariffV2SetEndPriceTariffV2Period]): List of periods containing end prices over non-
            overlapping periods.
            The periods are sorted chronologically.
        currency (str | Unset): Currency code (ISO 4217)
            If not set, the currency of the tariff is used.
             Example: EUR.
    """

    periods: list[EndPriceTariffV2SetEndPriceTariffV2Period]
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periods = []
        for periods_item_data in self.periods:
            periods_item = periods_item_data.to_dict()
            periods.append(periods_item)

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periods": periods,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.end_price_tariff_v2_set_end_price_tariff_v2_period import (
            EndPriceTariffV2SetEndPriceTariffV2Period,
        )

        d = dict(src_dict)
        periods = []
        _periods = d.pop("periods")
        for periods_item_data in _periods:
            periods_item = EndPriceTariffV2SetEndPriceTariffV2Period.from_dict(periods_item_data)

            periods.append(periods_item)

        currency = d.pop("currency", UNSET)

        end_price_tariff_v2_set = cls(
            periods=periods,
            currency=currency,
        )

        end_price_tariff_v2_set.additional_properties = d
        return end_price_tariff_v2_set

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
