from .node import Node


class Shape(Node):
    def __init__(self, name: str = None, fill: str = "transparent", stroke: str = "black", stroke_width: int = 1):
        super().__init__(name)
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width


__all__ = ["Shape"]
