import smtplib
import Creds

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(Creds.Username, Creds.Password)

a = MIMEMultipart('')
a['subject'] = 'Test mail with attachments'
a['From'] = Creds.Username
a['To'] = 'zeciljain07@gmail.com'

html = """\
<html>
    <body>
        <h1>This is a test mail</h1><br>
        <p>Hi,<p>
        <br/>
        You have successfully sent an email!!
        </p>
    </body>
</html>
"""

p1 = MIMEText(html, 'html')
a.attach(p1)

f = 'TKR.pdf'
with open(f, "rb") as attachment:
    p2 = MIMEBase("application", "octet-stream")
    p2.set_payload(attachment.read())

encoders.encode_base64(p2)
a.attach(p2)

f1 = 'image1.jpg'
with open(f1, 'rb') as attachment:
    p3 = MIMEBase("application", "octet-stream")
    p3.set_payload(attachment.read())

encoders.encode_base64(p3)
a.attach(p3)
s.sendmail(Creds.Username, 'zeciljain07@gmail.com', a.as_string())
s.quit()
