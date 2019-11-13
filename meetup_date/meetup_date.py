import datetime as dt


def meetup_date(year, month, nth=4, weekday=3):
    if nth > 0:
        day = dt.date(year=year, month=month, day=1)
    elif nth < 0:
        day = dt.date(year=year, month=month+1, day=1) - dt.timedelta(days=1)

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
