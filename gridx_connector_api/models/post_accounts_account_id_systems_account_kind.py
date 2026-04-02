from enum import Enum


class PostAccountsAccountIDSystemsAccountKind(str, Enum):
    B2B = "b2b"
    END_USER = "end-user"

    def __str__(self) -> str:
        return str(self.value)
