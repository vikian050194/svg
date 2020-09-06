from .shape import Shape

class Circle(Shape):
    def __init__(self, cx, cy, r=1):
        super().__init__("circle")
        self.cx = cx
        self.cy = cy
        self.r = r

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'cx="{self.cx}"',
            f'cy="{self.cy}"',
            f'r="{self.r}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'/>'
        ]
        
        return " ".join(lines)


__all__ = ["Circle"]
