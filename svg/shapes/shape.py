from .node import Node

class Shape(Node):
    def __init__(self, name=None, fill="transparent", stroke="black", stroke_width=1):
        super().__init__(name)
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width


__all__ = ["Shape"]
