from enum import Enum
from unittest import TestCase

from svg.get_color import get_colors


class TestGetColor(TestCase):
    def test_get_color(self):
        colors = get_colors("google")

        self.assertIsNotNone(colors)
