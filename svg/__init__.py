import os
from datetime import datetime

from svg.shapes import *
from svg.colors import *


folder = "output"

if not os.path.exists(folder):
    os.makedirs(folder)


def save(svg):
    output = str(svg)
    with open("output.svg", "w") as out_file:
        out_file.write(output)
    with open(folder + "/" + datetime.now().isoformat(sep="T", timespec="seconds") + ".svg", "w") as out_file:
        out_file.write(output)


def main():
    width = 1920
    height = 1080
    dx = width // 2
    dy = height // 2

    palette = Palette(Dell)
    palette.is_random = False

    svg = SVG(width, height)
    
    l = Line(0, 0, dx, dy)
    l.stroke = palette.get_color()
    l.stroke_width = 5
    svg.append(l)
    
    l = Line(dx, dy, width, height)
    l.stroke = palette.get_color()
    l.stroke_width = 5
    svg.append(l)

    c = Circle(dx, dy, 64)
    c.stroke_width = 0
    c.fill = palette.get_color()
    svg.append(c)

    pl = Polyline()
    pl.stroke = palette.get_color()
    pl.stroke_width = 5
    pl.append(50, 50)
    pl.append(100, 50)
    pl.append(100, 100)
    svg.append(pl)

    pg = Polygon()
    pg.stroke = palette.get_color()
    pg.stroke_width = 5
    pg.append(150, 150)
    pg.append(150, 200)
    pg.append(200, 200)
    svg.append(pg)

    color = palette.get_color()
    f = lambda x: 0.02*(x**3)
    for x in range(-dx, dx, 1):
        y = round(dy-round(f(x),2),2)
        if 0<=y<=height:
            c = Circle(x+dx, y, 5)
            c.fill = color
            c.stroke_width = 0
            svg.append(c)

    p = Path()
    p.stroke = palette.get_color()
    p.stroke_width = 5

    move = MoveTo(dx, dy)
    move.name = "M"
    p.d.append(move)

    # p.d.append(HorizontalLine(100))
    # p.d.append(VerticalLine(100))
    # p.d.append(HorizontalLine(-100))
    # p.d.append(VerticalLine(-100))
    p.d.append(MoveTo(100, 100))
    p.d.append(LineTo(300, 250))
    p.d.append(LineTo(150, 100))
    p.d.append(ClosePath())

    svg.append(p)

    print(svg)
    save(svg)
