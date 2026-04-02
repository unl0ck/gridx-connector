from enum import IntEnum


class ImportPowerLimitNumberOfPhases(IntEnum):
    VALUE_1 = 1
    VALUE_3 = 3

    def __str__(self) -> str:
        return str(self.value)
