from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.devices_additional_property_item import DevicesAdditionalPropertyItem


T = TypeVar("T", bound="Devices")


@_attrs_define
class Devices:
    """
    Example:
        {'homeconnect': [{'id': '27jslrNMHpUx266', 'url': 'homeconnect-device-url', 'parentURL': 'string',
            'deviceAddress': 'd:_n:NaTeYtMjnNGtQqQvbuJT4AoSY-LBq_;:7Jbs,L"Qz.hQg', 'type': 'washer', 'label': 'My New
            Dishwasher', 'bindings': [{'bindingId': 'jaxbv2', 'type': 'powerSequence', 'url':
            'https://api.eebus.org/devices/1041A421/bindings/jaxbv2', 'name': 'bindingName', 'validity':
            '2021-07-24T23:59:59Z'}], 'usecases': [{'name': 'fswg', 'actor': 'server'}], 'resources': [{'url':
            'https://api.eebus.org/devices/1041A421/powerSequences', 'type': 'powerSequence', 'specialization':
            'flexibleStart', 'supportsBinding': True, 'data': [{'sequenceId': 1, 'state': 'scheduled', 'activeSlotNumber':
            0, 'sequenceRemoteControllable': True, 'startTime': '2021-06-24T12:00:00Z', 'endTime': '2021-06-24T13:40:00Z',
            'earliestStartTime': '2021-06-24T06:20:00Z', 'latestEndTime': '2021-06-24T19:00:00Z', 'isPausable': False,
            'isStoppable': False, 'valueSource': 'empiricalValue', 'taskIdentifier': 0, 'powerTimeSlots': [{'slotId': 1,
            'defaultDuration': '00:23:00', 'powerMin': 100, 'powerExpectedValue': 200, 'powerMax': 1000}]}]}]}]}

    """

    additional_properties: dict[str, list[DevicesAdditionalPropertyItem]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.devices_additional_property_item import DevicesAdditionalPropertyItem

        d = dict(src_dict)
        devices = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = DevicesAdditionalPropertyItem.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        devices.additional_properties = additional_properties
        return devices

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[DevicesAdditionalPropertyItem]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[DevicesAdditionalPropertyItem]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
