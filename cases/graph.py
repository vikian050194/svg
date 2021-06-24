from svg.shapes import Circle, Line

from .common import *

def graph():
    circles = []
    lines = []
    
    n = 25
    stroke = 5
    # h = 10
    # w = h * 2

    points = []

    fc = palette.get_color()
    sc = palette.get_color()

    for i in range(0, n):
        c = Circle(r_x(), r_y(), stroke * 2)
        c.fill = fc
        c.stroke_width = 0
        circles.append(c)

    for i in range(0, n):
        c_from = circles[randint(0, len(circles) - 1)]
        without = list(set(circles) - set([c_from]))
        c_to = without[randint(0, len(without) - 1)]
        l = Line(c_from.cx, c_from.cy, c_to.cx, c_to.cy)
        l.stroke = fc
        l.stroke_width = 5
        lines.append(l)

    return circles + lines
