""" rates app """

import time
from datetime import date
from multiprocessing import freeze_support


from rates_api_server import rates_api_server
from rates_demo import get_rates_threadpool


if __name__ == '__main__':

    freeze_support()

    with rates_api_server():

        start = time.time()

        rates_data = get_rates_threadpool(date(2020, 8, 1), date(2020, 8, 20))

        for rate_data in rates_data:
            print(rate_data)

        end = time.time()

        print(f"elapsed: {end - start}")
