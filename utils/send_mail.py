import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import ssl
from config.config import settings
from utils.gen_html import gen_html


def send_mail(firstName, lastName, email, subject, message):
    try:
        name = firstName+" "+lastName
        # Configuring Email
        mail = EmailMessage()
        mail["From"] = f"{firstName}@TheYummyServings <{settings.MAIL}>"
        mail["To"] = settings.RECIEVER_MAIL
        mail["Subject"] = "New Contact Request Recieved"
        mail["Cc"] = settings.MAIL
        mail["reply-to"] = email
        html = gen_html(name, email, subject, message)
        asparagus_cid = make_msgid()
        mail.add_alternative(html.format(
            asparagus_cid=asparagus_cid[1:-1]), subtype='html')
        context = ssl.create_default_context()
        # Configuring Server
        server = smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT, context=context)
        server.ehlo()
        server.login(settings.MAIL, settings.MAIL_PASS)
        server.sendmail(settings.MAIL, settings.RECIEVER_MAIL, mail.as_string())
        server.close()
    except Exception as error:
        print('Something went wrong... (here in send_mail)')
        print(error)