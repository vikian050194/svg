import os
from datetime import datetime
from random import randint

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


width = 1920
height = 1080
dx = width // 2
dy = height // 2


def r_y():
    return randint(0, height)


def r_x():
    return randint(0, width)


palette = Palette(Gravit)
palette.is_random = False


def get_palette():
    global palette
    return palette


def main(get_specific_shapes):
    svg = SVG(width, height)

    cc = palette.get_color()

    l = Line(dx, 0, dx, height)
    l.stroke = cc
    l.stroke_width = 2
    svg.append(l)

    l = Line(0, dy, width, dy)
    l.stroke = cc
    l.stroke_width = 2
    svg.append(l)

    elements = get_specific_shapes()
    for element in elements:
        svg.append(element)

    print(svg)
    save(svg)


# __all__ = ["main"]
