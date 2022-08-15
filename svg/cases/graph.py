from typing import List

from svg.shapes import Circle, Line, Shape
from svg.cases.abstract import AbstractCase


class GraphCase(AbstractCase):
    @property
    def name(self) -> str:
        return "graph"

    def draw(self, n: int) -> List[Shape]:
        circles = []
        lines = []
        
        stroke = 5
        # h = 10
        # w = h * 2

        fc = self.palette.get_color()
        sc = self.palette.get_color()

        for i in range(0, n):
            x, y = self.rm.get_pair()
            c = Circle(x, y, stroke * 2)
            c.fill = fc
            c.stroke = sc
            c.stroke_width = stroke
            circles.append(c)

        for i in range(0, n):
            c_from = circles[self.rm.next(0, len(circles) - 1)]
            without = list(set(circles) - set([c_from]))
            c_to = without[self.rm.next(0, len(without) - 1)]
            l = Line(c_from.cx, c_from.cy, c_to.cx, c_to.cy)
            l.stroke = fc
            l.stroke_width = 5
            lines.append(l)

        return lines + circles


__all__ = ["GraphCase"]
