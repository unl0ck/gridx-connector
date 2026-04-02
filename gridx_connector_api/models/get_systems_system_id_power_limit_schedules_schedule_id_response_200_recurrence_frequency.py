from enum import Enum


class GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200RecurrenceFrequency(str, Enum):
    DAILY = "DAILY"

    def __str__(self) -> str:
        return str(self.value)
