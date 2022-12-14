""" rates api server """

from contextlib import contextmanager
from collections.abc import Generator
import multiprocessing as mp

import requests
from requests.exceptions import RequestException

from code.simple_rates_api.rates_api import start_rates_api


@contextmanager
def rates_api_server() -> Generator[None, None, None]:
    """ rates api server """

    # start "with" statement

    rates_api_process = mp.Process(target=start_rates_api)
    rates_api_process.start()

    while True:

        try:
            requests.get("http://127.0.0.1:5000/check")
            break
        except ConnectionError:
            continue
        except RequestException:
            continue

    # enter "with" statement code block

    yield

    # exit "with" statement code block

    rates_api_process.terminate()


class RatesApiServer:

    def __enter__(self) -> None:

        self.rates_api_process = mp.Process(target=start_rates_api)
        self.rates_api_process.start()

        while True:

            try:
                requests.get("http://127.0.0.1:5000/check")
                break
            except ConnectionError:
                continue
            except RequestException:
                continue

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:

        self.rates_api_process.terminate()
