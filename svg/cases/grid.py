from typing import List

from svg.shapes import Line, Shape
from svg.cases.abstract import AbstractCase


class GridCase(AbstractCase):
    @property
    def name(self) -> str:
        return "grid"

    def draw(self, count: int) -> List[Shape]:
        shapes = []

        dx = self.width // count
        dy = self.height // count
        cc = self.palette.get_color()

        l = Line(dx, 0, dx, self.height)
        l.stroke = cc
        l.stroke_width = 2
        shapes.append(l)

        l = Line(0, dy, self.width, dy)
        l.stroke = cc
        l.stroke_width = 2
        shapes.append(l)

        return shapes


__all__ = ["GridCase"]
