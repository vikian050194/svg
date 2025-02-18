from .node import Node


class SVG(Node):
    def __init__(self, width, height):
        super().__init__("svg")
        self.width = width
        self.height = height
        self.shapes = []

    def append(self, shape):
        self.shapes.append(shape)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            f'<{self.name} version="1.1" xmlns="http://www.w3.org/2000/svg" '
            f'width="{self.width}" '
            f'height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}"> '
            f'{"".join(map(str, self.shapes))}'
            f'</{self.name}>'
        )


__all__ = ["SVG"]
