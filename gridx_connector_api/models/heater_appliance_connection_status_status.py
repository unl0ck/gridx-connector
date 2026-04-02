from enum import Enum


class HeaterApplianceConnectionStatusStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
