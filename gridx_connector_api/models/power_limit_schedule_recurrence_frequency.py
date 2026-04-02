from enum import Enum


class PowerLimitScheduleRecurrenceFrequency(str, Enum):
    DAILY = "DAILY"

    def __str__(self) -> str:
        return str(self.value)
