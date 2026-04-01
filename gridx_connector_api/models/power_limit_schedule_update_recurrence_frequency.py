from enum import Enum


class PowerLimitScheduleUpdateRecurrenceFrequency(str, Enum):
    DAILY = "DAILY"

    def __str__(self) -> str:
        return str(self.value)
