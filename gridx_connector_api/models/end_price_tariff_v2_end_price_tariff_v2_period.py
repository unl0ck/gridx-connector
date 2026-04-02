from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndPriceTariffV2EndPriceTariffV2Period")


@_attrs_define
class EndPriceTariffV2EndPriceTariffV2Period:
    """Represents a period of a TariffV2 with end prices.
    End prices are prices with applied offset, VAT and provider fee.

        Attributes:
            from_ (datetime.datetime): Time at which the period starts in the RFC3339 format.
                 Example: 2018-04-01T00:10:00Z.
            to (datetime.datetime): Time at which the period ends in the RFC3339 format.
                 Example: 2018-04-01T00:10:00Z.
            feedin_price (float): Price including offset, VAT and provider fee per kWh for fed in energy in the period
                [from, to). Example: 0.09.
            offtake_price (float): Price including offset, VAT and provider fee per kWh for consumed energy in the period
                [from, to). Example: 0.4.
            market_price (float | None | Unset): Raw market price (Day-Ahead EPEX Spot price with 60min resolution) per kWh
                at the time of this period in the bidding zone of the system.
                Returned regardless if underlying tariff has a market data type or not (if available).

                For static tariffs (both offtake & feedin =STATIC) this can be `null`, when there is no market price for the
                requested period.
                 Example: 0.15.
    """

    from_: datetime.datetime
    to: datetime.datetime
    feedin_price: float
    offtake_price: float
    market_price: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        feedin_price = self.feedin_price

        offtake_price = self.offtake_price

        market_price: float | None | Unset
        if isinstance(self.market_price, Unset):
            market_price = UNSET
        else:
            market_price = self.market_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "feedinPrice": feedin_price,
                "offtakePrice": offtake_price,
            }
        )
        if market_price is not UNSET:
            field_dict["marketPrice"] = market_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        feedin_price = d.pop("feedinPrice")

        offtake_price = d.pop("offtakePrice")

        def _parse_market_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_price = _parse_market_price(d.pop("marketPrice", UNSET))

        end_price_tariff_v2_end_price_tariff_v2_period = cls(
            from_=from_,
            to=to,
            feedin_price=feedin_price,
            offtake_price=offtake_price,
            market_price=market_price,
        )

        end_price_tariff_v2_end_price_tariff_v2_period.additional_properties = d
        return end_price_tariff_v2_end_price_tariff_v2_period

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
