""" rates demo """

from datetime import date
from concurrent.futures import ThreadPoolExecutor
import time

import requests

from business_days import business_days

def get_rates(start_date: date, end_date: date) -> list[str]:
    """ get rates """

    rate_responses: list[str] = []

    currency_symbols = ['USD', 'CAD', 'GBP']

    for business_day in business_days(start_date, end_date):

        rate_url = "".join([
            "http://127.0.0.1:5050/api/",
            str(business_day),
            "?base=INR&symbols=",
            ",".join(currency_symbols)
        ])

        response = requests.get(rate_url, timeout=60)
        rate_responses.append(response.text)

    return rate_responses

def get_rate_task(business_day: date) -> str:
    """ get rate task method """

    currency_symbols = ['USD', 'CAD', 'GBP']

    rate_url = "".join([
        "http://127.0.0.1:5050/api/",
        str(business_day),
        "?base=INR&symbols=",
        ",".join(currency_symbols)
    ])

    response = requests.get(rate_url, timeout=60)
    return response.text


def get_rates_threadpool(start_date: date, end_date: date) -> list[str]:
    """ get rates """

    rate_responses: list[str] = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        rate_responses = list(executor.map(
            get_rate_task,
            [
                business_day
                for business_day in business_days(start_date, end_date)
            ]
        ))

    return rate_responses


