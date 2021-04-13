from datetime import date, time, timedelta, datetime


april_fools_2021 = date(year=2021, month=4, day=1)
noon = time(hour=12, minute=0, second=0)
midnite = time(hour=0, minute=0, second=0)

print(f"april fool's day is: {april_fools_2021}")
print(f"noon == {noon}")
print(f"midnight == {midnite}")

# working with dates
todays_date = date.today()
todays_date_w_time = datetime.today()
print(f"today: {todays_date}")
print(f"today w/ time: {todays_date_w_time}")

now = datetime.now()
print(f'now: {now}')

current_time = time(now.hour, now.minute, now.second)
print(f'current time: {current_time}')
datetime.combine(todays_date, current_time)

# working with datetime and strings
date_from_str = date.fromisoformat("2021-04-12")
print(date_from_str)

date_string = "04-12-2021 12:45:55"
date_fmt = "%m-%d-%Y %H:%M:%S"
dt = datetime.strptime(date_string, date_fmt)
print(dt)

# timedelta
days_since_new_year = todays_date - date.fromisoformat("2021-01-01")
print(f"days since new year 2021: {days_since_new_year}")

# the following would fail because you cannot do arithmetic
# with 'datetime.date' and 'datetime.datetime' objects
# date.fromisoformat("2021-12-31") - todays_date
# todays_date - now

# Arithmetic with datetime
yesterday = timedelta(days=-1)
print(f"yesterday is {yesterday} away")
print(f"yesterday was: {now + yesterday}")
