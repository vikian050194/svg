from random import randint

from svg.patterns import *
from svg.patterns.abstract import AbstractPattern
from svg.configuration import Configuration
from svg.get_color import get_colors
from svg.palette import Palette
from svg.shapes import *
from svg.colors import *
from svg.managers import *


def main(config: Configuration):
    rm = RandomManager(randint, config.width, config.height)
    tm = TimeManager()

    palette_colors = get_colors(config.palette)
    palette = Palette(palette_colors, config.order, rm)

    patterns = [
        BackgroundPattern,
        GridPattern,
        CirclePattern,
        TrianglePattern,
        GraphPattern,
        SerpPattern,
    ]

    pp = {}
    for p in patterns:
        pi = p(palette, config.width, config.height, rm)
        pp[pi.name] = pi

    svg = SVG(config.width, config.height)

    for pattern in config.patterns:
        pi: AbstractPattern = pp[pattern["name"]]
        del pattern["name"]
        override = {}

        for key in pi.overridable:
            if key in pattern:
                override[key] = pattern[key]
                del pattern[key]

        shapes = pi.draw(**pattern)

        for shape in shapes:
            for key in override:
                setattr(shape, key, override[key])

        for shape in shapes:
            svg.append(shape)

    output = str(svg)

    if config.write:
        fom = FileOutputManager(tm, config)
        fom.save(output)

    if config.print:
        tom = TerminalOutputManager(config)
        tom.save(output)
