from enum import Enum


class AbstractPowerSequenceState(str, Enum):
    COMPLETED = "completed"
    INACTIVE = "inactive"
    INVALID = "invalid"
    PAUSED = "paused"
    RUNNING = "running"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
