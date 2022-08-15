from typing import List

from svg.shapes import Polygon, Shape
from svg.cases.abstract import AbstractCase


class TriangleCase(AbstractCase):
    @property
    def name(self) -> str:
        return "triangle"

    def draw(self, count: int, edge: int) -> List[Shape]:
            shapes = []
    
            sc = self.palette.get_color()
            fc = self.palette.get_color()

            for _ in range(0, count):
                pg = Polygon()
                pg.stroke = sc
                pg.stroke_width = 5
                pg.fill = fc
                for _ in range(0, edge):
                    x, y = self.rm.get_pair()
                    pg.append(x, y)
                shapes.append(pg)

            return shapes


__all__ = ["TriangleCase"]
