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

    @abc.abstractmethod
    def get_bool(self) -> bool:
        raise NotImplementedError()


__all__ = ["AbstractRandomManager"]
