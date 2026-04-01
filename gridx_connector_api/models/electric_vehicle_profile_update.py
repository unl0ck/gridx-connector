from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElectricVehicleProfileUpdate")


@_attrs_define
class ElectricVehicleProfileUpdate:
    """
    Attributes:
        name (str | Unset): Name of the EV profile. Example: My profile.
        manufacturer (str | Unset): The manufacturer of the EV. Example: Tesla.
        model (str | Unset): The model of the EV (manufacturer-dependent). Example: Model-3.
        color (str | Unset): The color of the EV. Example: red.
        capacity (float | Unset): Battery capacity of the EV in Wh. Example: 12000.
        average_consumption (float | Unset): The average consumption of the EV provided in Wh/100km. Example: 30000.
        phases_count (float | Unset): The number of phases used for charging the EV (range 1-3). Example: 1.
        min_charge_power (float | Unset): The minimum total power that the EV should be charged with in Watt.

            If the EV Profile is assigned to a charging station, this configuration will be applied,
            otherwise, the [EV Charging Station Configuration](https://developer.gridx.ai/reference/get_gateways-gatewayid-
            appliances-applianceid-ev-configuration) will be used.
             Example: 8000.
        user_soc (float | Unset): The State of Charge (SoC) level read and set by the user for the connected EV.

            This is needed in cases where the SoC cannot be determined automatically.
            Value is between 0.0 - 100.0 in %.
            If the EV Profile is assigned to a charging station, this configuration will be applied,
            otherwise, the [EV Charging Station Configuration](https://developer.gridx.ai/reference/get_gateways-gatewayid-
            appliances-applianceid-ev-configuration) will be used.
             Example: 50.
        image (str | Unset): Image to be used when displaying the EV profile in base64 encoding. Format must be `jpeg`
            or `png`. Example: data:image/jpeg;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==.
        min_charge_power_per_phase (float | Unset): Defines the minimum charge power in W for one phase set by the user.
            Example: 2070.
        min_requested_soc (float | Unset): The minimum state of charge the EV shall have and keep to guarantee the range
            for the next usage. This is set by the user. The value ranges from 0.0 - 100.0 in %. Example: 70.
    """

    name: str | Unset = UNSET
    manufacturer: str | Unset = UNSET
    model: str | Unset = UNSET
    color: str | Unset = UNSET
    capacity: float | Unset = UNSET
    average_consumption: float | Unset = UNSET
    phases_count: float | Unset = UNSET
    min_charge_power: float | Unset = UNSET
    user_soc: float | Unset = UNSET
    image: str | Unset = UNSET
    min_charge_power_per_phase: float | Unset = UNSET
    min_requested_soc: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        manufacturer = self.manufacturer

        model = self.model

        color = self.color

        capacity = self.capacity

        average_consumption = self.average_consumption

        phases_count = self.phases_count

        min_charge_power = self.min_charge_power

        user_soc = self.user_soc

        image = self.image

        min_charge_power_per_phase = self.min_charge_power_per_phase

        min_requested_soc = self.min_requested_soc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if color is not UNSET:
            field_dict["color"] = color
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if average_consumption is not UNSET:
            field_dict["averageConsumption"] = average_consumption
        if phases_count is not UNSET:
            field_dict["phasesCount"] = phases_count
        if min_charge_power is not UNSET:
            field_dict["minChargePower"] = min_charge_power
        if user_soc is not UNSET:
            field_dict["userSoc"] = user_soc
        if image is not UNSET:
            field_dict["image"] = image
        if min_charge_power_per_phase is not UNSET:
            field_dict["minChargePowerPerPhase"] = min_charge_power_per_phase
        if min_requested_soc is not UNSET:
            field_dict["minRequestedSoc"] = min_requested_soc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        color = d.pop("color", UNSET)

        capacity = d.pop("capacity", UNSET)

        average_consumption = d.pop("averageConsumption", UNSET)

        phases_count = d.pop("phasesCount", UNSET)

        min_charge_power = d.pop("minChargePower", UNSET)

        user_soc = d.pop("userSoc", UNSET)

        image = d.pop("image", UNSET)

        min_charge_power_per_phase = d.pop("minChargePowerPerPhase", UNSET)

        min_requested_soc = d.pop("minRequestedSoc", UNSET)

        electric_vehicle_profile_update = cls(
            name=name,
            manufacturer=manufacturer,
            model=model,
            color=color,
            capacity=capacity,
            average_consumption=average_consumption,
            phases_count=phases_count,
            min_charge_power=min_charge_power,
            user_soc=user_soc,
            image=image,
            min_charge_power_per_phase=min_charge_power_per_phase,
            min_requested_soc=min_requested_soc,
        )

        electric_vehicle_profile_update.additional_properties = d
        return electric_vehicle_profile_update

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
