from enum import Enum


class PostSystemsSystemIDGatewaysResponse201Type(str, Enum):
    OTHER = "OTHER"
    PHYSICAL = "PHYSICAL"
    VIRTUAL = "VIRTUAL"

    def __str__(self) -> str:
        return str(self.value)
