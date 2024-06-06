def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2024):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for day in range(days_in_month.get(month)+1):
        yield day


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def gen_date():
    for year in gen_years(2024):
        for month in gen_months():
            leap_year = is_leap_year(year)
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield "%02d/%02d/%02d %02d:%02d:%02d" % (day, month, year, hour, minute, second)


def main():
    date_gen = gen_date()
    count = 0

    while True:
        date = next(date_gen)
        count += 1
        if count % 1000000 == 0:
            next(date_gen)
            print(date)


if __name__ == "__main__":
    main()
