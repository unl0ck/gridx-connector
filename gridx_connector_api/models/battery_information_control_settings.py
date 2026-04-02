from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.battery_information_control_settings_command import BatteryInformationControlSettingsCommand

T = TypeVar("T", bound="BatteryInformationControlSettings")


@_attrs_define
class BatteryInformationControlSettings:
    """Indicates the currently desired control settings for the battery.

    Attributes:
        value (int): Represents the charge/discharge power in mW.
        command (BatteryInformationControlSettingsCommand): Represents the current control command.
    """

    value: int
    command: BatteryInformationControlSettingsCommand
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        command = self.command.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "command": command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        command = BatteryInformationControlSettingsCommand(d.pop("command"))

        battery_information_control_settings = cls(
            value=value,
            command=command,
        )

        battery_information_control_settings.additional_properties = d
        return battery_information_control_settings

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
