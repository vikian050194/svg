from random import randint

from svg.cases import *
from svg.configuration import Configuration
from svg.get_color import get_colors
from svg.palette import Palette
from svg.shapes import *
from svg.colors import *
from svg.managers import *


def main(config: Configuration):
    palette_colors = get_colors(config.palette)
    palette = Palette(palette_colors, config.order)

    rm = RandomManager(randint, config.width, config.height)
    tm = TimeManager()
    fom = FileOutputManager(tm, config)
    tom = TerminalOutputManager(config)

    cases = [
        BackgroundCase,
        GridCase,
        CircleCase,
        TriangleCase,
        GraphCase,
        SerpCase,
    ]


    cc = {}
    for c in cases:
        ci = c(palette, config.width, config.height, rm)
        cc[ci.name] = ci.draw

    svg = SVG(config.width, config.height)

    for pattern in config.patterns:
        draw = cc[pattern["name"]]
        del pattern["name"]
        shapes = draw(**pattern)

        for shape in shapes:
            svg.append(shape)

    output = str(svg)
    tom.save(output)
    fom.save(output)
