from enum import Enum


class AbstractContainerType(str, Enum):
    CONTAINER = "CONTAINER"

    def __str__(self) -> str:
        return str(self.value)
