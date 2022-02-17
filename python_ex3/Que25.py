from dateutil.relativedelta import relativedelta
import datetime

t_dt = datetime.datetime.now()
m_dt = t_dt + relativedelta(months=1)
print(m_dt)