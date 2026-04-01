from enum import Enum


class HeaterCommissioningKind(str, Enum):
    FLOWPAIRING = "flow:Pairing"
    PROPERTYCRYPTOSETTINGS = "property:CryptoSettings"

    def __str__(self) -> str:
        return str(self.value)
