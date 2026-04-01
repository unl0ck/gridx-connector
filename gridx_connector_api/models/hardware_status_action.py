from enum import Enum


class HardwareStatusAction(str, Enum):
    CONSULT_DEVICE_READOUT = "CONSULT_DEVICE_READOUT"
    CONTACT_GRID_OPERATOR = "CONTACT_GRID_OPERATOR"
    CONTACT_INSTALLER = "CONTACT_INSTALLER"
    CONTACT_MANUFACTURER = "CONTACT_MANUFACTURER"

    def __str__(self) -> str:
        return str(self.value)
