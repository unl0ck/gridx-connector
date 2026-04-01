from enum import Enum


class GetGatewaysGatewayIDJobsResponse200ItemState(str, Enum):
    CANCELED = "CANCELED"
    DONE = "DONE"
    ERROR = "ERROR"
    PENDING = "PENDING"
    RECEIVED = "RECEIVED"
    STARTED = "STARTED"
    UNKNOWN_STATE = "UNKNOWN_STATE"

    def __str__(self) -> str:
        return str(self.value)
