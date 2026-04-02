from enum import Enum


class FeedinTariffType(str, Enum):
    EXTERNAL = "EXTERNAL"
    MARKET_DATA = "MARKET_DATA"
    STATIC = "STATIC"

    def __str__(self) -> str:
        return str(self.value)
