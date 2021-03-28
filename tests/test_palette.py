from enum import Enum
from unittest import TestCase

from svg.colors import Palette


class TestColors(str, Enum):
    COLOR_A = "color_a"
    COLOR_B = "color_b"
    COLOR_C = "color_c"


class TestPalette(TestCase):
    def test_get_next_color(self):
        palette = Palette(TestColors)

        self.assertEqual(palette.get_next_color(), "color_a")
        self.assertEqual(palette.get_next_color(), "color_b")
        self.assertEqual(palette.get_next_color(), "color_c")
        self.assertEqual(palette.get_next_color(), "color_a")
