from enum import Enum


class PostGatewaysGatewayIDJobsJobIDOrTypeResponse201Type(str, Enum):
    RESET = "RESET"
    RESTART = "RESTART"
    SCAN = "SCAN"
    UNKNOWN_TYPE = "UNKNOWN_TYPE"

    def __str__(self) -> str:
        return str(self.value)
