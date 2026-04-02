from enum import Enum


class EVChargingStationConfigurationCreationChargeMode(str, Enum):
    DEPARTURE_TIME_EV = "DEPARTURE_TIME_EV"
    FORCED_EV = "FORCED_EV"
    MIN_EV = "MIN_EV"
    SURPLUS_EV = "SURPLUS_EV"

    def __str__(self) -> str:
        return str(self.value)
