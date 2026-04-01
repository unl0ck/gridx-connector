from enum import Enum


class AbstractInverterBatteryInformationControlSettingsCommand(str, Enum):
    CHARGE = "charge"
    DISCHARGE = "discharge"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
