from unittest import TestCase
from unittest.mock import patch
from tempfile import TemporaryDirectory

import os

from svg.main import main
from svg.configuration import Configuration

# @skip("e2e")
@patch("builtins.print")
class TestMain(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        # TODO fix history dir hack
        os.makedirs(self.temp_dir.name + "/history")
        home=self.temp_dir.name
        width=1000
        height=1000
        palettes=["test"]
        order="forward"
        patterns=[
            {
                "name": "background",
                "fill": "white"
            },
            {
                "name": "grid",
                "count": 1
            }
        ]
        print_result=True
        write_results=True
        self.call = lambda home=home, width=width, height=height, palettes=palettes, order=order, patterns=patterns, print_result=print_result, write_results=write_results: main(config=Configuration(home, width, height, palettes, order, patterns, print_result, write_results))

    def tearDown(self):
        self.temp_dir.cleanup()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_background_and_grid(self, mock_print):
        self.call()
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        [first_call] = mock_print.call_args_list
        arguments = first_call[0]
        value=arguments[0]
        self.assertIn("rect", value)
        self.assertIn("line", value)
        self.assertIn("black", value)
        self.assertIn("white", value)
        self.assertIn("green", value)
        self.assertNotIn("red", value)
        mock_print.reset_mock()

    def test_custom_fill_and_stroke(self, mock_print):
        patterns = [
            {
                "name": "circle",
                "count": 1,
                "radius": 10,
                "fill": "#111111",
                "stroke": "#222222"
            }
        ]
        self.call(patterns=patterns)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        [first_call] = mock_print.call_args_list
        arguments = first_call[0]
        value=arguments[0]
        self.assertIn("circle", value)
        self.assertIn("#111111", value)
        self.assertIn("#222222", value)
        mock_print.reset_mock()
