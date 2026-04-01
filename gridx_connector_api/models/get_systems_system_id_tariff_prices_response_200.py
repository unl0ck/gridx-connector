from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_systems_system_id_tariff_prices_response_200_end_price_tariff_v2_period import (
        GetSystemsSystemIDTariffPricesResponse200EndPriceTariffV2Period,
    )


T = TypeVar("T", bound="GetSystemsSystemIDTariffPricesResponse200")


@_attrs_define
class GetSystemsSystemIDTariffPricesResponse200:
    """
    Attributes:
        currency (str): Currency code (ISO 4217) Example: EUR.
        periods (list[GetSystemsSystemIDTariffPricesResponse200EndPriceTariffV2Period]): List of periods containing end
            prices over non-overlapping periods.
            The periods are sorted chronologically.
        name (None | str): Name of the underlying TariffV2.
        from_ (datetime.datetime): Time at which the contained periods starts in the RFC3339 format.
             Example: 2018-04-01T00:10:00Z.
        to (datetime.datetime): Time at which the contained period ends in the RFC3339 format.
             Example: 2018-04-01T00:10:00Z.
    """

    currency: str
    periods: list[GetSystemsSystemIDTariffPricesResponse200EndPriceTariffV2Period]
    name: None | str
    from_: datetime.datetime
    to: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        periods = []
        for periods_item_data in self.periods:
            periods_item = periods_item_data.to_dict()
            periods.append(periods_item)

        name: None | str
        name = self.name

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "periods": periods,
                "name": name,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_tariff_prices_response_200_end_price_tariff_v2_period import (
            GetSystemsSystemIDTariffPricesResponse200EndPriceTariffV2Period,
        )

        d = dict(src_dict)
        currency = d.pop("currency")

        periods = []
        _periods = d.pop("periods")
        for periods_item_data in _periods:
            periods_item = GetSystemsSystemIDTariffPricesResponse200EndPriceTariffV2Period.from_dict(periods_item_data)

            periods.append(periods_item)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        get_systems_system_id_tariff_prices_response_200 = cls(
            currency=currency,
            periods=periods,
            name=name,
            from_=from_,
            to=to,
        )

        get_systems_system_id_tariff_prices_response_200.additional_properties = d
        return get_systems_system_id_tariff_prices_response_200

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
