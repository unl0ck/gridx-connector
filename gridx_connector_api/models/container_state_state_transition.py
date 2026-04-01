from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.container_state_state_transition_appliance_state import ContainerStateStateTransitionApplianceState

T = TypeVar("T", bound="ContainerStateStateTransition")


@_attrs_define
class ContainerStateStateTransition:
    """Defines the properties of a transition an appliance can go through.

    Attributes:
        start (ContainerStateStateTransitionApplianceState): The starting state of the appliance. Example: CONNECTING.
        target (ContainerStateStateTransitionApplianceState): The target state of the appliance. Example: DISCONNECTED.
    """

    start: ContainerStateStateTransitionApplianceState
    target: ContainerStateStateTransitionApplianceState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.value

        target = self.target.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = ContainerStateStateTransitionApplianceState(d.pop("start"))

        target = ContainerStateStateTransitionApplianceState(d.pop("target"))

        container_state_state_transition = cls(
            start=start,
            target=target,
        )

        container_state_state_transition.additional_properties = d
        return container_state_state_transition

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
