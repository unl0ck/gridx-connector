from enum import Enum


class RunStatusesItemStatus(str, Enum):
    DISABLED = "DISABLED"
    INITIALIZING = "INITIALIZING"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    SUBOPTIMAL = "SUBOPTIMAL"

    def __str__(self) -> str:
        return str(self.value)
