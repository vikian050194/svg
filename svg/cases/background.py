from typing import List

from svg.shapes import Rectangle, Shape
from svg.cases.abstract import AbstractCase


class BackgroundCase(AbstractCase):
    @property
    def name(self) -> str:
        return "background"

    def draw(self, color: str) -> List[Shape]:
        shapes = []
        
        background = Rectangle(0, 0, "100%", "100%")
        background.fill = color
        shapes.append(background)

        return shapes


__all__ = ["BackgroundCase"]
