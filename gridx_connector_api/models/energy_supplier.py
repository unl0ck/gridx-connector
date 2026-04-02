from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.energy_supplier_type import EnergySupplierType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergySupplier")


@_attrs_define
class EnergySupplier:
    """MetadataEnergySupplier represents the metadata related to energy supplier.

    Attributes:
        type_ (EnergySupplierType | Unset): Type determines if gridX is the energy supplier. The value is either "GRIDX"
            or "OTHER".
        unit_price (float | None | Unset): UnitPrice is unit price per kWh in EU cent. Deprecated - Use TariffV2
            instead.
        installment (float | None | Unset): Installment is the monthly payment.
        base_fee (float | None | Unset): BaseFee is the monthly base fee.
        feed_in_tariff (float | None | Unset): FeedInTariff is the cost-based compensation in EUR cent for feeding in.
            Deprecated - Use TariffV2 instead.
        expected_consumption (float | None | Unset): ExpectedConsumption is the expected annual consumption in kWh.
    """

    type_: EnergySupplierType | Unset = UNSET
    unit_price: float | None | Unset = UNSET
    installment: float | None | Unset = UNSET
    base_fee: float | None | Unset = UNSET
    feed_in_tariff: float | None | Unset = UNSET
    expected_consumption: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        unit_price: float | None | Unset
        if isinstance(self.unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = self.unit_price

        installment: float | None | Unset
        if isinstance(self.installment, Unset):
            installment = UNSET
        else:
            installment = self.installment

        base_fee: float | None | Unset
        if isinstance(self.base_fee, Unset):
            base_fee = UNSET
        else:
            base_fee = self.base_fee

        feed_in_tariff: float | None | Unset
        if isinstance(self.feed_in_tariff, Unset):
            feed_in_tariff = UNSET
        else:
            feed_in_tariff = self.feed_in_tariff

        expected_consumption: float | None | Unset
        if isinstance(self.expected_consumption, Unset):
            expected_consumption = UNSET
        else:
            expected_consumption = self.expected_consumption

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if installment is not UNSET:
            field_dict["installment"] = installment
        if base_fee is not UNSET:
            field_dict["baseFee"] = base_fee
        if feed_in_tariff is not UNSET:
            field_dict["feedInTariff"] = feed_in_tariff
        if expected_consumption is not UNSET:
            field_dict["expectedConsumption"] = expected_consumption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EnergySupplierType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnergySupplierType(_type_)

        def _parse_unit_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price = _parse_unit_price(d.pop("unitPrice", UNSET))

        def _parse_installment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        installment = _parse_installment(d.pop("installment", UNSET))

        def _parse_base_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        base_fee = _parse_base_fee(d.pop("baseFee", UNSET))

        def _parse_feed_in_tariff(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_in_tariff = _parse_feed_in_tariff(d.pop("feedInTariff", UNSET))

        def _parse_expected_consumption(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expected_consumption = _parse_expected_consumption(d.pop("expectedConsumption", UNSET))

        energy_supplier = cls(
            type_=type_,
            unit_price=unit_price,
            installment=installment,
            base_fee=base_fee,
            feed_in_tariff=feed_in_tariff,
            expected_consumption=expected_consumption,
        )

        energy_supplier.additional_properties = d
        return energy_supplier

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
