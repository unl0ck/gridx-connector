from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemCreate")


@_attrs_define
class SystemCreate:
    """
    Attributes:
        priorities (Any | Unset):
        curtailment_strategy (Any | Unset):
    """

    priorities: Any | Unset = UNSET
    curtailment_strategy: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priorities = self.priorities

        curtailment_strategy = self.curtailment_strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priorities is not UNSET:
            field_dict["priorities"] = priorities
        if curtailment_strategy is not UNSET:
            field_dict["curtailmentStrategy"] = curtailment_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        priorities = d.pop("priorities", UNSET)

        curtailment_strategy = d.pop("curtailmentStrategy", UNSET)

        system_create = cls(
            priorities=priorities,
            curtailment_strategy=curtailment_strategy,
        )

        system_create.additional_properties = d
        return system_create

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
