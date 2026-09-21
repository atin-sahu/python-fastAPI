from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.post("/users")
def create_user(user: User):
    return user