from enum import Enum


class DevicesAdditionalPropertyItemUsecasesItemName(str, Enum):
    FSWG = "fswg"

    def __str__(self) -> str:
        return str(self.value)
