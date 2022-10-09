from typing import List

import math
from enum import Enum

from svg.shapes import Polygon, Shape
from svg.cases.abstract import AbstractCase


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
                    d2 = b**2-4*a*c
                    d = math.sqrt(d2) 

                    xc_1 = ((-1)*b+d)/(2*a)
                    xc_2 = ((-1)*b-d)/(2*a)

                    yc_1 = la*xc_1+lb
                    yc_2 = la*xc_2+lb

                    xc = round(xc_1, 2)
                    yc = round(yc_1, 2)

                    pg.append(xa, ya)
                    pg.append(xb, yb)
                    pg.append(xc, yc)

                shapes.append(pg)

            return shapes


__all__ = ["TriangleCase"]
