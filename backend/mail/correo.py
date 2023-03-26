import base64
import requests
import json

def readEnv():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    return os.getenv("SENDER_MAIL"), os.getenv("RECIEVER_SMTP"), os.getenv("COMPANYS_NAME"), os.getenv("DIAS_DESUSO")


sender_mail, reciever_smtp, companys_name, dias_desuso = readEnv()

mensaje = f"""
Estimad@(s):

De acuerdo a los procedimientos vigentes, se cursará el bloqueo automático de las cuentas adjuntas, por no haber sido utilizadas dentro de los últimos {dias_desuso} días.
En caso de requerir la extensión de alguna de las cuentas, favor de informar dentro de las próximas 48 horas, enviando la solicitud con su respectiva justificación al correo {sender_mail}.
Quedamos atentos a vuestros comentarios, de no recibirlos dentro del plazo otorgado, se procederá al bloqueo de las cuentas.

Cordialmente,

{companys_name}

"""


# Desuso 202302


# Cuerpo del correo electrónico


def enviar_correo(fecha: str, ruta: str, jwt: str,destinatarios:list,mensaje: str = mensaje):
    # Configuración de las credenciales
    # Aquí se reemplaza con tu token JWT
    headers = {
        'Authorization': 'Bearer ' + jwt,
        'Content-Type': 'application/json'
    }
    # Leer el archivo y codificar su contenido en Base64
    with open(ruta, 'rb') as file:
        file_content = file.read()
    file_name = 'cuentas_candidatas_desuso.xlsx'
    encoded_content = base64.b64encode(file_content).decode('utf-8')
    to_recipients = []
    for destinatario in destinatarios:
        to_recipients.append({
            "emailAddress": {
                "address": destinatario
            }
        })

    body = {
        "message": {
            "subject": f'Bloqueo de cuentas en desuso ({companys_name}){fecha}',
            "body": {
                "contentType": "Text",
                "content": mensaje
            },
            "toRecipients": to_recipients,
            "ccRecipients": [
                                {
                                    "emailAddress": {
                                        "address": f"{sender_mail}"
                                    }
                                },
                            ],
            "from": {
                "emailAddress": {
                    "address": f"{sender_mail}"
                }
            }, "attachments": [
                {
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": file_name,
                    "contentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "contentBytes": encoded_content
                }],
        },
        "saveToSentItems": "true"
    }
    # Envío del correo electrónico
    response = requests.post('https://graph.microsoft.com/v1.0/me/sendMail', headers=headers, data=json.dumps(body))

    if response.status_code == 202:
        print("El correo electrónico fue enviado exitosamente.")
        return True
    else:
        print("Error al enviar el correo electrónico: ", response.text)
        return False

#prueba de correo

