from enum import Enum


class ContainerType(str, Enum):
    CONTAINER = "CONTAINER"

    def __str__(self) -> str:
        return str(self.value)
