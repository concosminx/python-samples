# data and times in python

from datetime import datetime, timezone, timedelta

print(datetime.now())

print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(hours=24, minutes=15)
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))  # string format time

user_date = input('Enter date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)