import datetime as dt


def meetup_date(year, month, nth=4, weekday=3):
    day = dt.date(year=year, month=month, day=1)
    week = 0
    while day.month == month:
        if day.weekday() == weekday:
            week += 1

        if week == nth:
            break

        day += dt.timedelta(days=1)

    return day


if __name__ == '__main__':
    print(meetup_date(2019, 11))
