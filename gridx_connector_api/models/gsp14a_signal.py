from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.gsp14a_signal_lpc_server_state import GSP14ASignalLpcServerState

T = TypeVar("T", bound="GSP14ASignal")


@_attrs_define
class GSP14ASignal:
    """GSP 14A signal status for a GSP-feature.

    Attributes:
        consumption_power_limit (int | None): Value of the current consumption power limit set by the grid control box
            in mW, null means no power limit. Example: 57000000.
        received_from_dso (datetime.datetime | None): The time at which the GSP 14A signal was received at from DSO, in
            UTC using the ISO 8601 full-time format. Example: 2024-09-11T12:19:52Z.
        valid_until (datetime.datetime | None): The time the GSP 14A signal is valid until, null means valid
            indefinitely, in UTC using the ISO 8601 full-time format. Example: 2024-09-11T12:19:52Z.
        sent_by_grid_box (datetime.datetime): The time at which the GSP 14A event was sent to us by the GridBox, in UTC
            using the ISO 8601 full-time format. Example: 2024-09-11T12:19:52Z.
        lpc_server_state (GSP14ASignalLpcServerState): The current state of connection between the GridBox with the
            device serving the consumptionPowerLimit.
    """

    consumption_power_limit: int | None
    received_from_dso: datetime.datetime | None
    valid_until: datetime.datetime | None
    sent_by_grid_box: datetime.datetime
    lpc_server_state: GSP14ASignalLpcServerState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumption_power_limit: int | None
        consumption_power_limit = self.consumption_power_limit

        received_from_dso: None | str
        if isinstance(self.received_from_dso, datetime.datetime):
            received_from_dso = self.received_from_dso.isoformat()
        else:
            received_from_dso = self.received_from_dso

        valid_until: None | str
        if isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        sent_by_grid_box = self.sent_by_grid_box.isoformat()

        lpc_server_state = self.lpc_server_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consumptionPowerLimit": consumption_power_limit,
                "receivedFromDSO": received_from_dso,
                "validUntil": valid_until,
                "sentByGridBox": sent_by_grid_box,
                "lpcServerState": lpc_server_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_consumption_power_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        consumption_power_limit = _parse_consumption_power_limit(d.pop("consumptionPowerLimit"))

        def _parse_received_from_dso(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_from_dso_type_0 = isoparse(data)

                return received_from_dso_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        received_from_dso = _parse_received_from_dso(d.pop("receivedFromDSO"))

        def _parse_valid_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = isoparse(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_until = _parse_valid_until(d.pop("validUntil"))

        sent_by_grid_box = isoparse(d.pop("sentByGridBox"))

        lpc_server_state = GSP14ASignalLpcServerState(d.pop("lpcServerState"))

        gsp14a_signal = cls(
            consumption_power_limit=consumption_power_limit,
            received_from_dso=received_from_dso,
            valid_until=valid_until,
            sent_by_grid_box=sent_by_grid_box,
            lpc_server_state=lpc_server_state,
        )

        gsp14a_signal.additional_properties = d
        return gsp14a_signal

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
