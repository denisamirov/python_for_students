import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

server = 'smtp.yandex.ru'
user = 'YOUR'
password = 'YOUR'

recipients = ['YOUR']
sender = 'YOUR'
subject = 'Тема сообщения'
text = 'Текст сообщения sdf sdf sdf sdaf <b>sdaf sdf</b> fg hsdgh <h1>f sd</h1> dfhjhgs sd gsdfg sdf'
html = '<html><head></head><body><p>' + '<img src="https://img3.akspic.ru/previews/5/5/4/1/7/171455/171455-zhivopis-illustracia-art-voda-oblako-500x.jpg">'+ text + '</p></body></html>'

# filepath = "fish.jpg"
# basename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Python script <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
# part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
# part_file.set_payload(open(filepath, "rb").read())
# part_file.add_header('Content-Description', basename)
# part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
# encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
# msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()