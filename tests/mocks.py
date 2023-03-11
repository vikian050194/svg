from typing import List, Tuple

from svg.colors import Base
from svg.managers.random_manager import AbstractRandomManager


class TestColors(Base):
    COLOR_A = "color_a"
    COLOR_B = "color_b"
    COLOR_C = "color_c"


class TestRandomManager(AbstractRandomManager):
    def __init__(self, values: List[int]):
        self.index = 0
        self.values = values

    def next(self) -> int:
        value = self.values[self.index]
        self.index = self.index + 1
        return value

    def get_x(self) -> int:
        return self.next()

    def get_y(self) -> int:
        return self.next()

    def get_pair(self) -> Tuple[int, int]:
        return self.next(), self.next()

    def get_bool(self) -> bool:
        return self.next() == 0
