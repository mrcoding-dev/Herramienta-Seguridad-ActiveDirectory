from pyad import aduser,adquery,pyad,pyadutils
import datetime
import accounts
def readEnv():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    return os.getenv("app_id"), os.getenv("api_key"), os.getenv("index_id")

def extractLeadership(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["manager"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            return row["manager"]
    else:
        print("No posee atributo manager")
        return None


def extractUsersFromAD():
    users = dict()
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["name", "sAMAccountname", "lastLogonTimestamp", "employeeID"],
        where_clause="objectClass = 'user'",
    )
    for row in q.get_results():

        if row["employeeID"] == "generico" or row["employeeID"] == "sala":
            print(f'{row["employeeID"]} es generico')
            pass

        elif "bc20" in row["name"] or "bd20" in row["name"] or "bl20" in row["name"]:
            print(f'{row["name"]} es bc20 o bd20')
            pass
        else:
            if row["lastLogonTimestamp"]:
                print(pyadutils.convert_datetime(row["lastLogonTimestamp"]))
                days_not_use = (datetime.datetime.now() - pyadutils.convert_datetime(row["lastLogonTimestamp"])).days
                if days_not_use > 90:
                    print(f'{row["sAMAccountname"]} no se ha conectado en {days_not_use} dias')
                    users[row["sAMAccountname"]] = days_not_use
                else:
                    print(f'{row["sAMAccountname"]} No entra en proceso de desuso')
            else:
                print(f'{row["sAMAccountname"]} no posee inicio de sesion')
    return users


def extractUsersFromADToArray(company):
    #extract users from AD and return a array with the username, order by company
    users = []
    q = adquery.ADQuery()
    q.execute_query(
        attributes=["name", "sAMAccountname", "lastLogonTimestamp", "employeeID","company"],
        where_clause="objectClass = 'user'",
    )
    for row in q.get_results():
        if row["employeeID"] == "generico" or row["employeeID"] == "sala":
            #print(f'{row["employeeID"]} es generico')
            pass

        elif "bc20" in row["name"] or "bd20" in row["name"] or "bl20" in row["name"]:
            #print(f'{row["name"]} es bc20 o bd20')
            pass
        elif row["lastLogonTimestamp"] is None:
            #print(f'{row["sAMAccountname"]} no posee inicio de sesion')
            pass
        else:
            days_not_use = (datetime.datetime.now() - pyadutils.convert_datetime(row["lastLogonTimestamp"])).days
            #if days_not_use > 90:
            if days_not_use > accounts.DIAS_DESUSO:
                if row["company"] == company:
                    users.append(row["sAMAccountname"])

    return users


def extractLastLogon(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["lastLogonTimestamp"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            if row["lastLogonTimestamp"] is None:
        
                return "No posee atributo lastLogonTimestamp"
            else:
                return pyadutils.convert_datetime(row["lastLogonTimestamp"])
    else:
        return "No posee atributo lastLogonTimestamp"
    

def extractRutFromAD(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["employeeID"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            return row["employeeID"]
    else:
        #print("No posee atributo employeeID")
        return None

def extractCompanyFromAD(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["company"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            return row["company"]
    else:
        print("No posee atributo company")
        return "No posee"

def extractEmail(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["mail"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
         for row in q.get_results():
            return row["mail"]
    else:
        print("No posee atributo mail")
        return "No posee"

def extractName(usernt):
    #nota esto trae el nombre completo, ejemplo pepeto garza
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["name"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            return row["name"]
    else:
        print("No posee atributo name")
        return "No posee"
    
def getCN(usernt):
    q = adquery.ADQuery()

    q.execute_query(
        attributes=["cn"],
        where_clause="sAMAccountName = '{}'".format(usernt)
    )
    if q.get_row_count() > 0:
        for row in q.get_results():
            return row["cn"]
    else:
        #print("No posee atributo cn")
        return None

def changeUsername(usernt):
    cn=getCN(usernt)
    user = aduser.ADUser.from_cn(cn)
    #bcyearmonthday
    #get display name actual
    namez = user.get_attribute("displayName")
    newusername = f'bd{datetime.datetime.now().strftime("%Y%m%d") + " " +namez[0]}'
    #replace displayName
    user.update_attribute("displayName", newusername)
    print(f'{usernt} renombrado')


def desactivateUser(usernt):
    cn = getCN(usernt)
    user = aduser.ADUser.from_cn(cn)
    user.disable()
    print(f'{usernt} desactivado')

def activateUser(usernt):
    cn = getCN(usernt)
    user = aduser.ADUser.from_cn(cn)
    user.enable()
    print(f'{usernt} activado')


