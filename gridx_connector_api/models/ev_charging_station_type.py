from enum import Enum


class EVChargingStationType(str, Enum):
    EVSTATION = "EVSTATION"

    def __str__(self) -> str:
        return str(self.value)
