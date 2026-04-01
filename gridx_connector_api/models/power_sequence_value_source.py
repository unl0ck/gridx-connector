from enum import Enum


class PowerSequenceValueSource(str, Enum):
    CALCULATEDVALUE = "calculatedValue"
    EMPIRICALVALUE = "empiricalValue"
    MEASUREDVALUE = "measuredValue"

    def __str__(self) -> str:
        return str(self.value)
