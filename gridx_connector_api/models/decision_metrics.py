from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DecisionMetrics")


@_attrs_define
class DecisionMetrics:
    """
    Attributes:
        percent_decision_taken (float): Percentage of the taken decisions as a share of the total possible decisions
            during this time interval. Taken decisions are all decisions excluding "no-decision" cases.
             Example: 75.
    """

    percent_decision_taken: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percent_decision_taken = self.percent_decision_taken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percent_decision_taken": percent_decision_taken,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent_decision_taken = d.pop("percent_decision_taken")

        decision_metrics = cls(
            percent_decision_taken=percent_decision_taken,
        )

        decision_metrics.additional_properties = d
        return decision_metrics

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
