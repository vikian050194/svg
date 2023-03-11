from unittest import TestCase, skip
from unittest.mock import patch
from tempfile import TemporaryDirectory

from svg.app import run

@skip("e2e")
@patch("builtins.print")
class TestApp(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.call = lambda: run()

    def tearDown(self):
        self.temp_dir.cleanup()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_argument_is_missed(self, mock_print):
        self.call()
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("ERROR: config file is not provided")
        mock_print.reset_mock()
