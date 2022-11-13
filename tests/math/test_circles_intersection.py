from unittest import TestCase

from svg.math.circles_intersection import solve


class TestCirclesIntersection(TestCase):
    def test_no_solutions(self):
        a = (xa, ya, ra) = (0, 0, 1)
        b = (xa, ya, ra) = (2, 2, 16)
        expected = []

        actual = solve(a, b)

        self.assertEqual(actual, expected)

    def test_one_solution(self):
        a = (xa, ya, ra) = (2, 3, 4)
        b = (xa, ya, ra) = (3, 3, 1)
        expected = [(4.0, 3.0)]

        actual = solve(a, b)

        self.assertEqual(actual, expected)

    def test_two_solutions_vertical(self):
        a = (xa, ya, ra) = (2, 2, 1)
        b = (xa, ya, ra) = (2, 3, 2)
        expected = [(3.0, 2.0), (1.0, 2.0)]

        actual = solve(a, b)

        self.assertEqual(actual, expected)

    def test_two_solutions_horizontal(self):
        a = (xa, ya, ra) = (2, 3, 1)
        b = (xa, ya, ra) = (3, 3, 2)
        expected = [(2.0, 4.0), (2.0, 2.0)]

        actual = solve(a, b)

        self.assertEqual(actual, expected)

    def test_two_solutions_common_case(self):
        a = (xa, ya, ra) = (0, 0, 1)
        b = (xa, ya, ra) = (1, 2, 2)
        expected = [(0.8, 0.6), (0.0, 1.0)]

        actual = solve(a, b)

        self.assertEqual(actual, expected)
