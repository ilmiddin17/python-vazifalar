import calendar
print(calendar.weekheader(3))
print(calendar.month(2021,3))
print(calendar.calendar(2021))
print(calendar.monthcalendar(2021,3))
is_leap=calendar.isleap(2020)
print(is_leap)
how_many=calendar.leapdays(2004,2009)
print(how_many)
import datetime
import time
print(datetime.time(12,15))