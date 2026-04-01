from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_usecases_item_actor import DeviceUsecasesItemActor
from ..models.device_usecases_item_name import DeviceUsecasesItemName

T = TypeVar("T", bound="DeviceUsecasesItem")


@_attrs_define
class DeviceUsecasesItem:
    """
    Attributes:
        name (DeviceUsecasesItemName): Semantic short name of the use-case. Example: fswg.
        actor (DeviceUsecasesItemActor): The actor's role in the current scenario. Example: server.
    """

    name: DeviceUsecasesItemName
    actor: DeviceUsecasesItemActor
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        actor = self.actor.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "actor": actor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = DeviceUsecasesItemName(d.pop("name"))

        actor = DeviceUsecasesItemActor(d.pop("actor"))

        device_usecases_item = cls(
            name=name,
            actor=actor,
        )

        device_usecases_item.additional_properties = d
        return device_usecases_item

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
