from enum import Enum


class GetSystemsSystemIDPowerLimitSchedulesScheduleIDResponse200Status(str, Enum):
    ACTIVE = "ACTIVE"
    OUTDATED = "OUTDATED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
