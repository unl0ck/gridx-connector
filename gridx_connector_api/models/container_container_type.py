from enum import Enum


class ContainerContainerType(str, Enum):
    EEBUS = "EEBUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
