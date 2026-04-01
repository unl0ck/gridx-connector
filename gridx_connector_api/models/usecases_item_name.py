from enum import Enum


class UsecasesItemName(str, Enum):
    FSWG = "fswg"

    def __str__(self) -> str:
        return str(self.value)
