from fastapi import FastAPI,HTTPException
from process import desuso
from app import ProcesoDesuso

app = FastAPI()


@app.get("/desuso")
async def desuso():
    value=ProcesoDesuso()
    if value:
        return {"mesage": "Proceso ejecutado correctamente"}
    #return error
    else:
        raise HTTPException(status_code=404, detail="Error al ejecutar el proceso")
