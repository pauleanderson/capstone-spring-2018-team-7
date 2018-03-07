import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

time = datetime.datetime.now()
from_address = "cofccapstoneteam7@gmail.com"
to_address = "koatliky@ya.ru"

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Today's apps worth attention"

body = "Hello N3twork Team, \nwe advise on checking the following apps today:"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_address,"datascience")
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()
