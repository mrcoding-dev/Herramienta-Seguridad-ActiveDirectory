import os
from dotenv import load_dotenv

load_dotenv()

SENDER_MAIL = os.getenv('SENDER_MAIL')
RECIEVER_SMTP=os.getenv('RECIEVER_SMTP').split(',')
COMPANYS_NAME=os.getenv('COMPANYS_NAME').split(',')
DIAS_DESUSO=int(os.getenv('DIAS_DESUSO'))