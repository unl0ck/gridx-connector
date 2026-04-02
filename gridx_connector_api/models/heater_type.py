from enum import Enum


class HeaterType(str, Enum):
    HEATER = "HEATER"

    def __str__(self) -> str:
        return str(self.value)
