from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BiddingZoneSet")


@_attrs_define
class BiddingZoneSet:
    """
    Attributes:
        bidding_zone (str):  Example: 10Y1001A1001A44P.
    """

    bidding_zone: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bidding_zone = self.bidding_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "biddingZone": bidding_zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bidding_zone = d.pop("biddingZone")

        bidding_zone_set = cls(
            bidding_zone=bidding_zone,
        )

        bidding_zone_set.additional_properties = d
        return bidding_zone_set

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
