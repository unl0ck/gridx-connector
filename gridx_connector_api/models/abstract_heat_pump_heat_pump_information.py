from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.abstract_heat_pump_heat_pump_information_type import AbstractHeatPumpHeatPumpInformationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractHeatPumpHeatPumpInformation")


@_attrs_define
class AbstractHeatPumpHeatPumpInformation:
    """The heat pump specific information.

    Attributes:
        type_ (AbstractHeatPumpHeatPumpInformationType | Unset): Describes the specific type of the heat pump.
        controllable (bool | Unset): Specifies whether this appliance is controllable by the EMS.
        behind_gcp (bool | Unset): Specifies whether this heat pump exists behind a GCP meter.
        with_own_tariff (bool | Unset): Specifies whether this heat pump has its own meter and tariff.
        user_control_enabled (bool | Unset): Specifies whether EMS control of this appliance is enabled by the user.
    """

    type_: AbstractHeatPumpHeatPumpInformationType | Unset = UNSET
    controllable: bool | Unset = UNSET
    behind_gcp: bool | Unset = UNSET
    with_own_tariff: bool | Unset = UNSET
    user_control_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        controllable = self.controllable

        behind_gcp = self.behind_gcp

        with_own_tariff = self.with_own_tariff

        user_control_enabled = self.user_control_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if controllable is not UNSET:
            field_dict["controllable"] = controllable
        if behind_gcp is not UNSET:
            field_dict["behindGCP"] = behind_gcp
        if with_own_tariff is not UNSET:
            field_dict["withOwnTariff"] = with_own_tariff
        if user_control_enabled is not UNSET:
            field_dict["userControlEnabled"] = user_control_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractHeatPumpHeatPumpInformationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractHeatPumpHeatPumpInformationType(_type_)

        controllable = d.pop("controllable", UNSET)

        behind_gcp = d.pop("behindGCP", UNSET)

        with_own_tariff = d.pop("withOwnTariff", UNSET)

        user_control_enabled = d.pop("userControlEnabled", UNSET)

        abstract_heat_pump_heat_pump_information = cls(
            type_=type_,
            controllable=controllable,
            behind_gcp=behind_gcp,
            with_own_tariff=with_own_tariff,
            user_control_enabled=user_control_enabled,
        )

        abstract_heat_pump_heat_pump_information.additional_properties = d
        return abstract_heat_pump_heat_pump_information

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
