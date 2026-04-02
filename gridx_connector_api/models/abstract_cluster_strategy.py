from enum import Enum


class AbstractClusterStrategy(str, Enum):
    AI = "AI"
    EQUALLY = "EQUALLY"
    FIRST_COME_FIRST_SERVE = "FIRST_COME_FIRST_SERVE"
    LAST_COME_FIRST_SERVE = "LAST_COME_FIRST_SERVE"
    PROPORTIONAL = "PROPORTIONAL"
    ROUND_ROBIN = "ROUND_ROBIN"
    SERIES = "SERIES"

    def __str__(self) -> str:
        return str(self.value)
