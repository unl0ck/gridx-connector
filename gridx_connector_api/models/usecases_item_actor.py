from enum import Enum


class UsecasesItemActor(str, Enum):
    CLIENT = "client"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
