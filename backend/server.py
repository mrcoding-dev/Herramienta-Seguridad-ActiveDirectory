import atexit
import subprocess
import threading
from datetime import datetime
import pythoncom
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse
from pyad.adquery import ADQuery
import pandas as pd
from pyad import pyad,pyadutils,aduser
from clase_ad import ad,readToken

from dotenv import load_dotenv
import os

def validar_token():
    token=readToken()
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


def update_token(new_token:str):
    with open("token.txt", "w") as f:
        f.write(new_token)


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/desuso")
async def desuso():
    pythoncom.CoInitialize()

    validarcion_token=validar_token()
    if validarcion_token:
        value =ad.envio_desuso()
        if value:

            response={"message": "Proceso de desuso completado"}
            return JSONResponse(content=response, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Error al ejecutar el proceso de desuso, por favor chequea el token JWT")
    else:
        raise HTTPException(status_code=404, detail="Error al ejecutar el proceso de desuso, por favor chequea el token JWT")


class TokenInput(BaseModel):
    message: str


@app.post("/agregar-token")
async def agregar_token(token_input: TokenInput):
    token = token_input.message
    if token:
        ##estatus code 200
        update_token(token)
        response={"message": "Token JWT agregado"}
        return JSONResponse(content=response, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Error al agregar el token JWT")


def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


def run_desuso():
    subprocess.call("desuso.exe")


@atexit.register
def on_exit():
    server_thread.join()
    desuso_thread.join()


if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    desuso_thread = threading.Thread(target=run_desuso)
    desuso_thread.start()
