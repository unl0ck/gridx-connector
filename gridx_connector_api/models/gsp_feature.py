from enum import Enum


class GSPFeature(str, Enum):
    VALUE_0 = "14a-lpc"

    def __str__(self) -> str:
        return str(self.value)
