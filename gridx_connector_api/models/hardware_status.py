from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.hardware_status_action import HardwareStatusAction
from ..models.hardware_status_description import HardwareStatusDescription
from ..models.hardware_status_state import HardwareStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwareStatus")


@_attrs_define
class HardwareStatus:
    """HardwareStatus provides information about the condition of the inverter and in case of issues,
    possible follow-up actions the user/installer can perform to resolve them.

        Attributes:
            state (HardwareStatusState | Unset): State of the inverter.
            action (HardwareStatusAction | Unset): Recommended action to resolve ERROR/WARNING state.
            error_code (str | Unset): Inverter manufacturer/model dependent error code formatted as it would be shown on
                display.
            description (HardwareStatusDescription | Unset): Contains details about the inverter ERROR and WARNING states.
            measured_at (datetime.datetime | Unset):  Example: 2018-04-15T00:00:00Z.
    """

    state: HardwareStatusState | Unset = UNSET
    action: HardwareStatusAction | Unset = UNSET
    error_code: str | Unset = UNSET
    description: HardwareStatusDescription | Unset = UNSET
    measured_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        error_code = self.error_code

        description: str | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.value

        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if action is not UNSET:
            field_dict["action"] = action
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if description is not UNSET:
            field_dict["description"] = description
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: HardwareStatusState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = HardwareStatusState(_state)

        _action = d.pop("action", UNSET)
        action: HardwareStatusAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = HardwareStatusAction(_action)

        error_code = d.pop("errorCode", UNSET)

        _description = d.pop("description", UNSET)
        description: HardwareStatusDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = HardwareStatusDescription(_description)

        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        hardware_status = cls(
            state=state,
            action=action,
            error_code=error_code,
            description=description,
            measured_at=measured_at,
        )

        hardware_status.additional_properties = d
        return hardware_status

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
