from .shape import Shape


class Text(Shape):
    def __init__(self, x: int, y: int, size: int, value: str):
        super().__init__("text")
        self.x = x
        self.y = y
        self.size = size
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'x="{self.x}"',
            f'y="{self.y}"',
            f'font-size="{self.size}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'text-anchor="middle"',
            f'dominant-baseline="middle"',
            f'>',
            self.value,
            f'</{self.name}>',
        ]
        
        return " ".join(lines)


__all__ = ["Text"]
