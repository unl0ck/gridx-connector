from enum import Enum


class DevicesAdditionalPropertyItemBindingsItemType(str, Enum):
    POWERSEQUENCE = "powerSequence"

    def __str__(self) -> str:
        return str(self.value)
