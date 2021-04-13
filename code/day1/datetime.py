from datetime import date, time, datetime

april_fools_2021 = date(year=2021, month=4, day=1)
noon = time(hour=12, minute=0, second=0)

april_fools_2021
noon

midnite = time(hour=0, minute=0, second=0)
midnite

# working with dates
todays_date = date.today()
todays_date_w_time = datetime.today()

todays_date
todays_date_w_time

now = datetime.now()
now

current_time = time(now.hour, now.minute, now.second)
current_time

datetime.combine(todays_date, current_time)

# working with datetime and strings
date_from_str = date.fromisoformat("2021-04-12")
date_from_str

date_string = "04-12-2021 12:45:55"
date_fmt = "%m-%d-%Y %H:%M:%S"

dt = datetime.strptime(date_string, date_fmt)
dt

# timedelta
todays_date - now
todays_date - date.fromisoformat("2021-01-01")

date.fromisoformat("2021-12-31") - todays_date

# Arithmetic with datetime
from datetime import timedelta

yesterday = timedelta(days=-1)
yesterday

now + yesterday
