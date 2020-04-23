
# main.py

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


app = FastAPI()

app.counter = -1

app.patients = []

# Zadanie 1

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

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


@app.get("/welcome")
def powitanie():
    return {"message": "Hello My Friend"}


@app.get("/")
def powitanie2():
    return {"message": "Hello Everybody"}


