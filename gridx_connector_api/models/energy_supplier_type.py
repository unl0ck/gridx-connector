from enum import Enum


class EnergySupplierType(str, Enum):
    GRIDX = "GRIDX"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
