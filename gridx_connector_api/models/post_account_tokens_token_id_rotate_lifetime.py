from enum import Enum


class PostAccountTokensTokenIDRotateLifetime(str, Enum):
    VALUE_0 = "1D"
    VALUE_1 = "1W"
    VALUE_2 = "1M"
    VALUE_3 = "1Y"

    def __str__(self) -> str:
        return str(self.value)
