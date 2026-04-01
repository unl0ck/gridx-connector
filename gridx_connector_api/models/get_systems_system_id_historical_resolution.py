from enum import Enum


class GetSystemsSystemIDHistoricalResolution(str, Enum):
    VALUE_0 = "15m"
    VALUE_1 = "1h"
    VALUE_2 = "1d"
    VALUE_3 = "1w"
    VALUE_4 = "1M"

    def __str__(self) -> str:
        return str(self.value)
