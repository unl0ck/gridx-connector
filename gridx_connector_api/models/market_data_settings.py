from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataSettings")


@_attrs_define
class MarketDataSettings:
    """Settings specific to market-data-based tariffs.

    Attributes:
        feedin_offset (float | Unset): Sets the fee per kWh on top of market prices for feed-in tariffs. Example: 2.5.
        offtake_offset (float | Unset): Sets the fee per kWh on top of market prices for off-take tariffs. Example: 2.5.
        provider_fee (float | Unset): Additional fee per kWh on top, after applying VAT. Example: 10.
        vat (float | Unset): The VAT is the value-added tax rate expressed as a decimal number. Example: 0.12.
    """

    feedin_offset: float | Unset = UNSET
    offtake_offset: float | Unset = UNSET
    provider_fee: float | Unset = UNSET
    vat: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedin_offset = self.feedin_offset

        offtake_offset = self.offtake_offset

        provider_fee = self.provider_fee

        vat = self.vat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feedin_offset is not UNSET:
            field_dict["feedinOffset"] = feedin_offset
        if offtake_offset is not UNSET:
            field_dict["offtakeOffset"] = offtake_offset
        if provider_fee is not UNSET:
            field_dict["providerFee"] = provider_fee
        if vat is not UNSET:
            field_dict["vat"] = vat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedin_offset = d.pop("feedinOffset", UNSET)

        offtake_offset = d.pop("offtakeOffset", UNSET)

        provider_fee = d.pop("providerFee", UNSET)

        vat = d.pop("vat", UNSET)

        market_data_settings = cls(
            feedin_offset=feedin_offset,
            offtake_offset=offtake_offset,
            provider_fee=provider_fee,
            vat=vat,
        )

        market_data_settings.additional_properties = d
        return market_data_settings

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
