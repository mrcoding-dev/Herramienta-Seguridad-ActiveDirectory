import time
import asyncio
import accounts

from mail import file_generator,mail_settings,helper





def enviar_reporte(usuarios,empresa,logo):
       file_generator.generate_daily_report(usuarios,empresa)
       mail_settings.enviar_reporte_desuso(accounts.RECIEVER_SMTP,empresa,logo)
       helper.delete_file('desuso_report.xlsx')

       return True



