from enum import Enum


class BaseApplianceCommissioningKind(str, Enum):
    FLOWPAIRING = "flow:Pairing"
    PROPERTYCRYPTOSETTINGS = "property:CryptoSettings"

    def __str__(self) -> str:
        return str(self.value)
