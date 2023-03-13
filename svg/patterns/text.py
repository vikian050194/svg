from typing import List

from svg.shapes import Text, Shape
from svg.patterns.abstract import AbstractPattern


class TextPattern(AbstractPattern):
    @property
    def name(self) -> str:
        return "text"

    @property
    def overridable(self) -> List[str]:
        return []

    def draw(self, size:int, value: str) -> List[Shape]:
        shapes = []
        
        sc = self.palette.get_color()
        fc = self.palette.get_color()
        sc = "white"
        x, y = self.rm.get_pair()

        text = Text(x, y, size, value)
        text.fill = fc
        text.stroke = sc
        text.stroke_width = 0
        shapes.append(text)

        return shapes


__all__ = ["TextPattern"]
