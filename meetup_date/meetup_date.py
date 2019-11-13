import datetime as dt
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    if nth > 0:
        # first day of month
        day = dt.date(year=year, month=month, day=1)
    elif nth < 0:
        # last day of month
        day = dt.date(year=year, month=month+1, day=1) - dt.timedelta(days=1)

    # determine if we are counting forwards or backwards
    sign = nth/abs(nth)

    week = 0
    while day.month == month:
        if day.weekday() == weekday:
            week += 1*sign

        if week == nth:
            break

        day += dt.timedelta(days=1*sign)

    return day


if __name__ == '__main__':
    print(meetup_date(2019, 11))
    print(Weekday.MONDAY)
