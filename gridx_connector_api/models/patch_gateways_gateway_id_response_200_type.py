from enum import Enum


class PatchGatewaysGatewayIDResponse200Type(str, Enum):
    OTHER = "OTHER"
    PHYSICAL = "PHYSICAL"
    VIRTUAL = "VIRTUAL"

    def __str__(self) -> str:
        return str(self.value)
