from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.heater_state_appliance_state import HeaterStateApplianceState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heater_state_state_transition import HeaterStateStateTransition


T = TypeVar("T", bound="HeaterState")


@_attrs_define
class HeaterState:
    """Contains information about the appliance's state.

    Attributes:
        current (HeaterStateApplianceState): The state the appliance is currently in. Example: SCANNED.
        desired (HeaterStateApplianceState): State an appliance can be in.
        transitions (list[HeaterStateStateTransition] | Unset): List with all the possible state transitions an
            appliance can go through.
            An appliance can go from a `starting` state to a `target` state.
    """

    current: HeaterStateApplianceState
    desired: HeaterStateApplianceState
    transitions: list[HeaterStateStateTransition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current.value

        desired = self.desired.value

        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "desired": desired,
            }
        )
        if transitions is not UNSET:
            field_dict["transitions"] = transitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heater_state_state_transition import HeaterStateStateTransition

        d = dict(src_dict)
        current = HeaterStateApplianceState(d.pop("current"))

        desired = HeaterStateApplianceState(d.pop("desired"))

        _transitions = d.pop("transitions", UNSET)
        transitions: list[HeaterStateStateTransition] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = HeaterStateStateTransition.from_dict(transitions_item_data)

                transitions.append(transitions_item)

        heater_state = cls(
            current=current,
            desired=desired,
            transitions=transitions,
        )

        heater_state.additional_properties = d
        return heater_state

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
