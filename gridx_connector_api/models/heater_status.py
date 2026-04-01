from enum import Enum


class HeaterStatus(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    UNDEFINED = "UNDEFINED"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
