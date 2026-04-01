from enum import Enum


class MeasurementsTotalMeasurementEVStationRepresentsThePowerOrEnergyTheGatewayMeasuredfromAEvChargingStationPlugState(
    str, Enum
):
    PLUGGED_ON_STATION = "PLUGGED_ON_STATION"
    PLUGGED_ON_STATION_AND_PLUGGED_ON_VEHICLE = "PLUGGED_ON_STATION_AND_PLUGGED_ON_VEHICLE"
    UNPLUGGED = "UNPLUGGED"

    def __str__(self) -> str:
        return str(self.value)
