from enum import Enum


class AbstractContainerContainerType(str, Enum):
    EEBUS = "EEBUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
