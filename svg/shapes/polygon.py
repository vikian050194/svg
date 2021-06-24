from .polyline import Polyline


class Polygon(Polyline):
    def __init__(self):
        super().__init__()
        self.name = "polygon"


__all__ = ["Polygon"]
