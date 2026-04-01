from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200_charge_mode import (
    PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200ChargeMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200")


@_attrs_define
class PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200:
    """
    Attributes:
        charging_enabled (bool | None): Specifies whether charging is allowed.
        charging_remote_controllable (bool | None): Specifies whether charging may be controlled via network connection.
        lock_enabled (bool | None): Specifies whether the plug is locked.
        min_requested_soc (float | None): The minimum SoC the EV shall have and keep to guarantee the range for the next
            usage.

            This is set by the user and needed for `DEPARTURE_TIME_EV` and `MIN_EV` charge modes.
            If this value is set, the `userTotalCapacity` needs to be set, too.
            Value is between 0.0 - 100.0 in %.
             Example: 30.
        departure_timestamp (datetime.datetime | None): The departure time of the EV for the `DEPARTURE_TIME_EV` charge
            mode.

            Only the time of the day is considered, not the exact date.
            If the time of day is in the past it is interpreted as tomorrow and if it in the future it is today.
        user_soc (float | None): The State of Charge (SoC) level read and set by the user for the connected EV.

            This is needed in cases where the SoC cannot be determined automatically.
            Value is between 0.0 - 100.0 in %.
             Example: 50.
        user_total_capacity (float | None): The size of the EV's battery in Wh.

            If this cannot be determined directly from the hardware, then the user enters it during the onboarding process.
            The value is needed to calculate the energy that needs to be charged to fulfill the `minRequestedSoc`.
             Example: 82000.
        max_power_calculated (float | None): The maximum potential total charge power in Watt is calculated by the
            gridBox in usual setups.

            The total power is defined as sum of all phases' power.
            It considers the maximum power supported by the EV and that the power can be curtailed by the DLM.
             Example: 8000.
        max_charge_power (float | None): The maximum total power that the EV should be charged with in Watt.

            The total power is defined as sum of all phases' power.
            EV charging power will not exceed the specified value.
             Example: 8000.
        min_charge_power (float | None): The minimum total power that the EV should be charged with in Watt.

            The total power is defined as sum of all phases' power.
            EV will only be charged if the total power is above the specified value.
             Example: 2070.
        appliance_id (UUID): ID of the EV charging station this configuration belongs to.
        created_at (datetime.datetime): Specifies when the configuration was created.
        updated_at (datetime.datetime): Specifies when the configuration was updated the last time.
        issue_timestamp (datetime.datetime | Unset): Specifies when the configuration was send or received the last time
            by the EMS.

            **Deprecated** - No longer updated, always returns the current date.
        estimated_departure_timestamp (datetime.datetime | Unset): The estimated timestamp when the desired SoC is
            reached.

            Optimally, the timestamp is close to the user's wanted `departureTimestamp`.
            The estimated timestamp is calculated by the EMS and takes into account the current SoC of the EV and the fact
            that the EV power can be curtailed by the DLM.
        charge_mode (PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200ChargeMode | Unset): Defines
            how the EV shall be charged.
              * `FORCED_EV`: EV will be charged with full power until 100% SoC. This is the default behaviour, also if there
            is no configuration set. It does not require any additional fields to be set. Also commonly referred to as
            "Quick Charge".
              * `MIN_EV`: EV will be charged with full power until the specified `minRequestedSoc` (must be provided). Also
            commonly referred to as "Safety Charge".
              * `DEPARTURE_TIME_EV`: EV will be charged until `departureTimestamp` to the `minRequestedSoc`. This means that
            initially it charges with surplus energy, but if it is not enough it will charge with full power to meet the
            requested `departureTimestamp`. Also commonly referred to as "Program Charge".
              * `SURPLUS_EV`: EV will only be charged with surplus energy regardless of SoC level. It does not require any
            additional fields to be set. Also commonly referred to as "Solar Charge".
        min_charge_power_per_phase (float | Unset): The minimum power that the EV should be charged with in Watt for one
            phase.

            EV will only be charged if **one** of the phases' power is above the specified value.
             Example: 1840.
        ev_profile_id (UUID | Unset): Represents the ID of the EV profile that is going to be used in the next charging
            session. Example: 6dd0a658-5828-4d30-bc65-a03c6d6e425f.
    """

    charging_enabled: bool | None
    charging_remote_controllable: bool | None
    lock_enabled: bool | None
    min_requested_soc: float | None
    departure_timestamp: datetime.datetime | None
    user_soc: float | None
    user_total_capacity: float | None
    max_power_calculated: float | None
    max_charge_power: float | None
    min_charge_power: float | None
    appliance_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    issue_timestamp: datetime.datetime | Unset = UNSET
    estimated_departure_timestamp: datetime.datetime | Unset = UNSET
    charge_mode: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200ChargeMode | Unset = UNSET
    min_charge_power_per_phase: float | Unset = UNSET
    ev_profile_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charging_enabled: bool | None
        charging_enabled = self.charging_enabled

        charging_remote_controllable: bool | None
        charging_remote_controllable = self.charging_remote_controllable

        lock_enabled: bool | None
        lock_enabled = self.lock_enabled

        min_requested_soc: float | None
        min_requested_soc = self.min_requested_soc

        departure_timestamp: None | str
        if isinstance(self.departure_timestamp, datetime.datetime):
            departure_timestamp = self.departure_timestamp.isoformat()
        else:
            departure_timestamp = self.departure_timestamp

        user_soc: float | None
        user_soc = self.user_soc

        user_total_capacity: float | None
        user_total_capacity = self.user_total_capacity

        max_power_calculated: float | None
        max_power_calculated = self.max_power_calculated

        max_charge_power: float | None
        max_charge_power = self.max_charge_power

        min_charge_power: float | None
        min_charge_power = self.min_charge_power

        appliance_id = str(self.appliance_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        issue_timestamp: str | Unset = UNSET
        if not isinstance(self.issue_timestamp, Unset):
            issue_timestamp = self.issue_timestamp.isoformat()

        estimated_departure_timestamp: str | Unset = UNSET
        if not isinstance(self.estimated_departure_timestamp, Unset):
            estimated_departure_timestamp = self.estimated_departure_timestamp.isoformat()

        charge_mode: str | Unset = UNSET
        if not isinstance(self.charge_mode, Unset):
            charge_mode = self.charge_mode.value

        min_charge_power_per_phase = self.min_charge_power_per_phase

        ev_profile_id: str | Unset = UNSET
        if not isinstance(self.ev_profile_id, Unset):
            ev_profile_id = str(self.ev_profile_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargingEnabled": charging_enabled,
                "chargingRemoteControllable": charging_remote_controllable,
                "lockEnabled": lock_enabled,
                "minRequestedSoc": min_requested_soc,
                "departureTimestamp": departure_timestamp,
                "userSoc": user_soc,
                "userTotalCapacity": user_total_capacity,
                "maxPowerCalculated": max_power_calculated,
                "maxChargePower": max_charge_power,
                "minChargePower": min_charge_power,
                "applianceID": appliance_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if issue_timestamp is not UNSET:
            field_dict["issueTimestamp"] = issue_timestamp
        if estimated_departure_timestamp is not UNSET:
            field_dict["estimatedDepartureTimestamp"] = estimated_departure_timestamp
        if charge_mode is not UNSET:
            field_dict["chargeMode"] = charge_mode
        if min_charge_power_per_phase is not UNSET:
            field_dict["minChargePowerPerPhase"] = min_charge_power_per_phase
        if ev_profile_id is not UNSET:
            field_dict["evProfileID"] = ev_profile_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_charging_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        charging_enabled = _parse_charging_enabled(d.pop("chargingEnabled"))

        def _parse_charging_remote_controllable(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        charging_remote_controllable = _parse_charging_remote_controllable(d.pop("chargingRemoteControllable"))

        def _parse_lock_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        lock_enabled = _parse_lock_enabled(d.pop("lockEnabled"))

        def _parse_min_requested_soc(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        min_requested_soc = _parse_min_requested_soc(d.pop("minRequestedSoc"))

        def _parse_departure_timestamp(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                departure_timestamp_type_0 = isoparse(data)

                return departure_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        departure_timestamp = _parse_departure_timestamp(d.pop("departureTimestamp"))

        def _parse_user_soc(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        user_soc = _parse_user_soc(d.pop("userSoc"))

        def _parse_user_total_capacity(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        user_total_capacity = _parse_user_total_capacity(d.pop("userTotalCapacity"))

        def _parse_max_power_calculated(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        max_power_calculated = _parse_max_power_calculated(d.pop("maxPowerCalculated"))

        def _parse_max_charge_power(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        max_charge_power = _parse_max_charge_power(d.pop("maxChargePower"))

        def _parse_min_charge_power(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        min_charge_power = _parse_min_charge_power(d.pop("minChargePower"))

        appliance_id = UUID(d.pop("applianceID"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _issue_timestamp = d.pop("issueTimestamp", UNSET)
        issue_timestamp: datetime.datetime | Unset
        if isinstance(_issue_timestamp, Unset):
            issue_timestamp = UNSET
        else:
            issue_timestamp = isoparse(_issue_timestamp)

        _estimated_departure_timestamp = d.pop("estimatedDepartureTimestamp", UNSET)
        estimated_departure_timestamp: datetime.datetime | Unset
        if isinstance(_estimated_departure_timestamp, Unset):
            estimated_departure_timestamp = UNSET
        else:
            estimated_departure_timestamp = isoparse(_estimated_departure_timestamp)

        _charge_mode = d.pop("chargeMode", UNSET)
        charge_mode: PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200ChargeMode | Unset
        if isinstance(_charge_mode, Unset):
            charge_mode = UNSET
        else:
            charge_mode = PatchGatewaysGatewayIDAppliancesApplianceIDEvConfigurationResponse200ChargeMode(_charge_mode)

        min_charge_power_per_phase = d.pop("minChargePowerPerPhase", UNSET)

        _ev_profile_id = d.pop("evProfileID", UNSET)
        ev_profile_id: UUID | Unset
        if isinstance(_ev_profile_id, Unset):
            ev_profile_id = UNSET
        else:
            ev_profile_id = UUID(_ev_profile_id)

        patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200 = cls(
            charging_enabled=charging_enabled,
            charging_remote_controllable=charging_remote_controllable,
            lock_enabled=lock_enabled,
            min_requested_soc=min_requested_soc,
            departure_timestamp=departure_timestamp,
            user_soc=user_soc,
            user_total_capacity=user_total_capacity,
            max_power_calculated=max_power_calculated,
            max_charge_power=max_charge_power,
            min_charge_power=min_charge_power,
            appliance_id=appliance_id,
            created_at=created_at,
            updated_at=updated_at,
            issue_timestamp=issue_timestamp,
            estimated_departure_timestamp=estimated_departure_timestamp,
            charge_mode=charge_mode,
            min_charge_power_per_phase=min_charge_power_per_phase,
            ev_profile_id=ev_profile_id,
        )

        patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200.additional_properties = d
        return patch_gateways_gateway_id_appliances_appliance_id_ev_configuration_response_200

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
