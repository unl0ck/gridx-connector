from enum import Enum


class StatusHistoryPeriodsItemStatus(str, Enum):
    DISABLED = "DISABLED"
    INITIALIZING = "INITIALIZING"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    SUBOPTIMAL = "SUBOPTIMAL"

    def __str__(self) -> str:
        return str(self.value)
