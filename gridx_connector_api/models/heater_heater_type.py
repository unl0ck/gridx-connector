from enum import Enum


class HeaterHeaterType(str, Enum):
    EXT_IO_DEVICE_ELECTRIC = "EXT_IO_DEVICE_ELECTRIC"
    MY_PV_AC_THOR = "MY_PV_AC_THOR"
    SIMULATION = "SIMULATION"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
