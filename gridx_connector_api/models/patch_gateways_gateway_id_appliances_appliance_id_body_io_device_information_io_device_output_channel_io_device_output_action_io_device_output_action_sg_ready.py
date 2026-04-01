from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_gateways_gateway_id_appliances_appliance_id_body_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready_state import (
    PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReadyState,
)

T = TypeVar(
    "T",
    bound="PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady",
)


@_attrs_define
class PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReady:
    """Used to specify a connection to a heat pump supporting the SGReady standard.

    Attributes:
        p_min (float):
        p_max (float):
        state (PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActi
            onIODeviceOutputActionSGReadyState): Represents one state of the sg ready standard.
        appliance_id (UUID):
    """

    p_min: float
    p_max: float
    state: PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReadyState
    appliance_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        p_min = self.p_min

        p_max = self.p_max

        state = self.state.value

        appliance_id = str(self.appliance_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pMin": p_min,
                "pMax": p_max,
                "state": state,
                "applianceID": appliance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        p_min = d.pop("pMin")

        p_max = d.pop("pMax")

        state = PatchGatewaysGatewayIDAppliancesApplianceIDBodyIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReadyState(
            d.pop("state")
        )

        appliance_id = UUID(d.pop("applianceID"))

        patch_gateways_gateway_id_appliances_appliance_id_body_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready = cls(
            p_min=p_min,
            p_max=p_max,
            state=state,
            appliance_id=appliance_id,
        )

        patch_gateways_gateway_id_appliances_appliance_id_body_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready.additional_properties = d
        return patch_gateways_gateway_id_appliances_appliance_id_body_io_device_information_io_device_output_channel_io_device_output_action_io_device_output_action_sg_ready

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
