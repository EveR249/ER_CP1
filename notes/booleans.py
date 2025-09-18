# ER 2nd Booleans notes
import time
import datetime as date

over = False
print(over)

name = "LaRose"
print(name.isalpha())

num = "4"
print(num.isnumeric())

print(bool(name))

current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current time in seconds since January 1st, 1970: {current_time}")
print(f"Current time: {readable_time}")

now = date.datetime.now()
hour = now.strftime("%H")
#month = %m %b %B
#day = %d
#year = %Y %y
#hour = %H
#minutes = %M
#seconds = %S

print(f"Current time according to datetime: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is in a string: {isinstance(hour, str)}")
print(f"My hour variable is in a string: {isinstance(hour, int)}")
print(f"My hour variable is in a string: {isinstance(hour, float)}")