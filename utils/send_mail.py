import smtplib
from smtplib import SMTPException
from email.message import EmailMessage
from email.utils import make_msgid
import ssl
from config.config import settings
from utils.gen_html import gen_html


def send_mail(displayName=None, mail=None, cc=None, subject="", message=None, html=None):
    """
        Parameters
        ----------
        displayName: str
            The Name to Display on When email is not opened, will not set if not provided
        mail: str
            The mail address you wanna send email to
            note: if RECIEVER_MAIL is set in .env then it will not send mail to it.
            but it will include it in "reply" and anywhere in the html or message template
        cc: str
            send cc to the address provided, else send to the sende email in .env
        subject: str
            Subject of the mail
        message: str
            You can either choose message or html
        html: str
            The html you want to send
    """
    try:
        # Configuring Email
        mail = EmailMessage()
        mail["From"] = f"{displayName} <{settings.MAIL}>" if displayName else settings.MAIL
        mail["To"] = settings.RECIEVER_MAIL if settings.RECIEVER_MAIL else mail
        mail["Subject"] = subject
        mail["Cc"] = cc if cc else settings.MAIL
        mail["reply-to"] = mail
        if html:
            asparagus_cid = make_msgid()
            mail.add_alternative(html.format(
                asparagus_cid=asparagus_cid[1:-1]), subtype='html')
        elif message:
            mail.set_content(message)
        else:
            mail.set_content("")
        context = ssl.create_default_context()
        # Configuring Server
        server = smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT, context=context)
        server.ehlo()
        server.login(settings.MAIL, settings.MAIL_PASS)
        server.sendmail(settings.MAIL, settings.RECIEVER_MAIL, mail.as_string())
        # payload = None coz no error
        return {"message": "Mail Sent", "code": 200, "payload": None}

    except SMTPException as error:
        error_code = error.smtp_code
        error_payload = str(error.smtp_error)
        error_message = "An Error Occoured"

        print(f"Error code: {error_code}")
        print(f"payload: {error_payload}")
        print(f"Message: {error_message}")

        rv = {"code": error_code, "payload": error.smtp_error, "message": error_message}
        return rv

    finally:
        server.quit()
