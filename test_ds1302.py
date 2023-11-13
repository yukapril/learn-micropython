from machine import Pin
from ds1302 import DS1302
import utime

# clk-clk, dio-dat, cs-rst
clk = Pin(4)
dio = Pin(5)
cs = Pin(2)

current_time = utime.time()
formatted_time = utime.localtime(current_time)
year, month, day, hour, minute, second, weekday, yearday = formatted_time
print("System Time: %d-%d-%d %d:%d:%d" % (year, month, day, hour, minute, second))

ds = DS1302(clk=clk, dio=dio, cs=cs)
Year, Month, Day, Weekday, Hour, Minute, Second = ds.DateTime()
print("DS1032 Time: %d-%d-%d %d:%d:%d" % (Year, Month, Day, Hour, Minute, Second))

# set time
# ds.DateTime([year, month, day, weekday, hour, minute, second])
