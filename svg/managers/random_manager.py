from typing import Tuple

from .abstract_random_manager import AbstractRandomManager


class RandomManager(AbstractRandomManager):
    def __init__(self, next, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.next = next

    def next(self, min: int, max: int) -> int:
        return self.next(min, max)

    def get_x(self) -> int:
        return self.next(0, self.max_x)

    def get_y(self) -> int:
        return self.next(0, self.max_y)

    def get_pair(self) -> Tuple[int, int]:
        return self.next(0, self.max_x), self.next(0, self.max_y)

    def get_bool(self) -> bool:
        return self.next(0, 1) == 0


__all__ = ["RandomManager"]
