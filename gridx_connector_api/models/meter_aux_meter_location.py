from enum import Enum


class MeterAuxMeterLocation(str, Enum):
    BATTERY = "BATTERY"
    BTTP = "BTTP"
    CLUSTER = "CLUSTER"
    EVSTATION = "EVSTATION"
    FUEL_CELL = "FUEL_CELL"
    GRID = "GRID"
    HEATING = "HEATING"
    HEAT_PUMP = "HEAT_PUMP"
    HEAT_PUMP_EXTERNAL = "HEAT_PUMP_EXTERNAL"
    MISC = "MISC"
    PV = "PV"
    PV_EXTERNAL = "PV_EXTERNAL"
    UNKNOWN = "UNKNOWN"
    WIND_TURBINE = "WIND_TURBINE"

    def __str__(self) -> str:
        return str(self.value)
