def ProcesoDesuso():
    """Esta funcion ejecuta todo el proceso de cuentas en desuso de manera manual, se ejecuta desde la terminal"""
    import accounts
    from process import extractData, desuso
    from mail import file_generator, mail_settings, helper, report
    from pyad import aduser, adquery, pyad, pyadutils
    import datetime
    desuso.dropAllAccounts()
    cuentas = desuso.desuso()
    for empresa in cuentas.keys():
        counter= 0
        if len(accounts.LOGO_COMPANY) < len(cuentas.keys()):
            logo = accounts.LOGO_COMPANY[0]
            try:
                desuso.uploadtoApi(cuentas[empresa])
                report.enviar_reporte(cuentas[empresa], empresa, logo)
            except Exception as e:
                print(e)
                return False
        elif len(accounts.LOGO_COMPANY) == len(cuentas.keys()):
            try:
                desuso.uploadtoApi(cuentas[empresa])
                report.enviar_reporte(cuentas[empresa], empresa, accounts.LOGO_COMPANY[counter])
            except Exception as e:
                print(e)
                return False
        elif len(accounts.LOGO_COMPANY) > len(cuentas.keys()):
            raise Exception("El numero de logos es mayor al numero de empresas")
        else:
            try:
                desuso.uploadtoApi(cuentas[empresa])
                report.enviar_reporte(cuentas[empresa], empresa, accounts.LOGO_COMPANY[0])
            except Exception as e:
                print(e)
                return False
        counter += 1
    return True


if __name__ == '__main__':
    ProcesoDesuso()
