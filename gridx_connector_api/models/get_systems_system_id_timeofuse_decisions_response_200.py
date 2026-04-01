from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_systems_system_id_timeofuse_decisions_response_200_decisions_item import (
        GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItem,
    )
    from ..models.get_systems_system_id_timeofuse_decisions_response_200_metrics import (
        GetSystemsSystemIDTimeofuseDecisionsResponse200Metrics,
    )


T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseDecisionsResponse200")


@_attrs_define
class GetSystemsSystemIDTimeofuseDecisionsResponse200:
    """
    Attributes:
        decisions (list[GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItem]):
        metrics (GetSystemsSystemIDTimeofuseDecisionsResponse200Metrics):
    """

    decisions: list[GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItem]
    metrics: GetSystemsSystemIDTimeofuseDecisionsResponse200Metrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decisions = []
        for decisions_item_data in self.decisions:
            decisions_item = decisions_item_data.to_dict()
            decisions.append(decisions_item)

        metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decisions": decisions,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_timeofuse_decisions_response_200_decisions_item import (
            GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItem,
        )
        from ..models.get_systems_system_id_timeofuse_decisions_response_200_metrics import (
            GetSystemsSystemIDTimeofuseDecisionsResponse200Metrics,
        )

        d = dict(src_dict)
        decisions = []
        _decisions = d.pop("decisions")
        for decisions_item_data in _decisions:
            decisions_item = GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItem.from_dict(decisions_item_data)

            decisions.append(decisions_item)

        metrics = GetSystemsSystemIDTimeofuseDecisionsResponse200Metrics.from_dict(d.pop("metrics"))

        get_systems_system_id_timeofuse_decisions_response_200 = cls(
            decisions=decisions,
            metrics=metrics,
        )

        get_systems_system_id_timeofuse_decisions_response_200.additional_properties = d
        return get_systems_system_id_timeofuse_decisions_response_200

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
