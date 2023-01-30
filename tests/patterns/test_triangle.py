from unittest import TestCase

from svg.patterns import TrianglePattern
from svg.patterns.triangle import Type
from svg.palette import Order, Palette
from svg.shapes import Polygon, Point
from tests.mocks import TestColors, TestRandomManager


class TestTrianglePattern(TestCase):
    def test_no_shapes(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = []
        random = TestRandomManager(values=random_values)
        pattern = TrianglePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)

        # Act
        shapes = pattern.draw(0, None)

        # Assert
        self.assertEqual(len(shapes), 0)

    def test_one_shape(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = list(range(0, 6))
        random = TestRandomManager(values=random_values)
        pattern = TrianglePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)
        polygon = Polygon()
        polygon.points = [Point(0, 1), Point(2, 3), Point(4, 5)]
        polygon.stroke = TestColors.COLOR_A.value
        polygon.fill = TestColors.COLOR_B.value
        polygon.stroke_width = 5
        expected = [polygon]

        # Act
        shapes = pattern.draw(1, Type.RANDOM)

        # Assert
        self.assertEqual(len(shapes), 1)
        self.assertIsInstance(shapes[0], Polygon)
        self.assertEqual(shapes, expected)

    def test_three_shapes(self):
        # Arrange
        palette = Palette(TestColors, Order.FORWARD, None)
        random_values = list(range(0, 18))
        random = TestRandomManager(values=random_values)
        pattern = TrianglePattern(
            palette=palette,
            width=1920,
            height=1080,
            rm=random)

        # Act
        shapes = pattern.draw(3, Type.RANDOM)

        # Assert
        self.assertEqual(len(shapes), 3)
        for shape in shapes:
            self.assertIsInstance(shape, Polygon)
