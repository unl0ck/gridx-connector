from enum import Enum


class PowerLimitScheduleRecurrenceByDayOfWeekItem(str, Enum):
    FR = "FR"
    MO = "MO"
    SA = "SA"
    SU = "SU"
    TH = "TH"
    TU = "TU"
    WE = "WE"

    def __str__(self) -> str:
        return str(self.value)
