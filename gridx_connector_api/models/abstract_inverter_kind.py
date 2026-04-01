from enum import Enum


class AbstractInverterKind(str, Enum):
    BATTERY = "BATTERY"
    HYBRID = "HYBRID"
    PV = "PV"
    PV_EXTERNAL = "PV_EXTERNAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
