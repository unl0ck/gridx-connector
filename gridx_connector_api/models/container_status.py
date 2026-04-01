from enum import Enum


class ContainerStatus(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    UNDEFINED = "UNDEFINED"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
