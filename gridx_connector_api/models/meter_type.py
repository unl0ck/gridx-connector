from enum import Enum


class MeterType(str, Enum):
    METER = "METER"

    def __str__(self) -> str:
        return str(self.value)
