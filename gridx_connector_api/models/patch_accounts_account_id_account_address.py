from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAccountsAccountIDAccountAddress")


@_attrs_define
class PatchAccountsAccountIDAccountAddress:
    """Represents a physical address of a customer.

    Attributes:
        city (str | Unset): The city of the location. Example: Aachen.
        country (str | Unset): The country of the location. Example: Germany.
        address_line_1 (str | Unset): First line of the location's address, typically containing the
            main information such as the street name and house number.
             Example: Oppenhoffallee 143.
        address_line_2 (str | Unset): Second line of the location's address, typically containing additional
            information such as apartment numbers, suite numbers, or other details
            that can help in identifying the exact location of the address.
        address_line_3 (str | Unset): Third line of the location's address, typically containing any other
            details that can help in identifying the exact location of the address.
        address_line_4 (str | Unset): Fourth line of the location's address, typically containing any other
            details that can help in identifying the exact location of the address.
        time_zone (str | Unset): The TZ Identifier of the location's timezone. Example: Europe/Berlin.
        postalcode (str | Unset): The postal code of the location. Example: 52062.
        region (str | Unset): The region of the address.
        telephone (str | Unset): The telephone number of the customer.
    """

    city: str | Unset = UNSET
    country: str | Unset = UNSET
    address_line_1: str | Unset = UNSET
    address_line_2: str | Unset = UNSET
    address_line_3: str | Unset = UNSET
    address_line_4: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    postalcode: str | Unset = UNSET
    region: str | Unset = UNSET
    telephone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        address_line_3 = self.address_line_3

        address_line_4 = self.address_line_4

        time_zone = self.time_zone

        postalcode = self.postalcode

        region = self.region

        telephone = self.telephone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if address_line_4 is not UNSET:
            field_dict["addressLine4"] = address_line_4
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode
        if region is not UNSET:
            field_dict["region"] = region
        if telephone is not UNSET:
            field_dict["telephone"] = telephone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        address_line_4 = d.pop("addressLine4", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        postalcode = d.pop("postalcode", UNSET)

        region = d.pop("region", UNSET)

        telephone = d.pop("telephone", UNSET)

        patch_accounts_account_id_account_address = cls(
            city=city,
            country=country,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            address_line_4=address_line_4,
            time_zone=time_zone,
            postalcode=postalcode,
            region=region,
            telephone=telephone,
        )

        patch_accounts_account_id_account_address.additional_properties = d
        return patch_accounts_account_id_account_address

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
