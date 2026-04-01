from enum import Enum


class ContainerSourceOrigin(str, Enum):
    API = "API"
    GRIDBOX = "GRIDBOX"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
