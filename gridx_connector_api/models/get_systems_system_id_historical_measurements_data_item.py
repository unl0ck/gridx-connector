from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_systems_system_id_historical_measurements_data_item_additional_meter_appliances import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_battery_measurement import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_extended_battery_measurement import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_extended_ev_station_measurement import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_heater_measurement import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation,
    )
    from ..models.get_systems_system_id_historical_measurements_data_item_measurement_grid import (
        GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid,
    )


T = TypeVar("T", bound="GetSystemsSystemIDHistoricalMeasurementsDataItem")


@_attrs_define
class GetSystemsSystemIDHistoricalMeasurementsDataItem:
    """
    Attributes:
        measured_at (str | Unset): Time when the data was measured.
        grid_l1 (float | Unset): GridL1 is the part of the grid connection point's first phase.
        grid_l2 (float | Unset): GridL2 is the part of the grid connection point's second phase.
        grid_l3 (float | Unset): GridL3 is the part of the grid connection point's second phase.
        grid_supply_limit (float | Unset): GridSupplyLimit is the restriction of supplied power at the grid
            connection point.
        photovoltaic (float | Unset): Photovoltaic is the measured power/energy in front of the
            photovoltaic systems.
        photovoltaic_external (float | Unset): PhotovoltaicExternal is the measured power/energy in front of the
            external photovoltaic systems.
        block_type_thermal_power_station (float | Unset): BTTPPower is the measured power for the block-type thermal
            power
            station.
        fuel_cell (float | Unset): FuelCell is the measured power/energy in front of the fuel cells.
        production (float | Unset): Production is sum of the producers.
        batteries (list[GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement] | Unset):
        heat_pump (float | Unset): HeatPump is the measured power/energy in front of the heat pumps.
        heat_pump_external (float | Unset): HeatPumpExternal is the measured power/energy in front of the heat
            pump which has its own heat pump tariff.
        ev_charging_stations (list[GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowe
            rOrEnergyTheGatewayMeasuredfromAEvChargingStation] | Unset):
        consumption (float | Unset): Consumption is adjusted power/energy of the system.
        total_consumption (float | Unset): Adjusted power/energy of the system which
            includes heatpump and EV.
        self_consumption (float | Unset): SelfConsumption is power/energy consumed through production and
            charged into battery.
        direct_consumption (float | Unset): DirectConsumption is power/energy consumed from production directly.
        direct_consumption_household (float | Unset): DirectConsumptionHousehold is power/energy consumed by the
            household through production directly.
        direct_consumption_heat_pump (float | Unset): DirectConsumptionHeatPump is power/energy consumed by the heat
            pump
            through production directly.
        direct_consumption_ev (float | Unset): DirectConsumptionEV is power/energy consumed by the EV through
            production directly.
        direct_consumption_heater (float | Unset): DirectConsumptionHeater is the power/energy consumed by the heater
            through production directly.
        self_supply (float | Unset): SelfSupply is power/energy consumed through storage and production.
        self_sufficiency_rate (float | Unset):
        self_consumption_rate (float | Unset):
        direct_consumption_rate (float | Unset):
        heating (float | Unset): HeatingPower is the aggregated amount of power measured for heaters.
        heating_temperature (float | Unset): HeatingTemperature is temperature of the heaters.
        heaters (list[GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement] | Unset): Heating measurement
            for all heaters that are part of the system.
        appliance_power (float | Unset): AppliancePower is power of the appliances with misc location.
        appliances (list[GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances] | Unset):
        grid_meter_reading_positive (float | Unset): GridMeterReadingPositive is the meter Reading for grid in Ws
            (Imported Energy).
        grid_meter_reading_negative (float | Unset): GridMeterReadingPositive is the meter Reading for grid in Ws
            (Exported Energy).
        heat_pump_meter_reading_positive (float | Unset): HeatPumpMeterReadingPositive is the meter Reading for HeatPump
            in Ws
            (Imported Energy).
        heat_pump_meter_reading_negative (float | Unset): HeatPumpMeterReadingNegative is the meter Reading for HeatPump
            in Ws
            (Exported Energy).
        wind_turbine (float | Unset):
        fuel_cell_meter_reading_positive (float | Unset): Meter reading for FuelCell in Ws (Imported Energy).
        fuel_cell_meter_reading_negative (float | Unset): Meter reading for FuelCell in Ws (Exported Energy).
        l_1_curtailment_power (float | Unset): Potential max. charging power minus the actual setpoint in Ws on phase 1.
        l_2_curtailment_power (float | Unset): Potential max. charging power minus the actual setpoint in Ws on phase 2.
        l_3_curtailment_power (float | Unset): Potential max. charging power minus the actual setpoint in Ws on phase 3.
        fuse_protection_count (int | Unset): Number of times the fuse was protected, based on the curtailed power over
            all phases.
        grid (GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid | Unset):
        battery (GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement | Unset):
        ev_charging_station (GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement | Unset):
    """

    measured_at: str | Unset = UNSET
    grid_l1: float | Unset = UNSET
    grid_l2: float | Unset = UNSET
    grid_l3: float | Unset = UNSET
    grid_supply_limit: float | Unset = UNSET
    photovoltaic: float | Unset = UNSET
    photovoltaic_external: float | Unset = UNSET
    block_type_thermal_power_station: float | Unset = UNSET
    fuel_cell: float | Unset = UNSET
    production: float | Unset = UNSET
    batteries: list[GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement] | Unset = UNSET
    heat_pump: float | Unset = UNSET
    heat_pump_external: float | Unset = UNSET
    ev_charging_stations: (
        list[
            GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation
        ]
        | Unset
    ) = UNSET
    consumption: float | Unset = UNSET
    total_consumption: float | Unset = UNSET
    self_consumption: float | Unset = UNSET
    direct_consumption: float | Unset = UNSET
    direct_consumption_household: float | Unset = UNSET
    direct_consumption_heat_pump: float | Unset = UNSET
    direct_consumption_ev: float | Unset = UNSET
    direct_consumption_heater: float | Unset = UNSET
    self_supply: float | Unset = UNSET
    self_sufficiency_rate: float | Unset = UNSET
    self_consumption_rate: float | Unset = UNSET
    direct_consumption_rate: float | Unset = UNSET
    heating: float | Unset = UNSET
    heating_temperature: float | Unset = UNSET
    heaters: list[GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement] | Unset = UNSET
    appliance_power: float | Unset = UNSET
    appliances: list[GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances] | Unset = UNSET
    grid_meter_reading_positive: float | Unset = UNSET
    grid_meter_reading_negative: float | Unset = UNSET
    heat_pump_meter_reading_positive: float | Unset = UNSET
    heat_pump_meter_reading_negative: float | Unset = UNSET
    wind_turbine: float | Unset = UNSET
    fuel_cell_meter_reading_positive: float | Unset = UNSET
    fuel_cell_meter_reading_negative: float | Unset = UNSET
    l_1_curtailment_power: float | Unset = UNSET
    l_2_curtailment_power: float | Unset = UNSET
    l_3_curtailment_power: float | Unset = UNSET
    fuse_protection_count: int | Unset = UNSET
    grid: GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid | Unset = UNSET
    battery: GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement | Unset = UNSET
    ev_charging_station: GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at = self.measured_at

        grid_l1 = self.grid_l1

        grid_l2 = self.grid_l2

        grid_l3 = self.grid_l3

        grid_supply_limit = self.grid_supply_limit

        photovoltaic = self.photovoltaic

        photovoltaic_external = self.photovoltaic_external

        block_type_thermal_power_station = self.block_type_thermal_power_station

        fuel_cell = self.fuel_cell

        production = self.production

        batteries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.batteries, Unset):
            batteries = []
            for batteries_item_data in self.batteries:
                batteries_item = batteries_item_data.to_dict()
                batteries.append(batteries_item)

        heat_pump = self.heat_pump

        heat_pump_external = self.heat_pump_external

        ev_charging_stations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ev_charging_stations, Unset):
            ev_charging_stations = []
            for ev_charging_stations_item_data in self.ev_charging_stations:
                ev_charging_stations_item = ev_charging_stations_item_data.to_dict()
                ev_charging_stations.append(ev_charging_stations_item)

        consumption = self.consumption

        total_consumption = self.total_consumption

        self_consumption = self.self_consumption

        direct_consumption = self.direct_consumption

        direct_consumption_household = self.direct_consumption_household

        direct_consumption_heat_pump = self.direct_consumption_heat_pump

        direct_consumption_ev = self.direct_consumption_ev

        direct_consumption_heater = self.direct_consumption_heater

        self_supply = self.self_supply

        self_sufficiency_rate = self.self_sufficiency_rate

        self_consumption_rate = self.self_consumption_rate

        direct_consumption_rate = self.direct_consumption_rate

        heating = self.heating

        heating_temperature = self.heating_temperature

        heaters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.heaters, Unset):
            heaters = []
            for heaters_item_data in self.heaters:
                heaters_item = heaters_item_data.to_dict()
                heaters.append(heaters_item)

        appliance_power = self.appliance_power

        appliances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.appliances, Unset):
            appliances = []
            for appliances_item_data in self.appliances:
                appliances_item = appliances_item_data.to_dict()
                appliances.append(appliances_item)

        grid_meter_reading_positive = self.grid_meter_reading_positive

        grid_meter_reading_negative = self.grid_meter_reading_negative

        heat_pump_meter_reading_positive = self.heat_pump_meter_reading_positive

        heat_pump_meter_reading_negative = self.heat_pump_meter_reading_negative

        wind_turbine = self.wind_turbine

        fuel_cell_meter_reading_positive = self.fuel_cell_meter_reading_positive

        fuel_cell_meter_reading_negative = self.fuel_cell_meter_reading_negative

        l_1_curtailment_power = self.l_1_curtailment_power

        l_2_curtailment_power = self.l_2_curtailment_power

        l_3_curtailment_power = self.l_3_curtailment_power

        fuse_protection_count = self.fuse_protection_count

        grid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grid, Unset):
            grid = self.grid.to_dict()

        battery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery, Unset):
            battery = self.battery.to_dict()

        ev_charging_station: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ev_charging_station, Unset):
            ev_charging_station = self.ev_charging_station.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if grid_l1 is not UNSET:
            field_dict["gridL1"] = grid_l1
        if grid_l2 is not UNSET:
            field_dict["gridL2"] = grid_l2
        if grid_l3 is not UNSET:
            field_dict["gridL3"] = grid_l3
        if grid_supply_limit is not UNSET:
            field_dict["gridSupplyLimit"] = grid_supply_limit
        if photovoltaic is not UNSET:
            field_dict["photovoltaic"] = photovoltaic
        if photovoltaic_external is not UNSET:
            field_dict["photovoltaicExternal"] = photovoltaic_external
        if block_type_thermal_power_station is not UNSET:
            field_dict["blockTypeThermalPowerStation"] = block_type_thermal_power_station
        if fuel_cell is not UNSET:
            field_dict["fuelCell"] = fuel_cell
        if production is not UNSET:
            field_dict["production"] = production
        if batteries is not UNSET:
            field_dict["batteries"] = batteries
        if heat_pump is not UNSET:
            field_dict["heatPump"] = heat_pump
        if heat_pump_external is not UNSET:
            field_dict["heatPumpExternal"] = heat_pump_external
        if ev_charging_stations is not UNSET:
            field_dict["evChargingStations"] = ev_charging_stations
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if total_consumption is not UNSET:
            field_dict["totalConsumption"] = total_consumption
        if self_consumption is not UNSET:
            field_dict["selfConsumption"] = self_consumption
        if direct_consumption is not UNSET:
            field_dict["directConsumption"] = direct_consumption
        if direct_consumption_household is not UNSET:
            field_dict["directConsumptionHousehold"] = direct_consumption_household
        if direct_consumption_heat_pump is not UNSET:
            field_dict["directConsumptionHeatPump"] = direct_consumption_heat_pump
        if direct_consumption_ev is not UNSET:
            field_dict["directConsumptionEV"] = direct_consumption_ev
        if direct_consumption_heater is not UNSET:
            field_dict["directConsumptionHeater"] = direct_consumption_heater
        if self_supply is not UNSET:
            field_dict["selfSupply"] = self_supply
        if self_sufficiency_rate is not UNSET:
            field_dict["selfSufficiencyRate"] = self_sufficiency_rate
        if self_consumption_rate is not UNSET:
            field_dict["selfConsumptionRate"] = self_consumption_rate
        if direct_consumption_rate is not UNSET:
            field_dict["directConsumptionRate"] = direct_consumption_rate
        if heating is not UNSET:
            field_dict["heating"] = heating
        if heating_temperature is not UNSET:
            field_dict["heatingTemperature"] = heating_temperature
        if heaters is not UNSET:
            field_dict["heaters"] = heaters
        if appliance_power is not UNSET:
            field_dict["appliancePower"] = appliance_power
        if appliances is not UNSET:
            field_dict["appliances"] = appliances
        if grid_meter_reading_positive is not UNSET:
            field_dict["gridMeterReadingPositive"] = grid_meter_reading_positive
        if grid_meter_reading_negative is not UNSET:
            field_dict["gridMeterReadingNegative"] = grid_meter_reading_negative
        if heat_pump_meter_reading_positive is not UNSET:
            field_dict["heatPumpMeterReadingPositive"] = heat_pump_meter_reading_positive
        if heat_pump_meter_reading_negative is not UNSET:
            field_dict["heatPumpMeterReadingNegative"] = heat_pump_meter_reading_negative
        if wind_turbine is not UNSET:
            field_dict["windTurbine"] = wind_turbine
        if fuel_cell_meter_reading_positive is not UNSET:
            field_dict["fuelCellMeterReadingPositive"] = fuel_cell_meter_reading_positive
        if fuel_cell_meter_reading_negative is not UNSET:
            field_dict["fuelCellMeterReadingNegative"] = fuel_cell_meter_reading_negative
        if l_1_curtailment_power is not UNSET:
            field_dict["l1CurtailmentPower"] = l_1_curtailment_power
        if l_2_curtailment_power is not UNSET:
            field_dict["l2CurtailmentPower"] = l_2_curtailment_power
        if l_3_curtailment_power is not UNSET:
            field_dict["l3CurtailmentPower"] = l_3_curtailment_power
        if fuse_protection_count is not UNSET:
            field_dict["fuseProtectionCount"] = fuse_protection_count
        if grid is not UNSET:
            field_dict["grid"] = grid
        if battery is not UNSET:
            field_dict["battery"] = battery
        if ev_charging_station is not UNSET:
            field_dict["evChargingStation"] = ev_charging_station

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_systems_system_id_historical_measurements_data_item_additional_meter_appliances import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_battery_measurement import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_extended_battery_measurement import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_extended_ev_station_measurement import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_heater_measurement import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_measurement_ev_station_represents_the_power_or_energy_the_gateway_measuredfrom_a_ev_charging_station import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation,
        )
        from ..models.get_systems_system_id_historical_measurements_data_item_measurement_grid import (
            GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid,
        )

        d = dict(src_dict)
        measured_at = d.pop("measuredAt", UNSET)

        grid_l1 = d.pop("gridL1", UNSET)

        grid_l2 = d.pop("gridL2", UNSET)

        grid_l3 = d.pop("gridL3", UNSET)

        grid_supply_limit = d.pop("gridSupplyLimit", UNSET)

        photovoltaic = d.pop("photovoltaic", UNSET)

        photovoltaic_external = d.pop("photovoltaicExternal", UNSET)

        block_type_thermal_power_station = d.pop("blockTypeThermalPowerStation", UNSET)

        fuel_cell = d.pop("fuelCell", UNSET)

        production = d.pop("production", UNSET)

        _batteries = d.pop("batteries", UNSET)
        batteries: list[GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement] | Unset = UNSET
        if _batteries is not UNSET:
            batteries = []
            for batteries_item_data in _batteries:
                batteries_item = GetSystemsSystemIDHistoricalMeasurementsDataItemBatteryMeasurement.from_dict(
                    batteries_item_data
                )

                batteries.append(batteries_item)

        heat_pump = d.pop("heatPump", UNSET)

        heat_pump_external = d.pop("heatPumpExternal", UNSET)

        _ev_charging_stations = d.pop("evChargingStations", UNSET)
        ev_charging_stations: (
            list[
                GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation
            ]
            | Unset
        ) = UNSET
        if _ev_charging_stations is not UNSET:
            ev_charging_stations = []
            for ev_charging_stations_item_data in _ev_charging_stations:
                ev_charging_stations_item = GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStation.from_dict(
                    ev_charging_stations_item_data
                )

                ev_charging_stations.append(ev_charging_stations_item)

        consumption = d.pop("consumption", UNSET)

        total_consumption = d.pop("totalConsumption", UNSET)

        self_consumption = d.pop("selfConsumption", UNSET)

        direct_consumption = d.pop("directConsumption", UNSET)

        direct_consumption_household = d.pop("directConsumptionHousehold", UNSET)

        direct_consumption_heat_pump = d.pop("directConsumptionHeatPump", UNSET)

        direct_consumption_ev = d.pop("directConsumptionEV", UNSET)

        direct_consumption_heater = d.pop("directConsumptionHeater", UNSET)

        self_supply = d.pop("selfSupply", UNSET)

        self_sufficiency_rate = d.pop("selfSufficiencyRate", UNSET)

        self_consumption_rate = d.pop("selfConsumptionRate", UNSET)

        direct_consumption_rate = d.pop("directConsumptionRate", UNSET)

        heating = d.pop("heating", UNSET)

        heating_temperature = d.pop("heatingTemperature", UNSET)

        _heaters = d.pop("heaters", UNSET)
        heaters: list[GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement] | Unset = UNSET
        if _heaters is not UNSET:
            heaters = []
            for heaters_item_data in _heaters:
                heaters_item = GetSystemsSystemIDHistoricalMeasurementsDataItemHeaterMeasurement.from_dict(
                    heaters_item_data
                )

                heaters.append(heaters_item)

        appliance_power = d.pop("appliancePower", UNSET)

        _appliances = d.pop("appliances", UNSET)
        appliances: list[GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances] | Unset = UNSET
        if _appliances is not UNSET:
            appliances = []
            for appliances_item_data in _appliances:
                appliances_item = GetSystemsSystemIDHistoricalMeasurementsDataItemAdditionalMeterAppliances.from_dict(
                    appliances_item_data
                )

                appliances.append(appliances_item)

        grid_meter_reading_positive = d.pop("gridMeterReadingPositive", UNSET)

        grid_meter_reading_negative = d.pop("gridMeterReadingNegative", UNSET)

        heat_pump_meter_reading_positive = d.pop("heatPumpMeterReadingPositive", UNSET)

        heat_pump_meter_reading_negative = d.pop("heatPumpMeterReadingNegative", UNSET)

        wind_turbine = d.pop("windTurbine", UNSET)

        fuel_cell_meter_reading_positive = d.pop("fuelCellMeterReadingPositive", UNSET)

        fuel_cell_meter_reading_negative = d.pop("fuelCellMeterReadingNegative", UNSET)

        l_1_curtailment_power = d.pop("l1CurtailmentPower", UNSET)

        l_2_curtailment_power = d.pop("l2CurtailmentPower", UNSET)

        l_3_curtailment_power = d.pop("l3CurtailmentPower", UNSET)

        fuse_protection_count = d.pop("fuseProtectionCount", UNSET)

        _grid = d.pop("grid", UNSET)
        grid: GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid | Unset
        if isinstance(_grid, Unset):
            grid = UNSET
        else:
            grid = GetSystemsSystemIDHistoricalMeasurementsDataItemMeasurementGrid.from_dict(_grid)

        _battery = d.pop("battery", UNSET)
        battery: GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement | Unset
        if isinstance(_battery, Unset):
            battery = UNSET
        else:
            battery = GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedBatteryMeasurement.from_dict(_battery)

        _ev_charging_station = d.pop("evChargingStation", UNSET)
        ev_charging_station: GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement | Unset
        if isinstance(_ev_charging_station, Unset):
            ev_charging_station = UNSET
        else:
            ev_charging_station = (
                GetSystemsSystemIDHistoricalMeasurementsDataItemExtendedEVStationMeasurement.from_dict(
                    _ev_charging_station
                )
            )

        get_systems_system_id_historical_measurements_data_item = cls(
            measured_at=measured_at,
            grid_l1=grid_l1,
            grid_l2=grid_l2,
            grid_l3=grid_l3,
            grid_supply_limit=grid_supply_limit,
            photovoltaic=photovoltaic,
            photovoltaic_external=photovoltaic_external,
            block_type_thermal_power_station=block_type_thermal_power_station,
            fuel_cell=fuel_cell,
            production=production,
            batteries=batteries,
            heat_pump=heat_pump,
            heat_pump_external=heat_pump_external,
            ev_charging_stations=ev_charging_stations,
            consumption=consumption,
            total_consumption=total_consumption,
            self_consumption=self_consumption,
            direct_consumption=direct_consumption,
            direct_consumption_household=direct_consumption_household,
            direct_consumption_heat_pump=direct_consumption_heat_pump,
            direct_consumption_ev=direct_consumption_ev,
            direct_consumption_heater=direct_consumption_heater,
            self_supply=self_supply,
            self_sufficiency_rate=self_sufficiency_rate,
            self_consumption_rate=self_consumption_rate,
            direct_consumption_rate=direct_consumption_rate,
            heating=heating,
            heating_temperature=heating_temperature,
            heaters=heaters,
            appliance_power=appliance_power,
            appliances=appliances,
            grid_meter_reading_positive=grid_meter_reading_positive,
            grid_meter_reading_negative=grid_meter_reading_negative,
            heat_pump_meter_reading_positive=heat_pump_meter_reading_positive,
            heat_pump_meter_reading_negative=heat_pump_meter_reading_negative,
            wind_turbine=wind_turbine,
            fuel_cell_meter_reading_positive=fuel_cell_meter_reading_positive,
            fuel_cell_meter_reading_negative=fuel_cell_meter_reading_negative,
            l_1_curtailment_power=l_1_curtailment_power,
            l_2_curtailment_power=l_2_curtailment_power,
            l_3_curtailment_power=l_3_curtailment_power,
            fuse_protection_count=fuse_protection_count,
            grid=grid,
            battery=battery,
            ev_charging_station=ev_charging_station,
        )

        get_systems_system_id_historical_measurements_data_item.additional_properties = d
        return get_systems_system_id_historical_measurements_data_item

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
