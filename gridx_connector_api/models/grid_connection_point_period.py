from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GridConnectionPointPeriod")


@_attrs_define
class GridConnectionPointPeriod:
    """
    Attributes:
        from_ (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the beginning of the period.
             Example: 2020-09-21T00:00:00Z.
        to (datetime.datetime | Unset): Timestamp in RFC3339 format that marks the end of the period.
             Example: 2020-09-21T00:15:00Z.
        import_active_power (float | Unset): The forecasted import active power in Watts.
        export_active_power (float | Unset): The forecasted export active power in Watts.
    """

    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    import_active_power: float | Unset = UNSET
    export_active_power: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        import_active_power = self.import_active_power

        export_active_power = self.export_active_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if import_active_power is not UNSET:
            field_dict["importActivePower"] = import_active_power
        if export_active_power is not UNSET:
            field_dict["exportActivePower"] = export_active_power

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        import_active_power = d.pop("importActivePower", UNSET)

        export_active_power = d.pop("exportActivePower", UNSET)

        grid_connection_point_period = cls(
            from_=from_,
            to=to,
            import_active_power=import_active_power,
            export_active_power=export_active_power,
        )

        grid_connection_point_period.additional_properties = d
        return grid_connection_point_period

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
