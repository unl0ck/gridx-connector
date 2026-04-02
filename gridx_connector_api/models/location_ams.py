from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationAMS")


@_attrs_define
class LocationAMS:
    """The Location where the System is located at. The first time it is created and on any subsequent updates, the
    coordinates are looked up and persisted, so that on subsequent retrievals, those fields should be present.
    However, a System is considered valid even without a location, so failure to retrieve the coordinates won't
    result in an error when creating or updating a system.

        Attributes:
            address_line_1 (str | Unset):  Example: TheresienhÃ¶he 12.
            address_line_2 (str | Unset):  Example: Aufgang 8.
            city (str | Unset):  Example: Munich.
            zipcode (str | Unset):  Example: 80339.
            country (str | Unset):  Example: Germany.
            latitude (float | Unset):
            longitude (float | Unset):
    """

    address_line_1: str | Unset = UNSET
    address_line_2: str | Unset = UNSET
    city: str | Unset = UNSET
    zipcode: str | Unset = UNSET
    country: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        city = self.city

        zipcode = self.zipcode

        country = self.country

        latitude = self.latitude

        longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if city is not UNSET:
            field_dict["city"] = city
        if zipcode is not UNSET:
            field_dict["zipcode"] = zipcode
        if country is not UNSET:
            field_dict["country"] = country
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        city = d.pop("city", UNSET)

        zipcode = d.pop("zipcode", UNSET)

        country = d.pop("country", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        location_ams = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            zipcode=zipcode,
            country=country,
            latitude=latitude,
            longitude=longitude,
        )

        location_ams.additional_properties = d
        return location_ams

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
