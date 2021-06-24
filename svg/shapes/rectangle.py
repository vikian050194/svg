from .shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__("rect")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lines = [
            f'<{self.name}',
            f'x="{self.x}"',
            f'y="{self.y}"',
            f'width="{self.width}"',
            f'height="{self.height}"',
            f'fill="{self.fill}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"',
            f'/>'
        ]

        return " ".join(lines)


__all__ = ["Rectangle"]
