from unittest import TestCase

from svg.calc import quadratic_equation


class TestQuadraticEquation(TestCase):
    def test_no_solutions(self):
        a = 1
        b = 2
        c = 3
        expected = []

        actual = quadratic_equation(a, b, c)

        self.assertEqual(actual, expected)

    def test_one_solution(self):
        a = 1
        b = 2
        c = 1
        expected = [-1.]

        actual = quadratic_equation(a, b, c)

        self.assertEqual(actual, expected)

    def test_two_solutions(self):
        a = 5
        b = 6
        c = 1
        expected = [-0.2, -1.]

        actual = quadratic_equation(a, b, c)

        self.assertEqual(actual, expected)
