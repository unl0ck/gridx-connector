from enum import Enum


class MeterSourceOrigin(str, Enum):
    API = "API"
    GRIDBOX = "GRIDBOX"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
