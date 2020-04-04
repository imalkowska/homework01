
# main.py

from fastapi import FastAPI

from pydantic import BaseModel

class MethodRequest(BaseModel):
    method: str

metoda = ''

app = FastAPI()

@app.get("/")
def root():
    global metoda
    metoda = 'GET'
    return {"message": "Hello World during the coronavirus pandemic!"}

class GiveMeSomethingRq(BaseModel):
    first_key: str
    constant_data: str = "POST"

class GiveMeSomethingResp(BaseModel):
    received: dict
    constant_data: str = "POST"

@app.post("/", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    global metoda
    metoda = 'POST'
    return GiveMeSomethingResp(received=rq.dict())

@app.get('/method')
def read_method():
    return {'message': metoda}
