from enum import Enum, unique


@unique
class Base(str, Enum):
    pass

__all__ = ["Base"]
