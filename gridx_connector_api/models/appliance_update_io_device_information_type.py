from enum import Enum


class ApplianceUpdateIODeviceInformationType(str, Enum):
    JANITZA = "JANITZA"
    JANITZA_UMG604 = "JANITZA_UMG604"
    RUTENBECK_TCR_IP4 = "RUTENBECK_TCR_IP4"
    SGREADY = "SGREADY"
    SHELLY = "SHELLY"
    SHELLY3EMPRO = "SHELLY3EMPRO"
    SHELLYPLUS1PM = "SHELLYPLUS1PM"
    SHELLYPLUS2PM = "SHELLYPLUS2PM"
    SHELLYPRO2 = "SHELLYPRO2"
    SIEMENS_PAC_7KM_2200 = "SIEMENS_PAC_7KM_2200"
    UNKNOWN = "UNKNOWN"
    WAGO = "WAGO"

    def __str__(self) -> str:
        return str(self.value)
