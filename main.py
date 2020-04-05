
# main.py

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()

app.counter = 0

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
    n = app.counter
    app.counter += 1
    app.patients.append(rq.dict())
    return GiveMeSomethingResp(id=n, patient=rq.dict())


# Zadanie 4

@app.get("/patient/{pk}", response_model=GiveMeSomethingRq)
def patient_get(pk: int):
    if app.counter<pk:
        raise HTTPException(status_code=404, detail="Item not found")
    return GiveMeSomethingRq(app.patients[pk])




