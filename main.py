
# main.py

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()

app.counter = 0

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

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)

class GiveMeSomethingRq(BaseModel):
    name: str
    surename: str

class GiveMeSomethingResp(BaseModel):
    id: int
    patient: dict

@app.post("/patient", response_model=GiveMeSomethingResp)
def method_post(rq: GiveMeSomethingRq):
    n = app.get('/counter')
    return GiveMeSomethingResp(id=n, patient=rq.dict())



# class GiveMeSomethingRq(BaseModel):
#     first_key: str
#     constant_data: str = "POST"

# class GiveMeSomethingResp(BaseModel):
#     received: dict
#     constant_data: str = "POST"

# @app.post("/", response_model=GiveMeSomethingResp)
# def receive_something(rq: GiveMeSomethingRq):
#     global metoda
#     metoda = 'POST'
#     return GiveMeSomethingResp(received=rq.dict())

# @app.post("/", response_model=Metoda)
# def read_post(metoda: Metoda):
# 	metoda.method = 'POST'
#     return {"message": " pandemic!"}

# @app.get('/method')
# def read_method():
#     return {'method': app.metoda}

# @app.get('/method', response_model=Metoda)
# def update_method():
#     return {'method': 'POST'}