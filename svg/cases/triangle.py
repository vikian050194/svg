from typing import List

import math
from enum import Enum

from svg.shapes import Polygon, Shape
from svg.cases.abstract import AbstractCase
from svg.math import quadratic_equation


class Type(str, Enum):
    RANDOM = "random"
    EQUILATERAL = "equilateral"


class TriangleCase(AbstractCase):
    @property
    def name(self) -> str:
        return "triangle"

    def draw(self, count: int, type: Type) -> List[Shape]:
            edge = 3
            shapes = []
    
            sc = self.palette.get_color()
            fc = self.palette.get_color()

            for _ in range(0, count):
                pg = Polygon()
                pg.stroke = sc
                pg.stroke_width = 5
                pg.fill = fc
                if type == Type.RANDOM:
                    for _ in range(0, edge):
                        x, y = self.rm.get_pair()
                        pg.append(x, y)
                if type == Type.EQUILATERAL:
                    xa, ya = self.rm.get_pair()
                    xb, yb = self.rm.get_pair()
                    r2 = ((xa-xb)**2)+((ya-yb)**2)
                    r = math.sqrt(r2)

                    la = (xb-xa)/(ya-yb)
                    lb = (xa**2+ya**2-xb**2-yb**2)/(2*(ya-yb))
                    a = 1 + la**2
                    b = 2*la*(lb-ya)-2*xa
                    c = xa**2+(lb-ya)**2-r2
                    
                    xcs = quadratic_equation.solve(a, b, c)

                    x = xcs[self.rm.next(0, 1)]

                    y = la*x+lb

                    xc = round(x, 2)
                    yc = round(y, 2)

                    pg.append(xa, ya)
                    pg.append(xb, yb)
                    pg.append(xc, yc)

                shapes.append(pg)

            return shapes


__all__ = ["TriangleCase"]
