import datetime
my_time=datetime.time(8,20,23)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(my_time.microsecond)
today=datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.ctime())
from datetime import datetime
my_date=datetime(2021,7,2,8,30)
print(my_date)
