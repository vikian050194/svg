from .shape import Shape
from .node import *

class Command(Node):
    def __init__(self):
        super().__init__(None)
        self.relative = True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name if self.relative else self.name.upper()


class MoveTo(Command):
    def __init__(self, x, y):
        super().__init__()
        self.name = "m"
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name} {self.x} {self.y}"


class LineTo(MoveTo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "l"


class CommandLine(Command):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __repr__(self):
        return f"{self.name} {self.value}"


class HorizontalLine(CommandLine):
    def __init__(self, value):
        super().__init__(value)
        self.name = "h"


class VerticalLine(CommandLine):
    def __init__(self, value):
        super().__init__(value)
        self.name = "v"


class ClosePath(Command):
    def __init__(self):
        super().__init__()
        self.name = "z"


class Path(Shape):
    def __init__(self):
        super().__init__("path")
        self.d = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'd="{" ".join(map(str,self.d))}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'/>'
        ]

        return " ".join(lines)
        

# __all__ = ["Path"]
