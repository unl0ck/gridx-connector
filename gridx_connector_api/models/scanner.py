from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scanner_name import ScannerName

T = TypeVar("T", bound="Scanner")


@_attrs_define
class Scanner:
    """Represents a scanner within a scan.

    Attributes:
        id (UUID): Unique identifier of a scanner. Example: 7992f38a-df67-49d9-9f2f-98c63015a20c.
        name (ScannerName): The name of the scanner which searches for the appliance in the network. Example:
            SMA_INVERTER_IGMP_HOST_DISCOVERY.
        started_at (datetime.datetime): The time at which the scan has started. Example: 2018-04-15T00:00:00Z.
        finished_at (datetime.datetime | None): The time at which the scan has finished. Example: 2018-04-15T00:00:00Z.
    """

    id: UUID
    name: ScannerName
    started_at: datetime.datetime
    finished_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name.value

        started_at = self.started_at.isoformat()

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "startedAt": started_at,
                "finishedAt": finished_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = ScannerName(d.pop("name"))

        started_at = isoparse(d.pop("startedAt"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finishedAt"))

        scanner = cls(
            id=id,
            name=name,
            started_at=started_at,
            finished_at=finished_at,
        )

        scanner.additional_properties = d
        return scanner

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
