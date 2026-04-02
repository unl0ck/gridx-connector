from enum import Enum


class AbstractEVStationType(str, Enum):
    EVSTATION = "EVSTATION"

    def __str__(self) -> str:
        return str(self.value)
