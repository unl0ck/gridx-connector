from enum import Enum


class PatchGatewaysGatewayIDResponse200ConnectionStatusStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
