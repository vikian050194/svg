from unittest import TestCase

from svg.patterns import CirclePattern
from svg.palette import Order, Palette
from svg.shapes import Circle

from tests.mocks import TestColors, TestRandomManager


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
        circle = Circle(33, 42, 10)
        circle.stroke = TestColors.COLOR_A.value
        circle.fill = TestColors.COLOR_B.value
        circle.stroke_width = 5
        expected = [circle]

        # Act
        shapes = pattern.draw(1, 10)

        # Assert
        self.assertEqual(len(shapes), 1)
        self.assertIsInstance(shapes[0], Circle)
        self.assertEqual(shapes, expected)

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
