import os
from dotenv import load_dotenv

load_dotenv()

SENDER_MAIL = os.getenv('SENDER_MAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
SENDER_SMTP=os.getenv('SENDER_SMTP')
SENDER_PORT=os.getenv('SENDER_PORT')

RECIEVER_SMTP=os.getenv('RECIEVER_SMTP').split(',')

COMPANYS_NAME=os.getenv('COMPANYS_NAME').split(',')
LOGO_COMPANY=os.getenv('LOGO_COMPANY').split(',')

DIAS_DESUSO=int(os.getenv('DIAS_DESUSO'))