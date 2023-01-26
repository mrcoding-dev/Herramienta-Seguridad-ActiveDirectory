from pyad import aduser,adquery,pyad,pyadutils
import datetime

import accounts
from process import extractData
from algoliasearch.search_client import SearchClient

app_id,api_key,index_id=extractData.readEnv()
client = SearchClient.create(app_id, api_key)
index = client.init_index(index_id)


def uploadtoApi(users):
    for usernt in users:
        rut = extractData.extractRutFromAD(usernt)
        company = extractData.extractCompanyFromAD(usernt)
        email = extractData.extractEmail(usernt)
        name = extractData.extractName(usernt)
        if rut is None:
            pass
        else:
            res = [
                {'usernt': usernt, 'objectID': rut, 'nombres': name, 'email': email,
                 'empresa': company, 'ultima_sesion': str(extractData.extractLastLogon(usernt)), 'rut': rut}
            ]
            index.save_objects(res, {'autoGenerateObjectIDIfNotExist': True})


def dropAllAccounts():
    index.clear_objects()


def desuso():
    empresas = accounts.COMPANYS_NAME
    users_by_company = {}
    for empresa in empresas:
        users = extractData.extractUsersFromADToArray(empresa)
        users_by_company[empresa] = users
        for usernt in users:
            extractData.changeUsername(usernt)
            extractData.desactivateUser(usernt)
    uploadtoApi(users_by_company)
    return users_by_company




