from unittest import TestCase

from svg.colors import Base
from svg.palette import Order
from svg import Palette


class TestColors(Base):
    COLOR_A = "color_a"
    COLOR_B = "color_b"
    COLOR_C = "color_c"


class TestPalette(TestCase):
    def test_get_color_forward(self):
        palette = Palette(TestColors, Order.FORWARD)

        self.assertEqual(palette.get_color(), "color_a")
        self.assertEqual(palette.get_color(), "color_b")
        self.assertEqual(palette.get_color(), "color_c")
        self.assertEqual(palette.get_color(), "color_a")
