from enum import Enum


class HeatPumpInformationType(str, Enum):
    DAIKIN_HOMEHUB = "DAIKIN_HOMEHUB"
    EEBUS = "EEBUS"
    EXT_IO_DEVICE = "EXT_IO_DEVICE"
    EXT_IO_DEVICE_DHW = "EXT_IO_DEVICE_DHW"
    INNOTEC = "INNOTEC"
    SAIA_PCD_E_LINE = "SAIA_PCD_E_LINE"
    SIMULATION = "SIMULATION"
    STIEBEL_ELTRON_WPMSYSTEM = "STIEBEL_ELTRON_WPMSYSTEM"
    UNKNOWN = "UNKNOWN"
    XNET_CLOUD = "XNET_CLOUD"

    def __str__(self) -> str:
        return str(self.value)
