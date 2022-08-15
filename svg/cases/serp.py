from typing import List

from svg.shapes import Line, Shape
from svg.cases.abstract import AbstractCase


class SerpCase(AbstractCase):
    @property
    def name(self) -> str:
        return "serp"

    def draw(self, count: int) -> List[Shape]:
            shapes = []

            sc = self.palette.get_color()
            self._color = sc
            self._stroke_width = 2

            self._recF(shapes, self.width // 2, 1, self.width - 1, self.height - 1, 1, self.height - 1, count)
            return shapes

    def _recF (self, e, xa, ya, xb, yb, xc, yc, i):
        if i == 0:
            l = Line(xa, ya, xc, yc)
            l.stroke = self._color
            l.stroke_width = self._stroke_width
            e.append(l)
            l = Line(xa, ya, xb, yb)
            l.stroke = self._color
            l.stroke_width = self._stroke_width
            e.append(l)
            l = Line(xb, yb, xc, yc)
            l.stroke = self._color
            l.stroke_width = self._stroke_width
            e.append(l)
        else:
            prevXA = xa
            prevYA = ya 
            prevXB = xb
            prevYB = yb 
            prevXC = xc
            prevYC = yc 
            nextxa = (prevXA + prevXC)/2
            nextya = (prevYA + prevYC)/2    
            nextxb = (prevXB + prevXA)/2
            nextyb = (prevYB + prevYA)/2    
            nextxc = (prevXC + prevXB)/2
            nextyc = (prevYC + prevYB)/2    
            
            self._recF(e, prevXA, prevYA, nextxa, nextya, nextxb, nextyb, i - 1);
            self._recF(e, nextxa, nextya, nextxc, nextyc, prevXC, prevYC, i - 1);
            self._recF(e, nextxb, nextyb, prevXB, prevYB, nextxc, nextyc, i - 1);


__all__ = ["SerpCase"]
