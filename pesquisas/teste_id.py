import datetime
from re import I
from sqlite3 import Time

now = datetime.datetime.now()
print(now)

hour = now.strftime("%I")
print(hour)

time = now.strftime("%I %M %S %f")
print(time)

date = now.strftime("%m %d %Y")
print(date)

id_doc = now.strftime("%m%d%Y%I%M%S%f")
print(id_doc)