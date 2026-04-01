from enum import Enum


class SourceOrigin(str, Enum):
    API = "API"
    GRIDBOX = "GRIDBOX"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
