from fastapi import FastAPI
from pydantic import BaseModel
from app.config.db import Base, engine
app = FastAPI()

Base.metadata.create_all(engine)

