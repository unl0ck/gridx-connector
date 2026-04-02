from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_inverter_battery_information_control_settings import (
        AbstractInverterBatteryInformationControlSettings,
    )


T = TypeVar("T", bound="AbstractInverterBatteryInformation")


@_attrs_define
class AbstractInverterBatteryInformation:
    """The battery specific information for inverters of BATTERY and HYBRID kind.

    Attributes:
        max_charge (int | Unset):  Example: 501.
        max_discharge (int | Unset):  Example: 501.
        controllable (bool | Unset): Controllable is true if the battery charging/discharging can be controlled.
        discharge_limit (int | Unset): DischargeLimit is the minimum state of charge in % from 0-100 to discharge to.
        recharge_limit (int | Unset): RechargeLimit is the state of charge in % from 0-100 to which the battery needs to
            recharge before allowing discharging again.
        control_settings (AbstractInverterBatteryInformationControlSettings | Unset): Indicates the currently desired
            control settings for the battery.
    """

    max_charge: int | Unset = UNSET
    max_discharge: int | Unset = UNSET
    controllable: bool | Unset = UNSET
    discharge_limit: int | Unset = UNSET
    recharge_limit: int | Unset = UNSET
    control_settings: AbstractInverterBatteryInformationControlSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_charge = self.max_charge

        max_discharge = self.max_discharge

        controllable = self.controllable

        discharge_limit = self.discharge_limit

        recharge_limit = self.recharge_limit

        control_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_settings, Unset):
            control_settings = self.control_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_charge is not UNSET:
            field_dict["maxCharge"] = max_charge
        if max_discharge is not UNSET:
            field_dict["maxDischarge"] = max_discharge
        if controllable is not UNSET:
            field_dict["controllable"] = controllable
        if discharge_limit is not UNSET:
            field_dict["dischargeLimit"] = discharge_limit
        if recharge_limit is not UNSET:
            field_dict["rechargeLimit"] = recharge_limit
        if control_settings is not UNSET:
            field_dict["controlSettings"] = control_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_inverter_battery_information_control_settings import (
            AbstractInverterBatteryInformationControlSettings,
        )

        d = dict(src_dict)
        max_charge = d.pop("maxCharge", UNSET)

        max_discharge = d.pop("maxDischarge", UNSET)

        controllable = d.pop("controllable", UNSET)

        discharge_limit = d.pop("dischargeLimit", UNSET)

        recharge_limit = d.pop("rechargeLimit", UNSET)

        _control_settings = d.pop("controlSettings", UNSET)
        control_settings: AbstractInverterBatteryInformationControlSettings | Unset
        if isinstance(_control_settings, Unset):
            control_settings = UNSET
        else:
            control_settings = AbstractInverterBatteryInformationControlSettings.from_dict(_control_settings)

        abstract_inverter_battery_information = cls(
            max_charge=max_charge,
            max_discharge=max_discharge,
            controllable=controllable,
            discharge_limit=discharge_limit,
            recharge_limit=recharge_limit,
            control_settings=control_settings,
        )

        abstract_inverter_battery_information.additional_properties = d
        return abstract_inverter_battery_information

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
