from enum import Enum


class HardwareStatusState(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
