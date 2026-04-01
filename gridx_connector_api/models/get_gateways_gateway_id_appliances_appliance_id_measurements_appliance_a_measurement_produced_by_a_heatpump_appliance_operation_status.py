from enum import Enum


class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceAMeasurementProducedByAHeatpumpApplianceOperationStatus(
    str, Enum
):
    COOLING = "COOLING"
    DEFROST = "DEFROST"
    DRINKING_HOT_WATER = "DRINKING_HOT_WATER"
    EVU_LOCK = "EVU_LOCK"
    EXTERNAL_SOURCE = "EXTERNAL_SOURCE"
    HEATING = "HEATING"
    OFF = "OFF"
    POOL_HEATING = "POOL_HEATING"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
