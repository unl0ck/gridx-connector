from enum import Enum


class AbstractIODeviceType(str, Enum):
    IO_DEVICE = "IO_DEVICE"

    def __str__(self) -> str:
        return str(self.value)
