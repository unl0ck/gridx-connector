from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.run_status_error_code import RunStatusErrorCode
from ..models.run_status_status import RunStatusStatus
from ..models.run_status_warnings_item import RunStatusWarningsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunStatus")


@_attrs_define
class RunStatus:
    """
    Attributes:
        from_ (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the beginning of the period.
             Example: 2020-09-21T00:00:00Z.
        to (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the end of the period.
             Example: 2020-09-21T00:15:00Z.
        status (RunStatusStatus | Unset): Operational status of Time-of-Use for a specific run.

            * `ONLINE` - Time-of-Use optimization is running successfully.
            * `SUBOPTIMAL` - Time-of-Use optimization is running suboptimally.
            * `OFFLINE` - Time-of-Use optimization failed.
            * `DISABLED` - Time-of-Use optimization is disabled for the system.
            * `INITIALIZING` - Time-of-Use optimization is initializing, it may take up to 48h.
             Example: ONLINE.
        error_code (RunStatusErrorCode | Unset): Most recent error causing a failure of Time-of-Use specific run.
            * `STATIC_PRICES` - Time-of-Use failing due to import and export prices are constant.
            * `MISSING_PRICES` - Time-of-Use failing due to missing import and export prices.
            * `INCOMPLETE_PRICES` - Time-of-Use failing due to incomplete import and export prices.
            * `MISSING_APPLIANCES` - Time-of-Use failing due to missing appliances in a system.
            * `MISSING_GRID_METER` - Time-of-Use failing due to missing grid meter.
            * `MULTIPLE_GRID_METERS` - Time-of-Use failing due to multiple grid meters within a system.
            * `MULTIPLE_BATTERIES` - Time-of-Use failing due to multiple batteries within a system.
            * `MULTIPLE_EVCS` - Time-of-Use failing due to multiple EV charging stations within a system.
            * `MULTIPLE_HEAT_PUMPS` - Time-of-Use failing due to multiple heat pumps within a system.
            * `MULTIPLE_PVS_CURTAILMENT` - Time-of-Use failing due to multiple PVs within a system with PV curtailment
            enabled.
            * `MISSING_CONTROLLABLE_APPLIANCE` - Time-of-Use failing due to missing controllable device (battery, EV or heat
            pump).
            * `OFFLINE_APPLIANCE` - Time-of-Use failing due to an offline appliance.
            * `EMS_NOT_ENABLED` - Time-of-Use failing due to energy management not being enabled on the system.
            * `EMS_CONSENT_NOT_GIVEN` - Time-of-Use failing due to consent to energy management not being given for the
            system.
            * `UNKNOWN_INVERTER` - Time-of-Use failing due to an unknown inverter.
            * `MISSING_HISTORICAL_DATA` - Time-of-Use failing due to insufficient historical data to generate forecasts.
            * `PV_CURTAILMENT_NOT_SUPPORTED` - Time-of-Use failing because the inverter does not support PV power
            curtailment.
            * `MISSING_FUSE_IMPORT_LIMIT` - Time-of-Use failing due to missing fuse protection import limit.
            * `INTERNAL_ERROR` - Time-of-Use failing due to an unknown, internal issue.
             Example: INTERNAL_ERROR.
        warnings (list[RunStatusWarningsItem] | Unset): All the relevant warnings that occurred during a Time-of-Use
            specific run.

            * `MISSING_EV_CONFIG` - Time-of-Use not working optimally due to missing EV configuration.
            * `MISSING_EV_PROFILE` - Time-of-Use not working optimally due to missing EV profile.
            * `UNSUPPORTED_CHARGE_MODE_QUICK` - Time-of-Use not working optimally due to EV set to Quick Charge Mode, which
            is not supported.
            * `UNSUPPORTED_CHARGE_MODE_SURPLUS` - Time-of-Use not working optimally due to EV set to Surplus Charge Mode,
            which is not supported.
            * `UNSUPPORTED_CHARGE_MODE_SAFETY` - Time-of-Use not working optimally due to EV set to Safety Charge Mode,
            which is not supported.
            * `UNSUPPORTED_CHARGE_MODE_UNKNOWN` - Time-of-Use not working optimally due to EV set to unknown charge mode.
             Example: ['MISSING_EV_CONFIG'].
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    status: RunStatusStatus | Unset = UNSET
    error_code: RunStatusErrorCode | Unset = UNSET
    warnings: list[RunStatusWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.value
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if status is not UNSET:
            field_dict["status"] = status
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        _status = d.pop("status", UNSET)
        status: RunStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RunStatusStatus(_status)

        _error_code = d.pop("error_code", UNSET)
        error_code: RunStatusErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = RunStatusErrorCode(_error_code)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[RunStatusWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = RunStatusWarningsItem(warnings_item_data)

                warnings.append(warnings_item)

        run_status = cls(
            from_=from_,
            to=to,
            status=status,
            error_code=error_code,
            warnings=warnings,
        )

        run_status.additional_properties = d
        return run_status

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
