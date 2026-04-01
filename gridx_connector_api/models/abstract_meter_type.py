from enum import Enum


class AbstractMeterType(str, Enum):
    METER = "METER"

    def __str__(self) -> str:
        return str(self.value)
