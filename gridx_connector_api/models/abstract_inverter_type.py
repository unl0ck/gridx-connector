from enum import Enum


class AbstractInverterType(str, Enum):
    INVERTER = "INVERTER"

    def __str__(self) -> str:
        return str(self.value)
