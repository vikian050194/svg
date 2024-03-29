from typing import List

from svg.shapes import Line, Shape
from svg.patterns.abstract import AbstractPattern


class GridPattern(AbstractPattern):
    @property
    def name(self) -> str:
        return "grid"

    @property
    def overridable(self) -> List[str]:
        return ["stroke"]

    def draw(self, count: int) -> List[Shape]:
        shapes = []

        parts_count = count + 1

        dx = self.width // parts_count
        dy = self.height // parts_count
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


__all__ = ["GridPattern"]
