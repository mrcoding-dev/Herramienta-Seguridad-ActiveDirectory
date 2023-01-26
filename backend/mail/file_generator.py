import xlsxwriter

from process import extractData


def generate_daily_report(usuarios,company):
    workbook = xlsxwriter.Workbook('desuso_report.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    #extrae por el listado de usuarios
    for user in usuarios:
        rut = extractData.extractRutFromAD(user)
        company = extractData.extractCompanyFromAD(user)
        email = extractData.extractEmail(user)
        name = extractData.extractName(user)

        if rut is None:
            pass
        elif company is None:
            pass
        elif email is None:
            email="No posee"
        elif name is None:
            name="No posee"

        worksheet.write(row, 0, user)
        worksheet.write(row, 1, rut)
        worksheet.write(row, 2, name)
        worksheet.write(row, 3, company)
        worksheet.write(row, 4, email)
        worksheet.write(row, 5, str(extractData.extractLastLogon(user)))
        row += 1

    return workbook.close()


