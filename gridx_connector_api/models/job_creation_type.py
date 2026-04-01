from enum import Enum


class JobCreationType(str, Enum):
    RESET = "RESET"
    RESTART = "RESTART"
    SCAN = "SCAN"
    UNKNOWN_TYPE = "UNKNOWN_TYPE"

    def __str__(self) -> str:
        return str(self.value)
