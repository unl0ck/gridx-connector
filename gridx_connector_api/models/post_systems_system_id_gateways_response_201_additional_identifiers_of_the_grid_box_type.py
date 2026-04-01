from enum import Enum


class PostSystemsSystemIDGatewaysResponse201AdditionalIdentifiersOfTheGridBoxType(str, Enum):
    SKI = "SKI"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
