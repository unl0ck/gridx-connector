from enum import Enum


class PatchGatewaysGatewayIDResponse200AdditionalIdentifiersOfTheGridBoxType(str, Enum):
    SKI = "SKI"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
