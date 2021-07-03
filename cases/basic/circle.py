from svg.shapes import Circle

from ..common import *

def circle():
    shapes = []
    
    n = 50

    sc = palette.get_color()
    fc = palette.get_color()

    for i in range(0, n):
        c = Circle(r_x(), r_y(), 64)
        c.stroke = sc
        c.stroke_width = 5
        c.fill = fc
        shapes.append(c)

    return shapes


__all__ = ["circle"]
