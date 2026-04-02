from enum import Enum


class DeviceBindingsItemType(str, Enum):
    POWERSEQUENCE = "powerSequence"

    def __str__(self) -> str:
        return str(self.value)
