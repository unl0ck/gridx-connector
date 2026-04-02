from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_inverter_hybrid_calc_mode import AbstractInverterHybridCalcMode
from ..models.abstract_inverter_kind import AbstractInverterKind
from ..models.abstract_inverter_type import AbstractInverterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_inverter_battery_information import AbstractInverterBatteryInformation
    from ..models.abstract_inverter_inverter import AbstractInverterInverter


T = TypeVar("T", bound="AbstractInverter")


@_attrs_define
class AbstractInverter:
    """
    Attributes:
        type_ (AbstractInverterType | Unset):
        kind (AbstractInverterKind | Unset): Indicates the role of the inverter.

            Setting the kind impacts the system measurements. So it's best to set it up correctly as early as possible
            in accordance to the actual installation in order for the measurement calculation to be correct (best during
            commissioning).
        manufacturer (str | Unset): Manufacturer of the appliance. Example: SMA.
        model (str | Unset): Model of the appliance. Example: Sunny Boy Storage 2.5.
        firmware (str | Unset): Firmware version of the appliance. Example: 2.4.23.R.
        inverter (AbstractInverterInverter | Unset): The inverter specific information.
        nominal_power_limit (int | Unset): Designed maximal power output of the inverter in mW.
        hybrid_calc_mode (AbstractInverterHybridCalcMode | Unset): The calculation mode for inverters of HYBRID kind.
        battery (AbstractInverterBatteryInformation | Unset): The battery specific information for inverters of BATTERY
            and HYBRID kind.
    """

    type_: AbstractInverterType | Unset = UNSET
    kind: AbstractInverterKind | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    inverter: AbstractInverterInverter | Unset = UNSET
    nominal_power_limit: int | Unset = UNSET
    hybrid_calc_mode: AbstractInverterHybridCalcMode | Unset = UNSET
    battery: AbstractInverterBatteryInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        manufacturer = self.manufacturer

        model = self.model

        firmware = self.firmware

        inverter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inverter, Unset):
            inverter = self.inverter.to_dict()

        nominal_power_limit = self.nominal_power_limit

        hybrid_calc_mode: int | Unset = UNSET
        if not isinstance(self.hybrid_calc_mode, Unset):
            hybrid_calc_mode = self.hybrid_calc_mode.value

        battery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery, Unset):
            battery = self.battery.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if kind is not UNSET:
            field_dict["kind"] = kind
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if inverter is not UNSET:
            field_dict["inverter"] = inverter
        if nominal_power_limit is not UNSET:
            field_dict["nominalPowerLimit"] = nominal_power_limit
        if hybrid_calc_mode is not UNSET:
            field_dict["hybridCalcMode"] = hybrid_calc_mode
        if battery is not UNSET:
            field_dict["battery"] = battery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_inverter_battery_information import AbstractInverterBatteryInformation
        from ..models.abstract_inverter_inverter import AbstractInverterInverter

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractInverterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractInverterType(_type_)

        _kind = d.pop("kind", UNSET)
        kind: AbstractInverterKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = AbstractInverterKind(_kind)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        _inverter = d.pop("inverter", UNSET)
        inverter: AbstractInverterInverter | Unset
        if isinstance(_inverter, Unset):
            inverter = UNSET
        else:
            inverter = AbstractInverterInverter.from_dict(_inverter)

        nominal_power_limit = d.pop("nominalPowerLimit", UNSET)

        _hybrid_calc_mode = d.pop("hybridCalcMode", UNSET)
        hybrid_calc_mode: AbstractInverterHybridCalcMode | Unset
        if isinstance(_hybrid_calc_mode, Unset):
            hybrid_calc_mode = UNSET
        else:
            hybrid_calc_mode = AbstractInverterHybridCalcMode(_hybrid_calc_mode)

        _battery = d.pop("battery", UNSET)
        battery: AbstractInverterBatteryInformation | Unset
        if isinstance(_battery, Unset):
            battery = UNSET
        else:
            battery = AbstractInverterBatteryInformation.from_dict(_battery)

        abstract_inverter = cls(
            type_=type_,
            kind=kind,
            manufacturer=manufacturer,
            model=model,
            firmware=firmware,
            inverter=inverter,
            nominal_power_limit=nominal_power_limit,
            hybrid_calc_mode=hybrid_calc_mode,
            battery=battery,
        )

        abstract_inverter.additional_properties = d
        return abstract_inverter

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
