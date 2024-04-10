import datetime
from datetime import timedelta
import time

future_date = datetime.date(2025, 12, 24)
print(future_date)

some_time = datetime.time(13, 22, 45)
print(some_time)

future_datetime = datetime.datetime(2547, 5, 1, 4, 15, 00)
print(future_datetime)

# formatting datetime obj
print("______________________________________")
print("formatting datetime obj")
print(future_datetime.strftime("%A, %B %d, %Y"))
print(future_datetime.strftime("%H:%M:%S %p"))
print(future_datetime.strftime("%Y-%m-%d"))

# convert str to dateTime
print("______________________________________")
print("convert str to dateTime")
given_datetime_str = "3000 11 20 14:25:45"
parsed_datetime = datetime.datetime.strptime(given_datetime_str, "%Y %m %d %H:%M:%S")
print(parsed_datetime)

# using timedelta
print("______________________________________")
print("using timedelta")
print(future_datetime)
print(future_datetime + timedelta(days=-5))
print(future_datetime + timedelta(minutes=14))

# time
print("______________________________________")
print("time")
current_time_in_seconds_since_the_Epoch = time.time()
print(current_time_in_seconds_since_the_Epoch)
print(time.ctime(current_time_in_seconds_since_the_Epoch))
print(time.ctime(0))

# delaying program execution
print("start")
time.sleep(3)
print("stop")

# checking how much time to create large list
start_time = time.time()
my_list = []
for n in range(10_000_000):
    my_list.append(n)
print(my_list)
end_time = time.time()
print(f"Elapsed: {round(end_time - start_time, 2)} seconds")
