""" simple rates client """

from unittest import TestCase
from unittest.mock import patch, Mock

from code.simple_rates_client.rates_api_server import rates_api_server


class TestRatesApiServer(TestCase):
    """ TestRatesApiServer """

    @patch("code.simple_rates_client.rates_api_server.start_rates_api")
    @patch("code.simple_rates_client.rates_api_server.requests")
    @patch("code.simple_rates_client.rates_api_server.mp")
    def test_start_rates_api(
        self, mock_mp: Mock, mock_requests: Mock,
        mock_start_rates_api: Mock) -> None:
        """ test_start_rates_api """

        rates_api_server_fn = rates_api_server.__wrapped__

        gen = rates_api_server_fn()

        next(gen)

        mock_mp.Process.assert_called_once_with(target=mock_start_rates_api)
        mock_mp.Process.return_value.start.assert_called_once()
        mock_requests.get.assert_called_once_with(
            "http://127.0.0.1:5000/check")

        next(gen, None)

        mock_mp.Process.return_value.terminate.assert_called_once()
        

    @patch("code.simple_rates_client.rates_api_server.start_rates_api")
    @patch("code.simple_rates_client.rates_api_server.requests")
    @patch("code.simple_rates_client.rates_api_server.mp")
    def test_start_rates_api_conn_error(
            self, mock_mp: Mock, mock_requests: Mock,
            mock_start_rates_api: Mock) -> None:
        """ test_start_rates_api_conn_error """

        mock_requests.get.side_effect = [
            ConnectionError(),
            True
        ]

        rates_api_server_fn = rates_api_server.__wrapped__

        gen = rates_api_server_fn()

        next(gen)

        mock_mp.Process.assert_called_once_with(target=mock_start_rates_api)
        mock_mp.Process.return_value.start.assert_called_once()
        mock_requests.get.assert_called_with("http://127.0.0.1:5000/check")

        next(gen, None)

        mock_mp.Process.return_value.terminate.assert_called_once()
