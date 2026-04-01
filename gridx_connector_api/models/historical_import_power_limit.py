from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.historical_import_power_limit_import_power_limits_stored_with_the_dynamic_api import (
        HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI,
    )


T = TypeVar("T", bound="HistoricalImportPowerLimit")


@_attrs_define
class HistoricalImportPowerLimit:
    """
    Attributes:
        system_id (UUID): Unique ID to identify the system the import power limits belong to. Example:
            512654ea-5328-4c79-8ed7-b4136aa31679.
        data (list[HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI]):
    """

    system_id: UUID
    data: list[HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_id = str(self.system_id)

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "systemID": system_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.historical_import_power_limit_import_power_limits_stored_with_the_dynamic_api import (
            HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI,
        )

        d = dict(src_dict)
        system_id = UUID(d.pop("systemID"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = HistoricalImportPowerLimitImportPowerLimitsStoredWithTheDynamicAPI.from_dict(data_item_data)

            data.append(data_item)

        historical_import_power_limit = cls(
            system_id=system_id,
            data=data,
        )

        historical_import_power_limit.additional_properties = d
        return historical_import_power_limit

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
