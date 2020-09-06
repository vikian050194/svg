from .shape import Shape

class Ellipse(Shape):
    def __init__(self, cx, cy, rx=1, ry=1):
        super().__init__("ellipse")
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'cx="{self.cx}"',
            f'cy="{self.cy}"',
            f'rx="{self.rx}"',
            f'ry="{self.ry}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'/>'
        ]
        
        return " ".join(lines)


__all__ = ["Ellipse"]
