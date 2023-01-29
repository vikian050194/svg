from unittest import TestCase

from typing import List, Tuple

from svg.patterns import CirclePattern
from svg.colors import Base
from svg.palette import Order, Palette
from svg.managers.random_manager import AbstractRandomManager
from svg.shapes.circle import Circle


class TestColors(Base):
    COLOR_A = "color_a"
    COLOR_B = "color_b"
    COLOR_C = "color_c"


class TestRandomManager(AbstractRandomManager):
    def __init__(self, values: List[int]):
        self.index = 0
        self.values = values

    def next(self) -> int:
        value = self.values[self.index]
        self.index = self.index + 1
        return value

    def get_x(self) -> int:
        return self.next()

    def get_y(self) -> int:
        return self.next()

    def get_pair(self) -> Tuple[int, int]:
        return self.next(), self.next()

    def get_bool(self) -> bool:
        return self.next() == 0


class TestCirclePattern(TestCase):
    def test_no_shapes(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = []
        random = TestRandomManager(values=random_values)
        pattern = CirclePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)

        # Act
        shapes = pattern.draw(0, 10)

        # Assert
        self.assertEqual(len(shapes), 0)

    def test_one_shape(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = [33, 42]
        random = TestRandomManager(values=random_values)
        pattern = CirclePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)

        # Act
        shapes = pattern.draw(1, 10)

        # Assert
        self.assertEqual(len(shapes), 1)
        self.assertIsInstance(shapes[0], Circle)
        self.assertEqual(shapes[0].cx, 33)
        self.assertEqual(shapes[0].cy, 42)
        self.assertEqual(shapes[0].r, 10)
        self.assertEqual(shapes[0].stroke_width, 5)
        self.assertEqual(shapes[0].stroke, TestColors.COLOR_A.value)
        self.assertEqual(shapes[0].fill, TestColors.COLOR_B.value)

    def test_three_shapes(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = list(range(0, 6))
        random = TestRandomManager(values=random_values)
        pattern = CirclePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)

        # Act
        shapes = pattern.draw(3, 10)

        # Assert
        self.assertEqual(len(shapes), 3)
        for shape in shapes:
            self.assertIsInstance(shape, Circle)
            self.assertEqual(shapes[0].r, 10)
