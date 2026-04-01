from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.container_source_origin import ContainerSourceOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerSource")


@_attrs_define
class ContainerSource:
    """
    Attributes:
        origin (ContainerSourceOrigin): Specifies who created the appliance. This can be one of:
            - `GRIDBOX` if the appliance was found during a scan using a gridBox.
            - `API` if a user of the gridX API used the 'Create Appliance' endpoint
              to create this appliance.
            - `UNKNOWN` otherwise.
             Example: API.
        uri (str | Unset): Contains an URI identifying the exact resource that created this appliance.

            If origin is 'GRID_BOX' the value will point to the gateway object of the gridBox. If
            origin is 'API' the value will specify the user that made the request to the gridX API.
            The 'UNKNOWN' origin should not occur in practice and is reserved for special cases (for now).
             Example: accounts/b30510fa-a8a5-475f-a75d-82a46cb62582/users/b30510fa-a8a5-475f-a75d-82a46cb62582.
    """

    origin: ContainerSourceOrigin
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin = self.origin.value

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
            }
        )
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin = ContainerSourceOrigin(d.pop("origin"))

        uri = d.pop("uri", UNSET)

        container_source = cls(
            origin=origin,
            uri=uri,
        )

        container_source.additional_properties = d
        return container_source

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
