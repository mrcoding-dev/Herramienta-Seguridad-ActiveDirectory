import datetime
import os
import shutil

import pyad
from pyad import pyadutils
from pyad.adquery import ADQuery
import pandas as pd
from pyad import pyad,pyadutils,aduser
from mail import correo



def readEnv():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    return os.getenv("SENDER_MAIL"), os.getenv("RECIEVER_SMTP"), os.getenv("COMPANYS_NAME"), os.getenv("DIAS_DESUSO")

sender_mail, reciever_smtp, companys_name, dias_desuso = readEnv()

dias_desuso=int(dias_desuso)
def getCN(usernt):
    try:
        if usernt == "Administrador":
            return None
        q = ADQuery()

        q.execute_query(
            attributes=["cn"],
            where_clause="sAMAccountName = '{}' ".format(usernt)
        )

        if q.get_row_count() ==1:
            for row in q.get_results():
                return row["cn"]
        elif q.get_row_count() > 1:
            for row in q.get_results():
                return row["cn"][0]
        else:
            #print("No posee atributo cn")
            return None
    except Exception as e:
        print("Ocurrio un error al obtener el cn de a {}".format(usernt))
        print(e)
        return None

def desactivateUser(usernt):
    try:
        cn = getCN(usernt)
        user = aduser.ADUser.from_cn(cn)
        user.disable()
        print(f'{usernt} desactivado')
    except Exception as e:
        print("Ocurrio un error al desactivar el usuario {}".format(usernt))
        print(e)

def changeUsername(usernt):
    try:
        cn=getCN(usernt)
        user = aduser.ADUser.from_cn(cn)
        #bcyearmonthday
        #get display name actual
        namez = user.get_attribute("displayName")
        print(namez)
        if len(namez) > 1:
            namez = namez[0]
        else:
            namez = namez[0] if namez else ''
        newusername = f'bd{datetime.datetime.now().strftime("%Y%m%d")} {namez}'

        #replace displayName
        user.update_attribute("displayName", newusername)
        print(f'{usernt} renombrado')
    except Exception as e:
        print("Ocurrio un error al cambiar el nombre de usuario {}".format(usernt))
        print(e)


def getUsersFromAD():
    q = ADQuery()
    q.execute_query(
        attributes=["sAMAccountname"],
        where_clause="objectClass = 'user'",
    )
    return [row["sAMAccountname"] for row in q.get_results()]



def readToken():
    with open("token.txt", "r") as f:
        token = f.read().strip()
    return token

class AD:
    def __init__(self):
        self.data = {}
        self.names = {}
        self.titles = {}
        self.companies = {}
        self.mails = {}
        self.departments = {}
        self.pwd_last_sets = {}
        self.manager = {}
        self.upn = {}
        self.last_logon_timestamps = {}
        self.when_created = {}
        self.cn = {}

        q = ADQuery()
        q.execute_query(
            attributes=["sAMAccountName", "displayName", "employeeID", "title", "company", "mail", "department",
                        "pwdLastSet", "lastLogonTimestamp", "whenCreated", "userPrincipalName",
                        "manager","cn"],
            where_clause="objectClass = 'user'",
        )
        exclusiones = ["administrador", "ad$", "adsyncmsafb3f6$"]

        for row in q.get_results():


            if row["sAMAccountName"].lower() in exclusiones:
                continue

            else:
                self.data[row["sAMAccountName"].lower()] = row["employeeID"] if row["employeeID"] else "No posee rut"
                self.names[row["sAMAccountName"].lower()] = row["displayName"]
                self.titles[row["sAMAccountName"].lower()] = row["title"]
                self.companies[row["sAMAccountName"].lower()] = row["company"]
                self.mails[row["sAMAccountName"].lower()] = row["mail"]
                self.departments[row["sAMAccountName"].lower()] = row["department"]
                self.pwd_last_sets[row["sAMAccountName"].lower()] = pyadutils.convert_datetime(row["pwdLastSet"]) if row[
                    "pwdLastSet"] else None
                self.manager[row["sAMAccountName"].lower()] = row["manager"]
                self.upn[row["sAMAccountName"].lower()] = row["userPrincipalName"]
                self.last_logon_timestamps[row["sAMAccountName"].lower()] = pyadutils.convert_datetime(row["lastLogonTimestamp"]) if row["lastLogonTimestamp"] else None
                self.when_created[row["sAMAccountName"].lower()] = row["whenCreated"]
                self.cn[row["sAMAccountName"].lower()] = row["cn"]





    def esta_user(self, user: str) -> bool:
        """Indica si el usernt se encuentra en ad"""
        try:
            if user.lower() in self.data:
                return True
        except Exception as e:
            print(e)
            return False

    def get_cn_x(self,user:str):
        return self.cn[user.lower()]

    def desactivar_usuario(self, usernt: str) -> bool:
        """Desactiva el usuario en el AD"""
        usernt = usernt.lower()
        try:
            cn = self.get_cn_x(usernt)
            user = aduser.ADUser.from_cn(cn)
            user.disable()
            return True
        except Exception as e:
            print(e)
            return False
    def cambiar_username(self, usernt: str) -> bool:
        """Cambia el nombre de usuario en el AD"""
        usernt = usernt.lower()
        try:
            cn = self.get_cn_x(usernt)
            user = aduser.ADUser.from_cn(cn)
            # bcyearmonthday
            # get display name actual
            namez = user.get_attribute("displayName")
            if len(namez) > 1:
                namez = namez[0]
            else:
                namez = namez[0] if namez else ''
            newusername = f'bd{datetime.datetime.now().strftime("%Y%m%d")} {namez}'

            # replace displayName
            user.update_attribute("displayName", newusername)
            return True
        except:
            return False

    def buscar_rut(self, usernt: str) -> str:
        usernt = usernt.lower()
        """Busca el rut del usuario mediante el usernt """
        try:
            return self.data[f'{usernt.lower()}']

        except:
            # print("usuario no encontrado en mayusculas")
            pass
        try:
            return self.data[f'{usernt}']

        except:
            # print("usuario no encontrado tal cual")
            pass
        try:
            return self.data[f'{usernt.upper()}']

        except:
            return 'No se encuentra usuario'

    def cantidad_usuarios(self) -> int:
        """Muestra la cantidad de usuarios que existen en el AD"""
        return len(self.data)

    def extrae_rut_jefe(self, usernt: str) -> str:
        usernt = usernt.lower()
        """Extrae el rut del jefe de un usuario dado un usernt"""
        try:
            return self.rut_jefe[usernt]
        except:
            return "Usuario no posee jefe"

    def extraer_correo_jefatura(self, usernt: str) -> str:
        usernt = usernt.lower()
        """Extrae el correo de la jefatura de un usuario dado un usernt"""
        try:
            rut_jefe = self.extrae_rut_jefe(usernt)
            if rut_jefe == "Usuario no posee jefe":
                return "Usuario no posee jefe"
            else:
                inverted_dict = {v: k for k, v in self.data.items()}

                usernt_jefe = inverted_dict.get(rut_jefe, None)

                correo = self.mails[usernt_jefe]
                return correo

        except:
            # print("Usuario no posee correo")
            pass

    def extraer_correo_manager(self, usuario):
        usernt = usuario.lower()
        """Extrae el correo del manager de un usuario"""
        import re

        try:
            nombre_manager = self.manager[usuario]
            nombre_manager = re.search('CN=(.*?),', nombre_manager).group(1)
            inverted_dict = {v: k for k, v in self.names.items()}
            usernt_manager = inverted_dict.get(nombre_manager, None)
            correo_manager = self.mails[usernt_manager]
            return correo_manager
        except:
            # print(usuario)
            return "Usuario no posee jefe"

    def obtener_empresa(self, usernt: str):
        usernt = usernt.lower()
        """Extrae la empresa de un usuario dado un usernt"""
        try:
            empresa = self.empresa[usernt]
        except:
            print("Usuario no posee empresa")
            pass
        if pd.isna(empresa):
            return "No posee atributo 3 asociado"
        else:
            return empresa

    def hallar_ruts_repetidos(self):
        """Esta funcion devuelve un listado de ruts que se encuentra repetidos en el AD"""
        rev_multidict = {}
        for key, value in self.data.items():
            if value not in ["generico", "sala"]:
                rev_multidict.setdefault(value, set()).add(key)

        # Imprime los usuarios que se encuentran repetidos (excepto "generico" y "sala")
        repetidos = [key for key, values in rev_multidict.items() if
                     len(values) > 1 and key not in ["generico", "sala"]]
        for key, value in rev_multidict.items():
            if len(value) > 1 and key not in ["generico", "sala"]:
                print(f'{key} : {value}')

        return repetidos

    def hallar_usernt_by_rut(self, rut: str) -> str:
        """Funcion encuentra el usuariont otorgando un rut"""
        for key, value in self.data.items():
            if value == rut.lower():
                return key

        return "No existe rut"

    def existe_usuario_by_rut(self, rut: str) -> bool:
        """Funcion que indica si existe un usuario en el AD otorgando un rut"""
        return rut.lower() in self.data.values()

    def nombre_by_usernt(self, usernt: str) -> str:
        usernt = usernt.lower()
        """Funcion que devuelve el nombre de un usuario otorgando su usernt"""
        return self.names[usernt]

    def es_bl_bc_o_bd(self, usernt: str) -> bool:
        usernt = usernt.lower()
        """Funcion que indica si un usuario es bl, bc o bd"""
        nombre = self.nombre_by_usernt(usernt)
        if "bc20" in str(nombre) or "bd20" in str(nombre) or "bl20" in str(nombre):
            return True
        else:
            return False

    def fecha_de_creacion_desuso(self, usernt: str):
        import datetime
        import pytz
        import pywintypes
        """Funcion que retorna los dias de desuso de un usuario"""
        fecha = self.when_created[usernt]
        tz = pytz.timezone('Europe/London')
        fecha_naive = fecha.replace(tzinfo=None)  # Eliminar información de zona horaria
        fecha_aware = tz.localize(fecha_naive)  # Convertir a objeto datetime.datetime con información de zona horaria
        now_aware = datetime.datetime.now(
            tz)  # Obtener la hora actual como objeto datetime.datetime con información de zona horaria
        delta = now_aware - fecha_aware
        days_not_use = delta.days
        return days_not_use

    def fecha_dias_exchange(self, display_name: str):
        """Retorna los dias de desuso del exchange online"""
        estado = self.esta_en_exchange(display_name)

        if estado == True:

            from datetime import datetime
            fecha = self.activity_exchange[display_name]
            if pd.isna(fecha) is False:
                fecha_dada_obj = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
                fecha_actual = datetime.now()
                diferencia = fecha_actual - fecha_dada_obj
                return diferencia.days
            else:
                # print("No ha iniciado sesion en exchange")
                return "No existe"
        else:
            return "No existe"

        # def fecha_de_expiracion_desuso(self, usernt: str):
        #    from datetime import datetime
        #    fecha = self.account_expires[usernt]
        #    fecha_dada_obj = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        #    fecha_actual = datetime.now()
        #    diferencia = fecha_actual - fecha_dada_obj

        #    return diferencia.days

    def obtener_inicio_sesion_logon(self, usernt: str):
        """Funcion que retorna la fecha de inicio de sesion del usuario"""
        from datetime import datetime
        fecha = self.last_logon_timestamps[usernt]
        if pd.isna(fecha):
            return "No ha iniciado sesion en mas de 60 dias"
        else:
            fecha_formateada = datetime.strptime(str(fecha), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            return fecha_formateada

    def obtener_empresa_individual(self, usernt: str):
        """Esto trae el atributo company"""
        empresa = self.companies[usernt]
        if pd.isna(empresa):
            return "No company"
        else:
            return empresa

    def fecha_de_creacion(self, usernt: str):
        """Funcion que retorna la fecha de creacion del usuario"""
        return self.when_created[usernt]

    def devolver_usernt_por_apellidos(self, apellidos: str) -> str:
        """Funcion que devuelve el usernt de un usuario otorgando sus apellidos"""
        for key, value in self.names.items():
            if apellidos.lower() in key.lower():
                return value

        return "No existe usuario"

    def obtener_desuso_by_lastlogintimestamp_by_usernt(self, usernt: str) -> str:
        """Funcion que retorna los dias de desuso de un usuario otorgando su usernt"""
        hoy = datetime.datetime.now()
        last_logon_timestamp = self.last_logon_timestamps[usernt]
        if pd.isna(last_logon_timestamp):
            return "No se encuentra usuario"
        else:
            format_string = '%Y-%m-%d %H:%M:%S.%f'
            last_logon_timestamp = datetime.datetime.strptime(last_logon_timestamp, format_string)
            days_since_last_login = (hoy - last_logon_timestamp).days
            print(f'{days_since_last_login} desde el ultimo logueo')
            return str(days_since_last_login)

    def usuarios_sin_logueo_pwdLastSet_o_lastLogonTimestamp_reciente(self) -> list:
        import datetime
        """Devuelve una lista de los usuarios que no se han logueado o actualizado su contraseña en los últimos 60 días"""
        usuarios = []
        for user_nt, last_logon_timestamp in self.last_logon_timestamps.items():
            if self.es_bl_bc_o_bd(user_nt):
                pass
            elif self.buscar_rut(user_nt) in ["generico", "sala"]:
                pass
            else:
                user_nt=user_nt.lower()
                pwd_last_set = self.pwd_last_sets[user_nt]
                if pd.isna(pwd_last_set) is True and pd.isna(last_logon_timestamp) is True:
                    # Si pwdLastSet y lastLogonTimestamp son NaN, el usuario nunca se ha logueado o actualizado su contraseña
                    # si esa cuenta no ha tenido movimiento y fue creada en mas de 60 dias va en consulta es decir se agrega
                    if ad.fecha_de_creacion_desuso(user_nt) >= dias_desuso:
                        usuarios.append(user_nt)
                    else:
                        pass
                else:
                    if pd.isna(last_logon_timestamp) is False and pd.isna(pwd_last_set) is True:
                        last_logon_date = datetime.datetime.strptime(last_logon_timestamp.split('.')[0],
                                                                     '%Y-%m-%d %H:%M:%S')

                        time_diff_logon = datetime.datetime.now() - last_logon_date
                        if time_diff_logon.days >= dias_desuso:
                            usuarios.append(user_nt)
                        else:
                            pass
                    elif pd.isna(pwd_last_set) is False and pd.isna(last_logon_timestamp) is True:
                        time_diff_pwd = datetime.datetime.now() - pwd_last_set
                        if time_diff_pwd.days >= dias_desuso:
                            usuarios.append(user_nt)
                        else:
                            pass
                    elif pd.isna(pwd_last_set) is False and pd.isna(last_logon_timestamp) is False:
                        last_logon_date = last_logon_timestamp
                        pwd_last_set_date = pwd_last_set
                        time_diff_logon = datetime.datetime.now() - last_logon_date
                        time_diff_pwd = datetime.datetime.now() - pwd_last_set_date

                        if time_diff_logon.days >= dias_desuso and time_diff_pwd.days >= dias_desuso:
                            usuarios.append(user_nt)
                        else:
                            pass
                    else:
                        pass
        return usuarios

    def generar_excel_desuso_completo(self):
        """Genera un excel con los usuarios desuso"""
        usuarios = self.usuarios_sin_logueo_pwdLastSet_o_lastLogonTimestamp_reciente()

        df_usuarios = pd.DataFrame({
            'Cuenta Dominio': [usuario for usuario in usuarios],
            'Último Inicio de Sesión': [self.obtener_inicio_sesion_logon(usuario) for usuario in usuarios],
            'Nombre': [self.nombre_by_usernt(usuario) for usuario in usuarios]
        })

        # Crea el objeto writer para escribir en el archivo Excel
        with pd.ExcelWriter('datos_desuso/usuarios_desuso.xlsx', engine='xlsxwriter') as writer:
            df_usuarios.to_excel(writer, index=False, sheet_name='Usuarios')

            # Obtén el libro y la hoja de trabajo para aplicar el formato de fecha
            workbook = writer.book
            worksheet = writer.sheets['Usuarios']

            # Define el formato de fecha y hora adecuado
            format1 = workbook.add_format({'num_format': 'dd/mm/yyyy hh:mm:ss'})
            worksheet.set_column('B:B', 20, format1)

        # desactivamos los usuarios y cambiarmos el display name---------------------

        for usuario in usuarios:

            self.desactivar_usuario(usuario)
            self.cambiar_username(usuario)


    def envio_desuso(self):
        """Envía el excel con los usuarios desuso a los correos de las jefaturas"""
        from mail.correo import enviar_correo
        from mail.accounts import RECIEVER_SMTP
        jwt = readToken()

        # Genera el archivo Excel con los usuarios en desuso
        excel_path = 'datos_desuso\\usuarios_desuso.xlsx'
        self.generar_excel_desuso_completo()

        # Envía el archivo Excel al correo determinado
        envio= enviar_correo(datetime.datetime.now().strftime("%d-%m-%Y"),excel_path,jwt,RECIEVER_SMTP)


        #mueve el archivo a la carpeta de log
        # si ya hay un archivo con el mismo nombre lo borra
        if os.path.exists('log\\usuarios_desuso.xlsx'):
            os.remove('log\\usuarios_desuso.xlsx')

        shutil.move(excel_path, 'log\\usuarios_desuso.xlsx')

        if not envio:
            return False
        return True


ad = AD()




#ad.usuarios_sin_logueo_pwdLastSet_o_lastLogonTimestamp_reciente()