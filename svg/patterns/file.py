from typing import List

from svg.shapes import Shape
from svg.patterns.abstract import AbstractPattern


files = [
    '<circle cx="1768" cy="583" r="64" fill="{{fill}}" stroke="#D0D3D6" stroke-width="5" transform="translate({{x}},{{y}}) scale({{scale}})"/>'
]


class FilePattern(AbstractPattern):
    @property
    def name(self) -> str:
        return "file"

    @property
    def overridable(self) -> List[str]:
        return []

    def draw(self, count: int) -> List[Shape]:
        shapes = []
        c = self.palette.get_color()
        for _ in range(0, count):
            file = files[self.rm.next(0, len(files) - 1)]
            # c = self.palette.get_color()
            file = file.replace("{{fill}}", c)
            x, y = self.rm.get_pair()
            file = file.replace("{{x}}", str(x))
            file = file.replace("{{y}}", str(y))
            # rotate = self.rm.next(0, 359)
            # file = file.replace("{{rotate}}", str(rotate))
            # scale = self.rm.next(1, 5)
            scale = self.rm.next(10, 30)
            scale = round((0 + scale)/100, 2)
            file = file.replace("{{scale}}", str(scale))
            shapes.append(file)

        return shapes


__all__ = ["FilePattern"]
