import abc
from typing import Tuple


class AbstractRandomManager(abc.ABC):
    @abc.abstractmethod
    def next(self, min: int, max: int) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_x(self) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_y(self) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_pair(self) -> Tuple[int, int]:
        raise NotImplementedError()


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


__all__ = ["RandomManager"]
