
# main.py

from fastapi import FastAPI, Depends, HTTPException, Response,Request, Cookie

from pydantic import BaseModel

import base64

from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

security = HTTPBasic()

app = FastAPI()

app.counter = -1

app.patients = []

app.sesje = []

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


# @app.get("/welcome")
# def powitanie():
#     return {"message": "Hello My Friend"}


@app.get("/")
def powitanie2():
    return {"message": "Hello Everybody"}


# Zadanie 2

app.login = 'trudnY'
app.haslo = 'PaC13Nt'

app.secret_key = "napis"


@app.post('/login')
def create_cookie(response: Response, credentials: HTTPBasicCredentials = Depends(security)):
    login = credentials.username
    password = credentials.password

    if login==app.login and password==app.haslo:
        secret = (f'{login}{password}{app.secret_key}')
        session_token = base64.b64encode(bytes(secret, 'ascii'))
        response.set_cookie(key="session_token", value=session_token)

        app.sesje.append(str(session_token)[2:-1])

        response.headers["Location"] = "/welcome"
        response.status_code = 307
        return response
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")



# zadanie 3

@app.post("/logout")
def wyloguj(response: Response, session_token: str = Cookie(None)):
    session_token = session_token[2:-1]

    if session_token in app.sesje:
        app.sesje.remove(session_token)
        response.headers["Location"] = "/"
        response.status_code = 307
        #response.set_cookie(key="session_token", value=session_token)
        return response
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")




# Zadanie 4 

@app.get("/welcome")
def powitanie(request: Request, session_token: str = Cookie(None)):
    session_token = session_token[2:-1]

    if app.sesje == []:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if session_token not in app.sesje:
        raise HTTPException(status_code=401, detail="Unauthorized")        

    return templates.TemplateResponse("item.html", {"request": request, 'user': app.login})



