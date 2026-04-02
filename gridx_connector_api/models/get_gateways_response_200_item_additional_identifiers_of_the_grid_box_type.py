from enum import Enum


class GetGatewaysResponse200ItemAdditionalIdentifiersOfTheGridBoxType(str, Enum):
    SKI = "SKI"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
