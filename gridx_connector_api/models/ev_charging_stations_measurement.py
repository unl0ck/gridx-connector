from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EVChargingStationsMeasurement")


@_attrs_define
class EVChargingStationsMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        appliance_id (UUID | Unset): Unique identifier
        type_ (str | Unset): Describes the 'physical' type of the appliance.
        kind (str | Unset): Indicates the role of the EVCS.
        l_1_voltage (int | Unset): Voltage for first phase in mW.
        l_2_voltage (int | Unset): Voltage for second phase in mW.
        l_3_voltage (int | Unset): Voltage for third phase in mW.
        l_1_current (int | Unset): Current for first phase in mA.
        l_2_current (int | Unset): Current for second phase in mA.
        l_3_current (int | Unset): Current for third phase in mA.
        real_power (int | Unset): Real Power in mW. Positive values mean charging, negative values
            mean discharging (V2G; currently not done).
        l_1_real_power (int | Unset): Real Power L1 in mW.
        l_2_real_power (int | Unset): Real Power L2 in mW.
        l_3_real_power (int | Unset): Real Power L3 in mW.
        max_charge (int | Unset): Maximum allowed charge power in mW.
        min_charge (int | Unset): Minimum allowed charge power in mW, below this power the EV won't
            charge.
        station_state (str | Unset): State indicating whether the charging station is charging, ready, in
            error state, etc.
        plug_state (str | Unset): State indicates whether an EV is plugged into the charging station.
        plugged_in (bool | Unset): PluggedIn true if an electric vehicle is currently plugged into the
            charging station.
        token_id (str | Unset): TokenID is the used authentication token at the charging station.
    """

    measured_at: datetime.datetime | Unset = UNSET
    appliance_id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    kind: str | Unset = UNSET
    l_1_voltage: int | Unset = UNSET
    l_2_voltage: int | Unset = UNSET
    l_3_voltage: int | Unset = UNSET
    l_1_current: int | Unset = UNSET
    l_2_current: int | Unset = UNSET
    l_3_current: int | Unset = UNSET
    real_power: int | Unset = UNSET
    l_1_real_power: int | Unset = UNSET
    l_2_real_power: int | Unset = UNSET
    l_3_real_power: int | Unset = UNSET
    max_charge: int | Unset = UNSET
    min_charge: int | Unset = UNSET
    station_state: str | Unset = UNSET
    plug_state: str | Unset = UNSET
    plugged_in: bool | Unset = UNSET
    token_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        appliance_id: str | Unset = UNSET
        if not isinstance(self.appliance_id, Unset):
            appliance_id = str(self.appliance_id)

        type_ = self.type_

        kind = self.kind

        l_1_voltage = self.l_1_voltage

        l_2_voltage = self.l_2_voltage

        l_3_voltage = self.l_3_voltage

        l_1_current = self.l_1_current

        l_2_current = self.l_2_current

        l_3_current = self.l_3_current

        real_power = self.real_power

        l_1_real_power = self.l_1_real_power

        l_2_real_power = self.l_2_real_power

        l_3_real_power = self.l_3_real_power

        max_charge = self.max_charge

        min_charge = self.min_charge

        station_state = self.station_state

        plug_state = self.plug_state

        plugged_in = self.plugged_in

        token_id = self.token_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if appliance_id is not UNSET:
            field_dict["applianceID"] = appliance_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if kind is not UNSET:
            field_dict["kind"] = kind
        if l_1_voltage is not UNSET:
            field_dict["l1Voltage"] = l_1_voltage
        if l_2_voltage is not UNSET:
            field_dict["l2Voltage"] = l_2_voltage
        if l_3_voltage is not UNSET:
            field_dict["l3Voltage"] = l_3_voltage
        if l_1_current is not UNSET:
            field_dict["l1Current"] = l_1_current
        if l_2_current is not UNSET:
            field_dict["l2Current"] = l_2_current
        if l_3_current is not UNSET:
            field_dict["l3Current"] = l_3_current
        if real_power is not UNSET:
            field_dict["realPower"] = real_power
        if l_1_real_power is not UNSET:
            field_dict["l1RealPower"] = l_1_real_power
        if l_2_real_power is not UNSET:
            field_dict["l2RealPower"] = l_2_real_power
        if l_3_real_power is not UNSET:
            field_dict["l3RealPower"] = l_3_real_power
        if max_charge is not UNSET:
            field_dict["maxCharge"] = max_charge
        if min_charge is not UNSET:
            field_dict["minCharge"] = min_charge
        if station_state is not UNSET:
            field_dict["stationState"] = station_state
        if plug_state is not UNSET:
            field_dict["plugState"] = plug_state
        if plugged_in is not UNSET:
            field_dict["pluggedIn"] = plugged_in
        if token_id is not UNSET:
            field_dict["tokenID"] = token_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        _appliance_id = d.pop("applianceID", UNSET)
        appliance_id: UUID | Unset
        if isinstance(_appliance_id, Unset):
            appliance_id = UNSET
        else:
            appliance_id = UUID(_appliance_id)

        type_ = d.pop("type", UNSET)

        kind = d.pop("kind", UNSET)

        l_1_voltage = d.pop("l1Voltage", UNSET)

        l_2_voltage = d.pop("l2Voltage", UNSET)

        l_3_voltage = d.pop("l3Voltage", UNSET)

        l_1_current = d.pop("l1Current", UNSET)

        l_2_current = d.pop("l2Current", UNSET)

        l_3_current = d.pop("l3Current", UNSET)

        real_power = d.pop("realPower", UNSET)

        l_1_real_power = d.pop("l1RealPower", UNSET)

        l_2_real_power = d.pop("l2RealPower", UNSET)

        l_3_real_power = d.pop("l3RealPower", UNSET)

        max_charge = d.pop("maxCharge", UNSET)

        min_charge = d.pop("minCharge", UNSET)

        station_state = d.pop("stationState", UNSET)

        plug_state = d.pop("plugState", UNSET)

        plugged_in = d.pop("pluggedIn", UNSET)

        token_id = d.pop("tokenID", UNSET)

        ev_charging_stations_measurement = cls(
            measured_at=measured_at,
            appliance_id=appliance_id,
            type_=type_,
            kind=kind,
            l_1_voltage=l_1_voltage,
            l_2_voltage=l_2_voltage,
            l_3_voltage=l_3_voltage,
            l_1_current=l_1_current,
            l_2_current=l_2_current,
            l_3_current=l_3_current,
            real_power=real_power,
            l_1_real_power=l_1_real_power,
            l_2_real_power=l_2_real_power,
            l_3_real_power=l_3_real_power,
            max_charge=max_charge,
            min_charge=min_charge,
            station_state=station_state,
            plug_state=plug_state,
            plugged_in=plugged_in,
            token_id=token_id,
        )

        ev_charging_stations_measurement.additional_properties = d
        return ev_charging_stations_measurement

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
