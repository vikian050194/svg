from typing import List

from svg.shapes import Rectangle, Shape
from svg.patterns.abstract import AbstractPattern


class BackgroundPattern(AbstractPattern):
    @property
    def name(self) -> str:
        return "background"

    @property
    def overridable(self) -> List[str]:
        return ["fill"]

    def draw(self) -> List[Shape]:
        shapes = []
        
        fill = self.palette.get_color()

        background = Rectangle(0, 0, "100%", "100%")
        background.fill = fill
        shapes.append(background)

        return shapes


__all__ = ["BackgroundPattern"]
