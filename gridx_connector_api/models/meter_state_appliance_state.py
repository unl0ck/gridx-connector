from enum import Enum


class MeterStateApplianceState(str, Enum):
    CONNECTED = "CONNECTED"
    CONNECTING = "CONNECTING"
    DISCONNECTED = "DISCONNECTED"
    SCANNED = "SCANNED"
    UNKNOWN_APPLIANCE_STATE = "UNKNOWN_APPLIANCE_STATE"
    UNTRUSTED = "UNTRUSTED"
    VERIFYING = "VERIFYING"

    def __str__(self) -> str:
        return str(self.value)
