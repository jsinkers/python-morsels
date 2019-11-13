import datetime as dt

meet_day = 3 # thursday
meet_week = 4


def meetup_date(year, month):
    day = dt.date(year=year, month=month, day=1)
    week = 0
    while day.month == month:
        if day.weekday() == meet_day:
            week += 1

        if week == meet_week:
            break

        day += dt.timedelta(days=1)

    return day


if __name__ == '__main__':
    print(meetup_date(2019, 11))
