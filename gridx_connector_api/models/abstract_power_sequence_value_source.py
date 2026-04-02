from enum import Enum


class AbstractPowerSequenceValueSource(str, Enum):
    CALCULATEDVALUE = "calculatedValue"
    EMPIRICALVALUE = "empiricalValue"
    MEASUREDVALUE = "measuredValue"

    def __str__(self) -> str:
        return str(self.value)
