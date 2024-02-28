from enum import Enum


class RailSpecVersion(str, Enum):
    VALUE_0 = "0.1"

    def __str__(self) -> str:
        return str(self.value)
