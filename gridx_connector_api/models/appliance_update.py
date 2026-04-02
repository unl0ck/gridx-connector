from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.appliance_update_appliance_state import ApplianceUpdateApplianceState
from ..models.appliance_update_kind import ApplianceUpdateKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appliance_update_crypto_settings_item import ApplianceUpdateCryptoSettingsItem
    from ..models.appliance_update_energy_management_settings import ApplianceUpdateEnergyManagementSettings
    from ..models.appliance_update_ev_load_management_parameters import ApplianceUpdateEvLoadManagementParameters
    from ..models.appliance_update_heat_pump_information import ApplianceUpdateHeatPumpInformation
    from ..models.appliance_update_io_device_information import ApplianceUpdateIODeviceInformation
    from ..models.appliance_update_load_settings import ApplianceUpdateLoadSettings


T = TypeVar("T", bound="ApplianceUpdate")


@_attrs_define
class ApplianceUpdate:
    """ApplianceUpdate contains fields of an appliance that can be updated.

    Attributes:
        inactive (bool | Unset):
        name (str | Unset): Name of the appliance.
        reverse_flow (bool | Unset): If true, changes the energy flow's direction.

            If during installation the input/output wiring is mixed up, set it to true in order to compensate for that.
            This impact the consumption/production calculation as follows:
            It switches the algebraic sign of the appliance's measurements, e.g. if an appliance measurement showed supply
            (+), it will change to feed-in (-) after this field is set to true (and vice versa).
        room (str | Unset): The physical room/location of the appliance in the building.
        load_settings (ApplianceUpdateLoadSettings | Unset): Configure load of appliance.
        kind (ApplianceUpdateKind | Unset): Indicates the specific kind or role of the appliance.
            Only settable for appliances of type `INVERTER` or `METER`.
        energy_settings (ApplianceUpdateEnergyManagementSettings | Unset): Contains energy management information
        crypto_settings (list[ApplianceUpdateCryptoSettingsItem] | Unset): Contains a list of crypto setting keys that
            are associated with the appliance.
        ev_load_management_parameters (ApplianceUpdateEvLoadManagementParameters | Unset): Load management configuration
            for EV charging stations.

            **Deprecated** - Use the system's EV charging station configuration instead.
        evse_id (str | Unset): The EVSE-ID related to the charge point.
        desired_state (ApplianceUpdateApplianceState | Unset): State an appliance can be in.
        heat_pump (ApplianceUpdateHeatPumpInformation | Unset): The heat pump specific information.
        io_device (ApplianceUpdateIODeviceInformation | Unset): The io device specific information.
    """

    inactive: bool | Unset = UNSET
    name: str | Unset = UNSET
    reverse_flow: bool | Unset = UNSET
    room: str | Unset = UNSET
    load_settings: ApplianceUpdateLoadSettings | Unset = UNSET
    kind: ApplianceUpdateKind | Unset = UNSET
    energy_settings: ApplianceUpdateEnergyManagementSettings | Unset = UNSET
    crypto_settings: list[ApplianceUpdateCryptoSettingsItem] | Unset = UNSET
    ev_load_management_parameters: ApplianceUpdateEvLoadManagementParameters | Unset = UNSET
    evse_id: str | Unset = UNSET
    desired_state: ApplianceUpdateApplianceState | Unset = UNSET
    heat_pump: ApplianceUpdateHeatPumpInformation | Unset = UNSET
    io_device: ApplianceUpdateIODeviceInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inactive = self.inactive

        name = self.name

        reverse_flow = self.reverse_flow

        room = self.room

        load_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.load_settings, Unset):
            load_settings = self.load_settings.to_dict()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        energy_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy_settings, Unset):
            energy_settings = self.energy_settings.to_dict()

        crypto_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.crypto_settings, Unset):
            crypto_settings = []
            for crypto_settings_item_data in self.crypto_settings:
                crypto_settings_item = crypto_settings_item_data.to_dict()
                crypto_settings.append(crypto_settings_item)

        ev_load_management_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ev_load_management_parameters, Unset):
            ev_load_management_parameters = self.ev_load_management_parameters.to_dict()

        evse_id = self.evse_id

        desired_state: str | Unset = UNSET
        if not isinstance(self.desired_state, Unset):
            desired_state = self.desired_state.value

        heat_pump: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heat_pump, Unset):
            heat_pump = self.heat_pump.to_dict()

        io_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.io_device, Unset):
            io_device = self.io_device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if name is not UNSET:
            field_dict["name"] = name
        if reverse_flow is not UNSET:
            field_dict["reverseFlow"] = reverse_flow
        if room is not UNSET:
            field_dict["room"] = room
        if load_settings is not UNSET:
            field_dict["loadSettings"] = load_settings
        if kind is not UNSET:
            field_dict["kind"] = kind
        if energy_settings is not UNSET:
            field_dict["energySettings"] = energy_settings
        if crypto_settings is not UNSET:
            field_dict["cryptoSettings"] = crypto_settings
        if ev_load_management_parameters is not UNSET:
            field_dict["evLoadManagementParameters"] = ev_load_management_parameters
        if evse_id is not UNSET:
            field_dict["evseID"] = evse_id
        if desired_state is not UNSET:
            field_dict["desiredState"] = desired_state
        if heat_pump is not UNSET:
            field_dict["heatPump"] = heat_pump
        if io_device is not UNSET:
            field_dict["ioDevice"] = io_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appliance_update_crypto_settings_item import ApplianceUpdateCryptoSettingsItem
        from ..models.appliance_update_energy_management_settings import ApplianceUpdateEnergyManagementSettings
        from ..models.appliance_update_ev_load_management_parameters import ApplianceUpdateEvLoadManagementParameters
        from ..models.appliance_update_heat_pump_information import ApplianceUpdateHeatPumpInformation
        from ..models.appliance_update_io_device_information import ApplianceUpdateIODeviceInformation
        from ..models.appliance_update_load_settings import ApplianceUpdateLoadSettings

        d = dict(src_dict)
        inactive = d.pop("inactive", UNSET)

        name = d.pop("name", UNSET)

        reverse_flow = d.pop("reverseFlow", UNSET)

        room = d.pop("room", UNSET)

        _load_settings = d.pop("loadSettings", UNSET)
        load_settings: ApplianceUpdateLoadSettings | Unset
        if isinstance(_load_settings, Unset):
            load_settings = UNSET
        else:
            load_settings = ApplianceUpdateLoadSettings.from_dict(_load_settings)

        _kind = d.pop("kind", UNSET)
        kind: ApplianceUpdateKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ApplianceUpdateKind(_kind)

        _energy_settings = d.pop("energySettings", UNSET)
        energy_settings: ApplianceUpdateEnergyManagementSettings | Unset
        if isinstance(_energy_settings, Unset):
            energy_settings = UNSET
        else:
            energy_settings = ApplianceUpdateEnergyManagementSettings.from_dict(_energy_settings)

        _crypto_settings = d.pop("cryptoSettings", UNSET)
        crypto_settings: list[ApplianceUpdateCryptoSettingsItem] | Unset = UNSET
        if _crypto_settings is not UNSET:
            crypto_settings = []
            for crypto_settings_item_data in _crypto_settings:
                crypto_settings_item = ApplianceUpdateCryptoSettingsItem.from_dict(crypto_settings_item_data)

                crypto_settings.append(crypto_settings_item)

        _ev_load_management_parameters = d.pop("evLoadManagementParameters", UNSET)
        ev_load_management_parameters: ApplianceUpdateEvLoadManagementParameters | Unset
        if isinstance(_ev_load_management_parameters, Unset):
            ev_load_management_parameters = UNSET
        else:
            ev_load_management_parameters = ApplianceUpdateEvLoadManagementParameters.from_dict(
                _ev_load_management_parameters
            )

        evse_id = d.pop("evseID", UNSET)

        _desired_state = d.pop("desiredState", UNSET)
        desired_state: ApplianceUpdateApplianceState | Unset
        if isinstance(_desired_state, Unset):
            desired_state = UNSET
        else:
            desired_state = ApplianceUpdateApplianceState(_desired_state)

        _heat_pump = d.pop("heatPump", UNSET)
        heat_pump: ApplianceUpdateHeatPumpInformation | Unset
        if isinstance(_heat_pump, Unset):
            heat_pump = UNSET
        else:
            heat_pump = ApplianceUpdateHeatPumpInformation.from_dict(_heat_pump)

        _io_device = d.pop("ioDevice", UNSET)
        io_device: ApplianceUpdateIODeviceInformation | Unset
        if isinstance(_io_device, Unset):
            io_device = UNSET
        else:
            io_device = ApplianceUpdateIODeviceInformation.from_dict(_io_device)

        appliance_update = cls(
            inactive=inactive,
            name=name,
            reverse_flow=reverse_flow,
            room=room,
            load_settings=load_settings,
            kind=kind,
            energy_settings=energy_settings,
            crypto_settings=crypto_settings,
            ev_load_management_parameters=ev_load_management_parameters,
            evse_id=evse_id,
            desired_state=desired_state,
            heat_pump=heat_pump,
            io_device=io_device,
        )

        appliance_update.additional_properties = d
        return appliance_update

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
