import smtplib
import Creds

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(Creds.Username, Creds.Password)

a = MIMEMultipart("")
a['subject'] = 'Test mail'
a['From'] = Creds.Username
a['To'] = 'zeciljain07@gmail.com'

html = """\
<html>
    <body>
        <p><b>This is a test mail<b><p><br>
        Hi,
        <br/>
        You have successfully sent an email!!
        </p>
    </body>
</html>
"""

p1 = MIMEText(html, 'html')
a.attach(p1)
