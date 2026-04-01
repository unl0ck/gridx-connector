from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_address import CustomerAddress


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """Represents an end-customer user.

    Attributes:
        delivery_address (CustomerAddress | Unset): Represents a physical address of a customer.
        customer_id (str | Unset): Uniquely identifies the customer.
        meter_id (str | Unset):
        wizard_completed (bool | Unset): True if the wizard has been completed.
        last_request_at (datetime.datetime | Unset): Specifies when the last request has been made by the customer. This
            field might not be always up-to-date and it might take some time for changes to be propagated.
    """

    delivery_address: CustomerAddress | Unset = UNSET
    customer_id: str | Unset = UNSET
    meter_id: str | Unset = UNSET
    wizard_completed: bool | Unset = UNSET
    last_request_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivery_address, Unset):
            delivery_address = self.delivery_address.to_dict()

        customer_id = self.customer_id

        meter_id = self.meter_id

        wizard_completed = self.wizard_completed

        last_request_at: str | Unset = UNSET
        if not isinstance(self.last_request_at, Unset):
            last_request_at = self.last_request_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if customer_id is not UNSET:
            field_dict["customerID"] = customer_id
        if meter_id is not UNSET:
            field_dict["meterID"] = meter_id
        if wizard_completed is not UNSET:
            field_dict["wizardCompleted"] = wizard_completed
        if last_request_at is not UNSET:
            field_dict["lastRequestAt"] = last_request_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_address import CustomerAddress

        d = dict(src_dict)
        _delivery_address = d.pop("deliveryAddress", UNSET)
        delivery_address: CustomerAddress | Unset
        if isinstance(_delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = CustomerAddress.from_dict(_delivery_address)

        customer_id = d.pop("customerID", UNSET)

        meter_id = d.pop("meterID", UNSET)

        wizard_completed = d.pop("wizardCompleted", UNSET)

        _last_request_at = d.pop("lastRequestAt", UNSET)
        last_request_at: datetime.datetime | Unset
        if isinstance(_last_request_at, Unset):
            last_request_at = UNSET
        else:
            last_request_at = isoparse(_last_request_at)

        customer = cls(
            delivery_address=delivery_address,
            customer_id=customer_id,
            meter_id=meter_id,
            wizard_completed=wizard_completed,
            last_request_at=last_request_at,
        )

        customer.additional_properties = d
        return customer

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
