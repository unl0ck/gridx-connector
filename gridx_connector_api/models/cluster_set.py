from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_set_priorities_item import ClusterSetPrioritiesItem
from ..models.cluster_set_strategy import ClusterSetStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSet")


@_attrs_define
class ClusterSet:
    """
    Attributes:
        system_id (UUID): Identifier of the system.
        priority (int | Unset): The higher the priority, the more energy the appliances will get; a cluster with higher
            priority will be curtailed least. Example: 1.
        name (str | Unset): The cluster's name meant to be displayable to the user. Example: E Corp HQ.
        strategy (ClusterSetStrategy | Unset): Identifies the specific curtailment approach within the cluster.
        priorities (list[ClusterSetPrioritiesItem] | Unset): Defines the priority for the EMS.
        max_power (int | Unset): The maximum power in W.
        max_power_l1 (int | Unset): The maximum power in W for phase L1.
        max_power_l2 (int | Unset): The maximum power in W for phase L2.
        max_power_l3 (int | Unset): The maximum power in W for phase L3.
        max_power_margin (int | Unset): The maximum power safety margin in W.
        max_power_margin_l1 (int | Unset): The maximum power safety margin in W for phase L1.
        max_power_margin_l2 (int | Unset): The maximum power safety margin in W for phase L2.
        max_power_margin_l3 (int | Unset): The maximum power safety margin in W for phase L3.
        max_power_worst_case (int | Unset): The assumed maximum power in W in case of a lost connection.
        max_power_worst_case_l1 (int | Unset): The assumed maximum power in W in case of a lost connection for phase L1.
        max_power_worst_case_l2 (int | Unset): The assumed maximum power in W in case of a lost connection for phase L2.
        max_power_worst_case_l3 (int | Unset): The assumed maximum power in W in case of a lost connection for phase L3.
        dynamic_power_distribution (bool | Unset): Specifies whether dynamic power distribution should be enabled or
            not.
    """

    system_id: UUID
    priority: int | Unset = UNSET
    name: str | Unset = UNSET
    strategy: ClusterSetStrategy | Unset = UNSET
    priorities: list[ClusterSetPrioritiesItem] | Unset = UNSET
    max_power: int | Unset = UNSET
    max_power_l1: int | Unset = UNSET
    max_power_l2: int | Unset = UNSET
    max_power_l3: int | Unset = UNSET
    max_power_margin: int | Unset = UNSET
    max_power_margin_l1: int | Unset = UNSET
    max_power_margin_l2: int | Unset = UNSET
    max_power_margin_l3: int | Unset = UNSET
    max_power_worst_case: int | Unset = UNSET
    max_power_worst_case_l1: int | Unset = UNSET
    max_power_worst_case_l2: int | Unset = UNSET
    max_power_worst_case_l3: int | Unset = UNSET
    dynamic_power_distribution: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_id = str(self.system_id)

        priority = self.priority

        name = self.name

        strategy: str | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        priorities: list[str] | Unset = UNSET
        if not isinstance(self.priorities, Unset):
            priorities = []
            for priorities_item_data in self.priorities:
                priorities_item = priorities_item_data.value
                priorities.append(priorities_item)

        max_power = self.max_power

        max_power_l1 = self.max_power_l1

        max_power_l2 = self.max_power_l2

        max_power_l3 = self.max_power_l3

        max_power_margin = self.max_power_margin

        max_power_margin_l1 = self.max_power_margin_l1

        max_power_margin_l2 = self.max_power_margin_l2

        max_power_margin_l3 = self.max_power_margin_l3

        max_power_worst_case = self.max_power_worst_case

        max_power_worst_case_l1 = self.max_power_worst_case_l1

        max_power_worst_case_l2 = self.max_power_worst_case_l2

        max_power_worst_case_l3 = self.max_power_worst_case_l3

        dynamic_power_distribution = self.dynamic_power_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "systemID": system_id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if name is not UNSET:
            field_dict["name"] = name
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if priorities is not UNSET:
            field_dict["priorities"] = priorities
        if max_power is not UNSET:
            field_dict["maxPower"] = max_power
        if max_power_l1 is not UNSET:
            field_dict["maxPowerL1"] = max_power_l1
        if max_power_l2 is not UNSET:
            field_dict["maxPowerL2"] = max_power_l2
        if max_power_l3 is not UNSET:
            field_dict["maxPowerL3"] = max_power_l3
        if max_power_margin is not UNSET:
            field_dict["maxPowerMargin"] = max_power_margin
        if max_power_margin_l1 is not UNSET:
            field_dict["maxPowerMarginL1"] = max_power_margin_l1
        if max_power_margin_l2 is not UNSET:
            field_dict["maxPowerMarginL2"] = max_power_margin_l2
        if max_power_margin_l3 is not UNSET:
            field_dict["maxPowerMarginL3"] = max_power_margin_l3
        if max_power_worst_case is not UNSET:
            field_dict["maxPowerWorstCase"] = max_power_worst_case
        if max_power_worst_case_l1 is not UNSET:
            field_dict["maxPowerWorstCaseL1"] = max_power_worst_case_l1
        if max_power_worst_case_l2 is not UNSET:
            field_dict["maxPowerWorstCaseL2"] = max_power_worst_case_l2
        if max_power_worst_case_l3 is not UNSET:
            field_dict["maxPowerWorstCaseL3"] = max_power_worst_case_l3
        if dynamic_power_distribution is not UNSET:
            field_dict["dynamicPowerDistribution"] = dynamic_power_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_id = UUID(d.pop("systemID"))

        priority = d.pop("priority", UNSET)

        name = d.pop("name", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: ClusterSetStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = ClusterSetStrategy(_strategy)

        _priorities = d.pop("priorities", UNSET)
        priorities: list[ClusterSetPrioritiesItem] | Unset = UNSET
        if _priorities is not UNSET:
            priorities = []
            for priorities_item_data in _priorities:
                priorities_item = ClusterSetPrioritiesItem(priorities_item_data)

                priorities.append(priorities_item)

        max_power = d.pop("maxPower", UNSET)

        max_power_l1 = d.pop("maxPowerL1", UNSET)

        max_power_l2 = d.pop("maxPowerL2", UNSET)

        max_power_l3 = d.pop("maxPowerL3", UNSET)

        max_power_margin = d.pop("maxPowerMargin", UNSET)

        max_power_margin_l1 = d.pop("maxPowerMarginL1", UNSET)

        max_power_margin_l2 = d.pop("maxPowerMarginL2", UNSET)

        max_power_margin_l3 = d.pop("maxPowerMarginL3", UNSET)

        max_power_worst_case = d.pop("maxPowerWorstCase", UNSET)

        max_power_worst_case_l1 = d.pop("maxPowerWorstCaseL1", UNSET)

        max_power_worst_case_l2 = d.pop("maxPowerWorstCaseL2", UNSET)

        max_power_worst_case_l3 = d.pop("maxPowerWorstCaseL3", UNSET)

        dynamic_power_distribution = d.pop("dynamicPowerDistribution", UNSET)

        cluster_set = cls(
            system_id=system_id,
            priority=priority,
            name=name,
            strategy=strategy,
            priorities=priorities,
            max_power=max_power,
            max_power_l1=max_power_l1,
            max_power_l2=max_power_l2,
            max_power_l3=max_power_l3,
            max_power_margin=max_power_margin,
            max_power_margin_l1=max_power_margin_l1,
            max_power_margin_l2=max_power_margin_l2,
            max_power_margin_l3=max_power_margin_l3,
            max_power_worst_case=max_power_worst_case,
            max_power_worst_case_l1=max_power_worst_case_l1,
            max_power_worst_case_l2=max_power_worst_case_l2,
            max_power_worst_case_l3=max_power_worst_case_l3,
            dynamic_power_distribution=dynamic_power_distribution,
        )

        cluster_set.additional_properties = d
        return cluster_set

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
