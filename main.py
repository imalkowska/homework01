
# main.py

from fastapi import FastAPI, Depends, HTTPException, Response, Cookie

from pydantic import BaseModel

import base64

from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

app = FastAPI()

app.counter = -1

app.patients = []

# Zadanie 1

# @app.get("/")
# def root():
#     return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.post("/method")
def method_post():
    return {"method": "POST"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

# Zadanie 3

class GiveMeSomethingRq(BaseModel):
    name: str
    surename: str

class GiveMeSomethingResp(BaseModel):
    id: int
    patient: dict

@app.post("/patient", response_model=GiveMeSomethingResp)
def patient_post(rq: GiveMeSomethingRq):
    app.counter += 1
    n = app.counter
    app.patients.append(rq.dict())
    return GiveMeSomethingResp(id=n, patient=rq.dict())


# Zadanie 4

@app.get("/patient/{pk}")
def patient_get(pk: int):
    if app.counter<pk:
        raise HTTPException(status_code=204, detail="No Content")
    return app.patients[pk]




# PRACA DOMOWA NR 3

# Zadanie 1


# def sprawdz_sesje(sesja: str):
# 	def wrapp(funkcja):
# 		if sesja != 'aaaa':
# 			raise HTTPException(status_code=403, detail="Unathorised")
# 		return funkcja
# 	return wrapp



@app.get("/welcome")
def powitanie():
    return {"message": "Hello My Friend"}


@app.get("/")
def powitanie2():
    return {"message": "Hello Everybody"}


# Zadanie 2

app.login = 'trudnY'
app.haslo = 'PaC13Nt'

app.secret_key = "abcdefgh"

@app.post("/login")
def create_cookie(response: Response, credentials: HTTPBasicCredentials = Depends(security)):
    login = credentials.username
    password = credentials.password
    secret = (f'{login}{password}{app.secret_key}')

    session_token = base64.b64encode(bytes(secret, "ascii"))
    response.set_cookie(key="session_token", value=session_token)
    if login==app.login and password==app.haslo:
        response.headers["Location"] = "/welcome"
        response.status_code = 307
        print('hej')
        return response
    else:
        raise HTTPException(status_code=403, detail="Unathorised")



