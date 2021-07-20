from datetime import date, time, datetime, timedelta

def working_with_date():
    print('Working with date: \n')
    print('---')

    today = date.today()
    print(today)
    print(today.strftime("%d/%m/%Y"))
    print(today.day)
    print(today.month)
    print(today.year)

def working_with_time():
    print('Working with time: \n')
    print('---')

    specific_time = time(hour=12, minute=30, second=45)
    print(specific_time)
    str_time = specific_time.strftime('%Hh%M')
    print(str_time)
    print(specific_time.hour)
    print(specific_time.minute)
    print(specific_time.second)

def working_with_datetime():
    print('Working with datetime: \n')

    now = datetime.now()
    print(now)
    print(now.weekday())
    str_now = now.strftime('%d/%m/%Y %H:%M')
    print(str_now)
    print(now.strftime('%c'))
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)

    specific_time = datetime(year=2019, month=1, day=1, hour=12, minute=30, second=45)
    print(specific_time)

    str_date = '01/02/2003'
    converted_date = datetime.strptime(str_date, '%d/%m/%Y')
    print(converted_date)

def working_with_timedelta():
    print('Working with timedelta: \n')

    today = date.today()
    tomorrow = today + timedelta(days=1)
    plus_one_year = today + timedelta(days=365)

    print(today)
    print(tomorrow)
    print(plus_one_year)


if(__name__ == "__main__"):
    working_with_date()
    print('-------------')
    working_with_time()
    print('-------------')
    working_with_datetime()
    print('-------------')
    working_with_timedelta()