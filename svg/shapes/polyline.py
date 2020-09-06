from .shape import Shape 

class Polyline(Shape):
    def __init__(self):
        super().__init__("polyline")
        self.points = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'points="{" ".join(map(str,self.points))}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'/>'
        ]

        return " ".join(lines)


__all__ = ["Polyline"]
