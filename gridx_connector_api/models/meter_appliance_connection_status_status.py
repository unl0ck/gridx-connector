from enum import Enum


class MeterApplianceConnectionStatusStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
