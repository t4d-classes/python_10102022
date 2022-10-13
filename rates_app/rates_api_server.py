""" rates api server """

from contextlib import contextmanager
from collections.abc import Generator
import multiprocessing as mp

import requests
from requests.exceptions import RequestException

from rates_api import start_rates_api

@contextmanager
def rates_api_server() -> Generator[None,None,None]:
    """ rates api server """

    print("start server")
    rates_api_process = mp.Process(target=start_rates_api)
    rates_api_process.start()

    while True:

        try:
            requests.get("http://127.0.0.1:5050/check")
            break
        except ConnectionError:
            continue
        except RequestException:
            continue

    yield

    rates_api_process.terminate()
    print("end server")
