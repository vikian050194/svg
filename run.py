#!/usr/bin/env python3

from svg.shapes import *
from svg.utils import *

def save(svg):
    with open("output.svg", "w") as out_file:
        out_file.write(str(svg))


def main():
    width = 1920
    height = 1080
    dx = width // 2
    dy = height // 2

    svg = SVG(width, height)
    
    l = Line(0, 0, dx, dy)
    l.stroke = get_random_color()
    l.stroke_width = 5
    svg.add(l)
    
    l = Line(dx, dy, width, height)
    l.stroke = get_random_color()
    l.stroke_width = 5
    svg.add(l)

    c = Circle(dx, dy, 64)
    c.stroke_width = 0
    c.fill = get_random_color()
    svg.add(c)

    pl = Polyline()
    pl.stroke = get_random_color()
    pl.stroke_width = 5
    pl.points.append(Point(50, 50))
    pl.points.append(Point(100, 50))
    pl.points.append(Point(100, 100))
    svg.add(pl)

    pg = Polygon()
    pg.stroke = get_random_color()
    pg.stroke_width = 5
    pg.points.append(Point(150, 150))
    pg.points.append(Point(150, 200))
    pg.points.append(Point(200, 200))
    svg.add(pg)

    color = get_random_color()
    f = lambda x: 0.02*(x**3)
    for x in range(-dx, dx, 1):
        y = round(dy-round(f(x),2),2)
        if 0<=y<=height:
            c = Circle(x+dx, y, 5)
            c.fill = color
            c.stroke_width = 0
            svg.add(c)

    print(svg)
    save(svg)


if __name__ == "__main__":
    main()
