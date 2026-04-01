from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meter_commissioning_kind import MeterCommissioningKind
from ..models.meter_kind import MeterKind
from ..models.meter_protocol import MeterProtocol
from ..models.meter_status import MeterStatus
from ..models.meter_type import MeterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meter_appliance_connection_status import MeterApplianceConnectionStatus
    from ..models.meter_aux_meter import MeterAuxMeter
    from ..models.meter_crypto_settings_item import MeterCryptoSettingsItem
    from ..models.meter_energy_management_settings import MeterEnergyManagementSettings
    from ..models.meter_load_settings import MeterLoadSettings
    from ..models.meter_network import MeterNetwork
    from ..models.meter_sensor_settings import MeterSensorSettings
    from ..models.meter_source import MeterSource
    from ..models.meter_state import MeterState


T = TypeVar("T", bound="Meter")


@_attrs_define
class Meter:
    """Meter represents a monitor-/controllable meter.

    Attributes:
        id (UUID): Uniquely identifies the appliance. Example: ec4d0c89-a604-49ac-82f0-427f9cb42204.
        created_at (datetime.datetime): Specifies when the appliance was created.
        updated_at (datetime.datetime): Specifies when the appliance was updated the last time.
        connection_status (MeterApplianceConnectionStatus):
        type_ (MeterType): Describes the 'physical' type of the appliance.

            See `kind` for further distinction of the type in terms of the appliance's purpose/role,
            e.g. appliance with type=INVERTER and kind=BATTERY represents a battery inverter.
             Example: INVERTER.
        inactive (bool):
        reverse_flow (bool): If true, changes the energy flow's direction.

            If during installation the input/output wiring is mixed up, set it to true in order to compensate for that.
            This impact the consumption/production calculation as follows:
            It switches the algebraic sign of the appliance's measurements, e.g. if an appliance measurement showed supply
            (+), it will change to feed-in (-) after this field is set to true (and vice versa).
        state (MeterState): Contains information about the appliance's state.
        aux_meter (MeterAuxMeter): The meter specific information.
        kind (MeterKind): Indicates what the meter measures.
            Setting the kind impacts the system measurements. So it's best to set it up correctly as early as possible in
            accordance to the actual installation in order for the measurement calculation to be correct (best during
            commissioning).
        status (MeterStatus | Unset): Status of the appliance. This field is set dynamically in the appliance handler.

            **Deprecated** - Use `ConnectionStatus` instead.
        name (str | Unset): Name of the appliance.
        room (str | Unset): The physical room/location of the appliance in the building.
        serialnumber (str | Unset): Serialnumber of the appliance. Example: 1901000652.
        network (MeterNetwork | Unset): Represents a network connection.
        parent (UUID | Unset): Specifies the parent appliance ID, for an appliance which is a child of a `CONTAINER` or
            `INVERTER` of kind `HYBRID`.
        load_settings (MeterLoadSettings | Unset): Configure load of appliance.
        sensor_settings (MeterSensorSettings | Unset):
        source (MeterSource | Unset):
        commissioning_kind (MeterCommissioningKind | Unset): Indicates special requirements to be fulfilled during the
            commissioning for this appliance.

            If empty or unset (default), the appliance can be commissioned as regular.
            - `property:CryptoSettings` means that the appliance property `CryptoSettings` needs to be set, e.g. for
            authenticating towards it with an appliance-specific API token.
            - `flow:Pairing` means that a coupling or pairing flow has to be initiated and run-through in order for the
            appliance to behave correctly.
        energy_settings (MeterEnergyManagementSettings | Unset): Contains energy management information
        crypto_settings (list[MeterCryptoSettingsItem] | Unset): Contains a list of crypto setting keys that are
            associated with the appliance.
        protocol (MeterProtocol | Unset): Network protocol supported by the appliance Example: EEBUS.
        model (str | Unset): Model of the meter. Example: B-control Energy Manager 300.
        firmware (str | Unset): Firmware version of the meter. Example: 2.03.
        manufacturer (str | Unset): Manufacturer of the meter. Example: TQ Systems.
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    connection_status: MeterApplianceConnectionStatus
    type_: MeterType
    inactive: bool
    reverse_flow: bool
    state: MeterState
    aux_meter: MeterAuxMeter
    kind: MeterKind
    status: MeterStatus | Unset = UNSET
    name: str | Unset = UNSET
    room: str | Unset = UNSET
    serialnumber: str | Unset = UNSET
    network: MeterNetwork | Unset = UNSET
    parent: UUID | Unset = UNSET
    load_settings: MeterLoadSettings | Unset = UNSET
    sensor_settings: MeterSensorSettings | Unset = UNSET
    source: MeterSource | Unset = UNSET
    commissioning_kind: MeterCommissioningKind | Unset = UNSET
    energy_settings: MeterEnergyManagementSettings | Unset = UNSET
    crypto_settings: list[MeterCryptoSettingsItem] | Unset = UNSET
    protocol: MeterProtocol | Unset = UNSET
    model: str | Unset = UNSET
    firmware: str | Unset = UNSET
    manufacturer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        connection_status = self.connection_status.to_dict()

        type_ = self.type_.value

        inactive = self.inactive

        reverse_flow = self.reverse_flow

        state = self.state.to_dict()

        aux_meter = self.aux_meter.to_dict()

        kind = self.kind.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name

        room = self.room

        serialnumber = self.serialnumber

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        parent: str | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = str(self.parent)

        load_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.load_settings, Unset):
            load_settings = self.load_settings.to_dict()

        sensor_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sensor_settings, Unset):
            sensor_settings = self.sensor_settings.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        commissioning_kind: str | Unset = UNSET
        if not isinstance(self.commissioning_kind, Unset):
            commissioning_kind = self.commissioning_kind.value

        energy_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy_settings, Unset):
            energy_settings = self.energy_settings.to_dict()

        crypto_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.crypto_settings, Unset):
            crypto_settings = []
            for crypto_settings_item_data in self.crypto_settings:
                crypto_settings_item = crypto_settings_item_data.to_dict()
                crypto_settings.append(crypto_settings_item)

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        model = self.model

        firmware = self.firmware

        manufacturer = self.manufacturer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "connectionStatus": connection_status,
                "type": type_,
                "inactive": inactive,
                "reverseFlow": reverse_flow,
                "state": state,
                "auxMeter": aux_meter,
                "kind": kind,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if room is not UNSET:
            field_dict["room"] = room
        if serialnumber is not UNSET:
            field_dict["serialnumber"] = serialnumber
        if network is not UNSET:
            field_dict["network"] = network
        if parent is not UNSET:
            field_dict["parent"] = parent
        if load_settings is not UNSET:
            field_dict["loadSettings"] = load_settings
        if sensor_settings is not UNSET:
            field_dict["sensorSettings"] = sensor_settings
        if source is not UNSET:
            field_dict["source"] = source
        if commissioning_kind is not UNSET:
            field_dict["commissioningKind"] = commissioning_kind
        if energy_settings is not UNSET:
            field_dict["energySettings"] = energy_settings
        if crypto_settings is not UNSET:
            field_dict["cryptoSettings"] = crypto_settings
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if model is not UNSET:
            field_dict["model"] = model
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_appliance_connection_status import MeterApplianceConnectionStatus
        from ..models.meter_aux_meter import MeterAuxMeter
        from ..models.meter_crypto_settings_item import MeterCryptoSettingsItem
        from ..models.meter_energy_management_settings import MeterEnergyManagementSettings
        from ..models.meter_load_settings import MeterLoadSettings
        from ..models.meter_network import MeterNetwork
        from ..models.meter_sensor_settings import MeterSensorSettings
        from ..models.meter_source import MeterSource
        from ..models.meter_state import MeterState

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        connection_status = MeterApplianceConnectionStatus.from_dict(d.pop("connectionStatus"))

        type_ = MeterType(d.pop("type"))

        inactive = d.pop("inactive")

        reverse_flow = d.pop("reverseFlow")

        state = MeterState.from_dict(d.pop("state"))

        aux_meter = MeterAuxMeter.from_dict(d.pop("auxMeter"))

        kind = MeterKind(d.pop("kind"))

        _status = d.pop("status", UNSET)
        status: MeterStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MeterStatus(_status)

        name = d.pop("name", UNSET)

        room = d.pop("room", UNSET)

        serialnumber = d.pop("serialnumber", UNSET)

        _network = d.pop("network", UNSET)
        network: MeterNetwork | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = MeterNetwork.from_dict(_network)

        _parent = d.pop("parent", UNSET)
        parent: UUID | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = UUID(_parent)

        _load_settings = d.pop("loadSettings", UNSET)
        load_settings: MeterLoadSettings | Unset
        if isinstance(_load_settings, Unset):
            load_settings = UNSET
        else:
            load_settings = MeterLoadSettings.from_dict(_load_settings)

        _sensor_settings = d.pop("sensorSettings", UNSET)
        sensor_settings: MeterSensorSettings | Unset
        if isinstance(_sensor_settings, Unset):
            sensor_settings = UNSET
        else:
            sensor_settings = MeterSensorSettings.from_dict(_sensor_settings)

        _source = d.pop("source", UNSET)
        source: MeterSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = MeterSource.from_dict(_source)

        _commissioning_kind = d.pop("commissioningKind", UNSET)
        commissioning_kind: MeterCommissioningKind | Unset
        if isinstance(_commissioning_kind, Unset):
            commissioning_kind = UNSET
        else:
            commissioning_kind = MeterCommissioningKind(_commissioning_kind)

        _energy_settings = d.pop("energySettings", UNSET)
        energy_settings: MeterEnergyManagementSettings | Unset
        if isinstance(_energy_settings, Unset):
            energy_settings = UNSET
        else:
            energy_settings = MeterEnergyManagementSettings.from_dict(_energy_settings)

        _crypto_settings = d.pop("cryptoSettings", UNSET)
        crypto_settings: list[MeterCryptoSettingsItem] | Unset = UNSET
        if _crypto_settings is not UNSET:
            crypto_settings = []
            for crypto_settings_item_data in _crypto_settings:
                crypto_settings_item = MeterCryptoSettingsItem.from_dict(crypto_settings_item_data)

                crypto_settings.append(crypto_settings_item)

        _protocol = d.pop("protocol", UNSET)
        protocol: MeterProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = MeterProtocol(_protocol)

        model = d.pop("model", UNSET)

        firmware = d.pop("firmware", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        meter = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            connection_status=connection_status,
            type_=type_,
            inactive=inactive,
            reverse_flow=reverse_flow,
            state=state,
            aux_meter=aux_meter,
            kind=kind,
            status=status,
            name=name,
            room=room,
            serialnumber=serialnumber,
            network=network,
            parent=parent,
            load_settings=load_settings,
            sensor_settings=sensor_settings,
            source=source,
            commissioning_kind=commissioning_kind,
            energy_settings=energy_settings,
            crypto_settings=crypto_settings,
            protocol=protocol,
            model=model,
            firmware=firmware,
            manufacturer=manufacturer,
        )

        meter.additional_properties = d
        return meter

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
