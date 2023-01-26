import smtplib, ssl, email
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mail import html_helper
import accounts

def enviar_reporte_desuso(receiver_email,empresa,logo):
    """Esta funcion recibe parametros y enviar el mail"""
    fecha= time.strftime("%d/%m/%Y")

    sender_email = accounts.SENDER_MAIL
    password = accounts.SENDER_PASSWORD

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f'Reporte Cuentas en desuso - {empresa}'
    msg["From"] = sender_email
    if len(receiver_email)>0:
        msg["To"] = ', '.join(receiver_email)
    else:
        msg["To"] = receiver_email[0]

    # HTML Message Part
    html_template = html_helper.reporte_html(fecha,empresa,logo)

    part = MIMEText(html_template, "html")
    msg.attach(part)
    # Add Attachment
    ecsel = MIMEBase('application', "octet-stream")
    ecsel.set_payload(open("desuso_report.xlsx", "rb").read())
    encoders.encode_base64(ecsel)
    ecsel.add_header('Content-Disposition', 'attachment; filename="desuso_report.xlsx"')
    msg.attach(ecsel)

    # Create secure SMTP connection and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(accounts.SENDER_SMTP, int(accounts.SENDER_PORT), context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )

