from enum import Enum


class GSP14ASignalLpcServerState(str, Enum):
    FAILSAFE = "FAILSAFE"
    INIT = "INIT"
    LIMITED = "LIMITED"
    UNLIMITED_AUTONOMOUS = "UNLIMITED_AUTONOMOUS"
    UNLIMITED_CONTROLLED = "UNLIMITED_CONTROLLED"

    def __str__(self) -> str:
        return str(self.value)
