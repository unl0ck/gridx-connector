from enum import Enum


class PostSystemsSystemIDGatewaysResponse422Type(str, Enum):
    GENERAL = "GENERAL"
    STARTCODE_ALREADY_REGISTERED = "STARTCODE_ALREADY_REGISTERED"
    STARTCODE_NOT_FOUND = "STARTCODE_NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
