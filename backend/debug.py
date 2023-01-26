from pyad import aduser,adquery,pyad,pyadutils
import datetime

import accounts
from process import extractData,desuso
from mail import file_generator,mail_settings,helper,report


desuso.dropAllAccounts()
cuentas=desuso.desuso()

#desuso empresas_usuarios = {'Vida Security S.A.': ['pgarza'], 'Banco Security': []}


#index and add accounts.LOGO_COMPANY


for empresa in cuentas.keys():
    if len(accounts.LOGO_COMPANY)>0:
        desuso.uploadtoApi(cuentas[empresa])
        for logo in accounts.LOGO_COMPANY:
            report.enviar_reporte(cuentas[empresa],empresa,logo)
    else:
        desuso.uploadtoApi(cuentas[empresa])
        report.enviar_reporte(cuentas[empresa],empresa,accounts.LOGO_COMPANY)