
# main.py

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

#@app.get("/method")
#def read_method():
#    return {"method": "METHOD"}



class GiveMeSomethingRq(BaseModel):
    first_key: str

class GiveMeSomethingResp(BaseModel):
    received: dict
    constant_data: str = "POST"

@app.post("/", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
	return GiveMeSomethingResp(received=rq.dict())