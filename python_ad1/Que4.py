import smtplib
import Creds

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(Creds.Username, Creds.Password)

text = """
This is a test mail
Hi,
You have successfully sent an email!!
"""

s.sendmail(Creds.Username, 'zeciljain07@gmail.com', text)
s.quit()