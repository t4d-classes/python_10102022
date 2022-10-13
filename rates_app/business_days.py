""" business days module """

from collections.abc import Generator
from typing import Any, cast
from datetime import date, timedelta
import holidays

# class Holidays:
#     """ holidays class """

#     def UnitedStates(self) -> list[date]:
#         """ united states holiday date list"""
#         return []

def business_days(start_date: date, end_date: date) -> list[date]:
    """ business days """

    us_holidays = cast(list[date], cast(Any, holidays).UnitedStates())

    days: list[date] = []

    for day in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days

def business_days_gen(
    start_date: date, end_date: date) -> Generator[date,None,None]:
    """ business days """

    us_holidays = cast(list[date], cast(Any, holidays).UnitedStates())

    for day in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date


# for business_day in business_days_gen(date(2022, 6, 3), date(2022, 7, 5)):
#     print(business_day)
    