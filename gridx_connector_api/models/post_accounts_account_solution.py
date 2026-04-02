from enum import Enum


class PostAccountsAccountSolution(str, Enum):
    CHARGE = "CHARGE"
    COMMERCIAL = "COMMERCIAL"
    CUSTOM_P2P = "CUSTOM_P2P"
    GENERAL = "GENERAL"
    HOME = "HOME"
    HOME_VIRTUAL_METERING = "HOME_VIRTUAL_METERING"
    MICROGRID = "MICROGRID"
    SMART_DISTRICT = "SMART_DISTRICT"

    def __str__(self) -> str:
        return str(self.value)
