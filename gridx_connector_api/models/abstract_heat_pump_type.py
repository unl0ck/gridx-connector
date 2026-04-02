from enum import Enum


class AbstractHeatPumpType(str, Enum):
    HEAT_PUMP = "HEAT_PUMP"

    def __str__(self) -> str:
        return str(self.value)
