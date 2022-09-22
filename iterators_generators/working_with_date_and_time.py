# import calendar
#
# print(calendar.calendar(2022))

from datetime import datetime, timedelta, date, time
#print(datetime.now())
now = datetime.now()
print(f"{now:%A, %B %d %Y}")

