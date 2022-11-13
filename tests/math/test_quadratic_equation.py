from unittest import TestCase

from svg.math.quadratic_equation import solve


class TestQuadraticEquation(TestCase):
    def test_no_solutions(self):
        a = 1
        b = 2
        c = 3
        expected = []

        actual = solve(a, b, c)

        self.assertEqual(actual, expected)

    def test_one_solution(self):
        a = 1
        b = 2
        c = 1
        expected = [-1.]

        actual = solve(a, b, c)

        self.assertEqual(actual, expected)

    def test_two_solutions(self):
        a = 5
        b = 6
        c = 1
        expected = [-0.2, -1.]

        actual = solve(a, b, c)

        self.assertEqual(actual, expected)
