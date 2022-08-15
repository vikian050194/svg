from typing import List

import abc

from svg.shapes import Shape
from svg.palette import Palette
from svg.managers.random_manager import AbstractRandomManager


class AbstractCase(abc.ABC):
    def __init__(self, palette: Palette, width: int, height: int, rm: AbstractRandomManager):
        self.palette = palette
        self.width = width
        self.height = height
        self.rm = rm

    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def draw(self) -> List[Shape]:
        raise NotImplementedError()


__all__ = ["AbstractCase"]
