import calendar
from datetime import date

dts = calendar.monthrange(2022, 2)
dt1 = date(2022, 2, dts[0])
dt2 = date(2022, 2, dts[1])
f_dt = dt1.strftime('%d %B %Y %A %H %M %S %p')
l_dt = dt2.strftime('%d %B %Y %A %H %M %S %p')
print(f_dt, '\n', l_dt)
