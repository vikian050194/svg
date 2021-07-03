from svg.shapes import Polygon

from ..common import *

def triangle():
    shapes = []
    
    n = 3
    k = 3

    sc = palette.get_color()
    fc = palette.get_color()

    for i in range(0, n):
        pg = Polygon()
        pg.stroke = sc
        pg.stroke_width = 5
        pg.fill = fc
        for j in range(0, k):
            pg.append(r_x(), r_y())
        shapes.append(pg)

    return shapes


__all__ = ["triangle"]
