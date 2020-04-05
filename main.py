
# main.py

from fastapi import FastAPI

from pydantic import BaseModel

class Metoda(BaseModel):
    method: str

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}


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