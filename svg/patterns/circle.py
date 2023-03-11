from typing import List, Optional

from svg.shapes import Circle, Shape
from svg.patterns.abstract import AbstractPattern


class CirclePattern(AbstractPattern):
    @property
    def name(self) -> str:
        return "circle"

    @property
    def overridable(self) -> List[str]:
        return ["fill", "stroke"]

    def draw(self, count: int, radius: int) -> List[Shape]:
        shapes = []
        
        sc = self.palette.get_color()
        fc = self.palette.get_color()

        for _ in range(0, count):
            x, y = self.rm.get_pair()
            c = Circle(x, y, radius)
            c.stroke = sc
            c.stroke_width = 5
            c.fill = fc
            shapes.append(c)

        return shapes


__all__ = ["CirclePattern"]
