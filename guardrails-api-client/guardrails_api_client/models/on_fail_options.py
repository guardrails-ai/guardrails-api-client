from enum import Enum


class OnFailOptions(str, Enum):
    EXCEPTION = "exception"
    FILTER = "filter"
    FIX = "fix"
    FIX_REASK = "fix_reask"
    NOOP = "noop"
    REASK = "reask"
    REFRAIN = "refrain"

    def __str__(self) -> str:
        return str(self.value)
