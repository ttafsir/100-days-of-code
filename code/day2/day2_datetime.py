from datetime import timedelta, datetime


t = timedelta(days=4, hours=10)

print(t.days)
print(t.seconds)

# timedelta objects have no 'hours' attribute and the seconds
# only go up to the equivalent of 24 hours.
# t.hours  # fails
print(t.seconds / 60 / 60)  # <- 10 hours

total_seconds = t.total_seconds()
print(total_seconds)  # <- 381600.0
print((((total_seconds / 60 / 60) - 10.0)) / 24)  # 4 days

eta = timedelta(hours=6)
today = datetime.today()

print(today + eta)
