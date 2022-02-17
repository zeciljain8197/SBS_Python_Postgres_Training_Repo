from dateutil.relativedelta import relativedelta
import  datetime

t_dt = datetime.datetime.now()
w_dt = t_dt + relativedelta(weeks=1)
print(w_dt)