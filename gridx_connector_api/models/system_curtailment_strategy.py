from enum import Enum


class SystemCurtailmentStrategy(str, Enum):
    EQUALLY = "EQUALLY"
    PROPORTIONAL = "PROPORTIONAL"
    SERIES = "SERIES"

    def __str__(self) -> str:
        return str(self.value)
