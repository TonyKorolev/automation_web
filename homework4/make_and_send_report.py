import smtplib
import yaml
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open('testdata.yaml') as f:
    info = yaml.safe_load(f)

password = info['expassword']
report_file = 'log.txt'
from_mail = 'leonstark@mail.ru'
to_mail = 'leonstark@mail.ru'


msg = MIMEMultipart()
msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = 'Test report'



with open(report_file, 'rb') as f:
    part = MIMEApplication(f.read(), Name = report_file)
    # part['Content-Disposition'] = 'attachment; filename="%s"' % Path.absolute(report_file)
    msg.attach(part)

first_text = 'Test results'
msg.attach(MIMEText(first_text, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(from_mail, password)
text = msg.as_string()
server.sendmail(from_mail, to_mail, text)
server.quit()
