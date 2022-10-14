""" Test Patterns Module """

from unittest import TestCase
from unittest.mock import patch, Mock

from code.ut_app.patterns import action_a, action_b, console_log


class TestPatterns(TestCase):
    """ Test Patterns Class """

    @patch("code.ut_app.patterns.console_log")
    def test_action_a(self, mock_console_log: Mock) -> None:
        """ test_action_a """

        action_a()
        mock_console_log.assert_called_once_with("action a")

    def test_action_a_alt(self) -> None:
        """ test_action_a_alt """

        with patch(
            "code.ut_app.patterns.console_log") as mock_console_log:
            action_a()
            mock_console_log.assert_called_once_with("action a")

    def test_action_b(self) -> None:
        """ test_action_b """

        # arrange
        mock_log = Mock()

        # act

        action_b(mock_log)

        # assert
        mock_log.assert_called_once_with("action b")


    @patch("code.ut_app.patterns.print")
    def test_console_log(self, mock_print: Mock) -> None:
        """ test_console_log """

        console_log("test")
        mock_print.assert_called_once_with("test")
