from svg.shapes import *


def point_eq(self, other: Point):
    return self.x == other.x and self.y == other.y


setattr(Point, "__eq__", point_eq)


def point_cr(self, other: Circle):
    result = self.cx == other.cx and self.cy == other.cy
    result = result and self.r == other.r
    result = result and self.fill == other.fill and self.stroke == other.stroke
    result = result and self.stroke_width == other.stroke_width
    return result


setattr(Circle, "__eq__", point_cr)


def point_pl(self, other: Polygon):
    result = self.points == other.points
    result = result and self.fill == other.fill and self.stroke == other.stroke
    result = result and self.stroke_width == other.stroke_width
    return result

setattr(Polygon, "__eq__", point_pl)
