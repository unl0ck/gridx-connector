from enum import Enum


class DeviceUsecasesItemActor(str, Enum):
    CLIENT = "client"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
