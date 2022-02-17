from dateutil.relativedelta import relativedelta
import datetime

t_dt = datetime.datetime.now()
y_dt = t_dt + relativedelta(years=1)
print(y_dt)