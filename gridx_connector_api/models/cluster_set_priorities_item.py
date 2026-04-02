from enum import Enum


class ClusterSetPrioritiesItem(str, Enum):
    BATTERY = "BATTERY"
    EV = "EV"
    HEATER = "HEATER"
    HEATPUMP = "HEATPUMP"

    def __str__(self) -> str:
        return str(self.value)
